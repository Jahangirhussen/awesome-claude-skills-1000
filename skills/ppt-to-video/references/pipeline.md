# ppt-to-video 파이프라인 상세

## 0. 코드 위치

이 스킬의 `scripts/revoice/`가 실제 파이썬 패키지다. 작업할 프로젝트 폴더에
`revoice/`가 없으면 이 폴더의 것을 복사해 프로젝트 안에 두고(같은 디렉터리에서
`python -m revoice.xxx`로 호출하는 구조라 프로젝트 루트에 있어야 함), 있으면
날짜 비교 등으로 최신 버전인지 확인한 뒤 그대로 쓴다. 테스트: `python -m pytest tests`
(44개, `scripts/tests/`에 동봉).

## 1. 인제스트 — `revoice/deck.py`

```bash
python -m revoice.deck <파일.pptx> [출력폴더=deck]
```

- `export_slides()`: PowerPoint COM으로 슬라이드를 1920×1080 PNG로 원본 그대로
  내보낸다(`powershell` 경유 호출 — pywin32 불필요).
- `extract_outline()`: 슬라이드별 제목·본문·**발표자 노트**를 `python-pptx`로 추출.
- 결과: `deck/slide_NN.png` (23장이면 23개) + `deck/outline.json`.

발표자 노트에 이미 완성된 대본이 있어도 **그대로 베끼지 않는다** — 참고 자료일 뿐,
브랜드 나레이터 톤으로 다시 쓴다(아래 3절).

## 2. 매니페스트 스키마 — `revoice/manifest.py`

```python
Scene(id, type, file="", src_in="", src_out="", narration="", note="", flags=[])
```

| type | file 필요 | src_in/out | narration | 화면 | 소리 |
|---|---|---|---|---|---|
| `SLIDE` | O (`deck/slide_NN.png`) | 불필요(길이=TTS) | 필수 | PPT 요소 애니메이션(3절) | 신규 TTS |
| `VO` | 선택 | O(기존 영상 구간) 또는 file 지정 시 그 영상 | 필수 | 기존영상+구자막마스킹, 또는 file 그대로 | 신규 TTS |
| `ORIGINAL` | - | O | - | 기존영상 구간 | 원음 |
| `CLIP` | O | O | - | 그 파일 구간 | 원음 |
| `EXTERNAL` | O | O | - | 그 파일 구간(범퍼) | 원음 |

Manifest 최상위: `source, source_file, voice, tts_style, output, bgm{engine,prompt,duck}, scenes[]`.

인터뷰·증언처럼 원음을 쓰는 씬(`ORIGINAL`/`CLIP`)은 **브랜드 주장의 스파인이 아니라
증거로만** 쓴다 — 브랜드 나레이터가 도입("~들어보시죠")과 마무리 문장을 인접 SLIDE/VO
씬에서 맡고, CLIP은 원음 10~25초만 순수하게 재생한다. 노출 전 원 소유자/본사 확인
게이트를 거친다.

### 인터뷰 클립 소스 찾기

슬라이드 자체(발표자 노트나 본문)에 유튜브 URL+타임코드가 적혀 있는 경우가 많다 —
추측하지 말고 그 좌표를 먼저 찾는다. 다운로드:

```bash
python -m yt_dlp --js-runtimes node --extractor-args "youtube:player_client=android,web" \
  -f "bv*[height<=1080]+ba/b[height<=1080]" --download-sections "*시작-끝" \
  -o "출력.%(ext)s" --merge-output-format mp4 --retries 5 "<url>"
```

- `--js-runtimes node`: yt-dlp가 유튜브 서명 해독에 JS 실행기를 요구함(2026년 기준).
- 대본에 적힌 넓은 구간을 통으로 받은 뒤, **faster-whisper로 전사**해 실제 인용할
  10~25초 구간을 정확히 찾는다(문자열 매칭이 아니라 타임스탬프 확인 — 추측 금지).
- **640p 초과 화질은 PO 토큰이 필요해 막힐 수 있다**(구조적 제약, 2026년 시점). 여러
  플레이어 클라이언트를 시도해도 안 되면 640p로 진행하거나, 브라우저를 완전히 종료한
  뒤 `--cookies-from-browser chrome`을 시도할 수 있다고 사용자에게 안내한다.

## 3. PPT 요소 애니메이션 — `revoice/deck.py::render_animated_slides`

정지 이미지에 밋밋한 푸시인만 얹지 않는다 — PowerPoint COM의 네이티브 애니메이션
엔진(`Slide.TimeLine.MainSequence.AddEffect`)으로 요소가 순서대로 나타나는 모션을
만들고 `Presentation.CreateVideo()`로 슬라이드별 mp4로 뽑는다. HTML 재현이 아니라
PowerPoint 자체 렌더러가 원본을 그대로 쓰므로 브랜드 룩이 100% 보존된다.

- 슬라이드를 `Hidden` 토글하면 `CreateVideo`가 숨긴 슬라이드를 완전히 건너뛴다 —
  슬라이드마다 파일 복사·재오픈 없이 한 세션에서 일괄 처리.
