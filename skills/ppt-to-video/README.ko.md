# ppt-to-video

*다른 언어로 보기: [English](README.md) | **한국어***

PowerPoint 슬라이드를 **PPT 요소 애니메이션이 살아있는 나레이션 영상**으로 만드는
Claude Code Skill이다. 기존 영상을 씬 단위로 리컷·리보이스하는 것도 같은 파이프라인
안에서 처리한다. 슬라이드는 절대 HTML로 다시 그리지 않는다.

## 왜 이렇게 만들었나

"PPT로 영상 만들기"의 흔한 방법은 슬라이드를 HTML/CSS로 재현해서 그 위에 애니메이션을
얹는 것이다. 실제로 해보면 브랜드의 실제 룩(폰트·사진·정확한 레이아웃)에서 벗어나
흔한 템플릿처럼 보이게 된다.

이 도구는 대신 **PowerPoint 자체**를 COM 자동화로 구동한다:

- 슬라이드는 PowerPoint 자체 렌더러로 PNG로 내보낸다 — 원본 파일과 픽셀 단위로
  동일하며, 다시 그리는 과정이 없다.
- 요소 등장 애니메이션(순차 페이드인)은 PowerPoint의 네이티브 `Slide.TimeLine`
  애니메이션 엔진으로 넣고 `Presentation.CreateVideo()`로 mp4로 뽑는다 — 사람이
  PowerPoint에서 직접 쓰는 것과 같은 엔진이지, 재구현한 게 아니다.
- 나레이션 음성은 합성(Gemini TTS) 후 **faster-whisper로 다시 전사**해 실제 단어
  단위 타임스탬프를 얻고, 이 타임스탬프가 슬라이드 요소가 등장하는 시점을 정한다 —
  고정된 일반 타이밍이 아니라 실제로 말하는 내용과 맞물려 등장한다.
- ffmpeg가 슬라이드 애니메이션·나레이션·배경음악(음성 아래로 더킹)·인터뷰/B롤
  클립을 전부 합성한다.

Windows + 정품 데스크톱 PowerPoint에서만 안정적으로 동작한다(PowerPoint COM
자동화는 마이크로소프트가 서버 환경에서 공식적으로 지원하지 않음) — 다른 환경에서
쓰고 싶다면 트레이드오프는 `references/pipeline.md`(영문) 참고.

## 설치

Claude Code 스킬 디렉터리에 클론한다:

```bash
git clone https://github.com/olymplan427-rgb/ppt-to-video.git ~/.claude/skills/ppt-to-video
```

그리고 영상을 만들 프로젝트에서:

```bash
python ~/.claude/skills/ppt-to-video/scripts/check_env.py
```

이건 환경을 **점검만** 한다(PowerPoint·ffmpeg·Node.js·Python 패키지·
`GEMINI_API_KEY`) — 스스로 아무것도 설치하지 않는다. 빠진 게 있으면 출력된 안내를
따라 직접 설치한다.

`scripts/revoice/`를 프로젝트에 복사한다(프로젝트 루트에서
`python -m revoice.<모듈>`로 호출하는 구조):

```bash
cp -r ~/.claude/skills/ppt-to-video/scripts/revoice ./revoice
```

## 사용법

Claude가 따르는 워크플로우는 [SKILL.md](SKILL.md)를, 매니페스트 스키마 전체·
애니메이션 내부 동작·알려진 제약은 [references/pipeline.md](references/pipeline.md)
를 참고한다(둘 다 본문은 원래 한글로 작성돼 있음 — 지금 이 두 README만 한/영 병기).

매니페스트가 있다면 기본 루프는:

```bash
python -m revoice.build render --manifest manifest.json --dry-run   # API 호출 없이 미리보기
python -m revoice.build render --manifest manifest.json             # 변경된 씬만 재빌드
python -m revoice.build render --manifest manifest.json --only P03  # 씬 하나만 재빌드
```

## 테스트

```bash
cd scripts && python -m pytest tests -q
```

## 라이선스

MIT — [LICENSE](LICENSE) 참고.