- **나레이션 동기화**: 씬의 TTS 음성을 faster-whisper로 전사해 문장별 발화 종료
  시각(체크포인트)을 구하고, 화면 요소를 문서 순서대로 그 구간에 배분한다
  (`build.py::_sentence_checkpoints`) — 문자열 매칭이 아니라 **단어 개수 비율**로
  위치를 찾는다(TTS가 원문을 그대로 읽어도 whisper 재전사 철자가 달라질 수 있어서).
- `CreateVideo`는 **간헐적으로 실패**한다(같은 슬라이드가 재시도하면 성공 — 콘텐츠
  문제가 아니라 COM 자체의 산발적 오류). 최대 2회 재시도 + "성공 확인 전에는 기존
  파일을 지우지 않음"(임시 파일에 렌더 후 성공 시에만 교체)이 이미 구현돼 있다.
- msoAnimTrigger 상수 주의: `2`=WithPrevious(전부 동시), `3`=AfterPrevious(순차) —
  순차 등장을 원하면 반드시 3.

## 4. 렌더 — `revoice/build.py`

```bash
python -m revoice.build render --manifest <파일> --dry-run   # API 호출 없이 미리보기
python -m revoice.build render --manifest <파일>              # 변경분만 재빌드
python -m revoice.build render --manifest <파일> --only P03   # 그 씬만
python -m revoice.build render --manifest <파일> --all        # 캐시 무시 전체
python -m revoice.build render --manifest <파일> --static-slides  # PPT애니메이션 끄기
python -m revoice.build render --manifest <파일> --new-bgm    # BGM도 새로 생성
```

**증분 캐시가 핵심**: 나레이션·화면 소스가 바뀐 씬만 재빌드한다. 매번 전체를
재빌드하면 TTS API를 불필요하게 다시 호출하고(비용), BGM도 새로 생성돼 영상 전체의
배경음악이 바뀐다. `--only`로 좁혀서 반복 수정한다.

여러 매니페스트가 한 프로젝트에 병존할 수 있다(예: 기존 리컷용 + 신규 PPT용) —
`--manifest` 플래그로 구분하고, 각 매니페스트의 `output` 파일명이 서로 다르면
중간 산출물(리스트·베이스영상·BGM)도 자동으로 안 겹친다.

**렌더링 로직 자체를 고치면**(예: 리드인 처리 추가, 애니메이션 알고리즘 변경)
`build.py`의 `_CODEGEN_VERSION`/`_ANIM_CODEGEN_VERSION`을 올려야 한다 — 캐시는
입력 데이터만 해시하고 코드를 보지 않으므로, 안 올리면 낡은 세그먼트를 계속
재사용하는 사고가 난다.

## 5. 나레이션 톤 원칙

발표자 노트나 화면 텍스트를 순서대로 읽는 "화면 낭독"이 되기 쉽다 — 전문 진행자
톤을 만들려면:

- **직접 호칭** ("원장님", "여러분") 을 섞는다.
- **수사적 질문**으로 다음 내용을 예고한다 ("이게 뭘까요?").
- 숫자를 나열하지 않고 **인과관계로 재구성**한다 — "A. B. C." 대신 "A 덕분에 B가
  됐고, 그래서 C입니다."
- 서스펜스 문장 ("그런데 이 숫자, 그냥 믿지 마세요") 으로 다음 문장을 당긴다.
- 사실·수치는 절대 바꾸지 않는다 — 표현·리듬만 바꾼다.

## 6. 확인 게이트

`build.py::check_gate()`가 나레이션·노트에 `⚠`, `[확인`, `(대본 확인 필요)`, `TBD`가
남아 있으면 렌더를 차단한다. 1차 시도에서 이런 미확정 표식이 최종 프레임에 그대로
노출된 사고가 있었다 — 표식을 지우는 건 실제로 사용자 확인을 받은 뒤에만 한다.
`--force`로 우회할 수 있지만, 의도적인 경우가 아니면 쓰지 않는다.

## 7. 다른 환경으로 확장하고 싶다면

PPT 요소 애니메이션은 PowerPoint COM 전용 — Windows + 정품 데스크톱 오피스가 있는
컴퓨터에서만 동작한다. 이걸 웹 서비스(불특정 다수가 업로드만 하면 영상이 나오는 형태)
로 확장하려면 트레이드오프가 있다:

- 서버에서 PowerPoint를 무인 자동화하는 건 **마이크로소프트가 공식적으로 지원하지
  않는다**(신뢰성 보장 없음, "Considerations for server-side Automation of Office").
  클라우드 Windows VM+라이선스로 억지로 돌릴 수는 있으나 정식 지원 경로가 아니다.
- 대안은 LibreOffice 헤드리스로 슬라이드 PNG 추출까지는 크로스플랫폼으로 가능하지만,
  **요소 애니메이션은 포기**하고 정지+푸시인(`--static-slides`)으로 후퇴해야 한다.
- 결론: "요소 애니메이션 있는 버전"과 "아무 OS에서나 되는 버전" 중 하나를 포기해야
  한다는 게 핵심 트레이드오프다. 사내 담당자가 각자 Windows PC에서 Claude Code로
  이 스킬을 쓰는 것이 현재로선 애니메이션 품질을 유지하는 유일한 경로.
