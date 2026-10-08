"""설명회 영상 제작 오케스트레이터.

한 매니페스트로 두 제작 방식을 모두 다룬다:
  - 받은 PPT로 새 영상을 만든다      → SLIDE 씬 위주
  - 기존 설명회 영상을 고쳐 쓴다      → VO/ORIGINAL 씬 위주
둘은 섞을 수 있고, 섞는 게 정상이다(신규 슬라이드 + 기존 인터뷰 원음).

명령:
  python -m revoice.deck  <파일.pptx> [deck]   PPT → 슬라이드 PNG + outline.json
  python -m revoice.build render --dry-run     무엇이 다시 만들어질지만 보기
  python -m revoice.build render               변경분만 재빌드 → 최종 mp4
  python -m revoice.build render --only SC03   그 씬만 다시 만들고 최종 재결합
  python -m revoice.build render --all         캐시 무시하고 전부 재빌드
  python -m revoice.build render --static-slides  SLIDE 씬을 PPT 애니메이션 없이 정지+푸시인으로
  python -m revoice.build render --manifest manifest_client.json   다른 매니페스트로 빌드
  python -m revoice.build trust-audio          기존 나레이션 WAV를 현행으로 인정

여러 매니페스트가 한 프로젝트에 병존할 수 있다(기존 리컷용 manifest.json + 신규 PPT용
manifest_client.json 등). list.txt·베이스 영상·BGM 파일명은 manifest의 output 파일명에서
파생되므로 서로 덮어쓰지 않는다 — 단, output 값을 서로 다르게 지정해야 한다.

증분 빌드가 핵심이다. 검수는 "씬 하나 고쳐줘"의 반복인데, 예전 구조는 그때마다
VO 전체를 TTS 재호출하고 BGM까지 새로 생성해(=영상 전체 배경음악이 바뀜) 한 번에
10분 넘게 걸렸다. 지금은 입력이 바뀐 씬만 다시 만든다.

SLIDE 씬은 기본으로 PPT 자체 애니메이션(요소 순차 페이드인, PowerPoint COM으로 렌더)을
배경으로 쓴다 — 정지 이미지에 밋밋한 푸시인만 얹던 이전 방식 대신, HTML로 다시 그리지
않고도 브랜드 룩 그대로 모션을 얻는다. deck/outline.json이 없거나 --static-slides를
주면 이전 방식(정지+푸시인)으로 대체된다.
"""
import os
import re
import sys
import json
import hashlib
import subprocess

from revoice.manifest import load_manifest
from revoice.timecode import parse_tc
from revoice.timing import reconcile
from revoice import compose, deck, download, transcribe, revoice_tts, lyria_bgm

MANIFEST = "manifest.json"
BUILD = "build"
AUDIO = "audio"
ANIM_DIR = os.path.join("deck", "anim")
CACHE = os.path.join(BUILD, ".cache.json")

_SLIDE_NO_RE = re.compile(r"slide_(\d+)\.png$")

# 캐시는 입력 데이터만 해시하고 렌더링 코드 자체는 보지 않는다 — _render_scene의 조립
# 로직을 바꿀 때마다(이번엔 file= 경로에 리드인 적용 누락을 고침) 이 값을 올려야 예전
# 캐시가 "안 바뀐 것"으로 오판돼 낡은 세그먼트를 계속 재사용하는 사고를 막는다.
_CODEGEN_VERSION = "2"

# 애니메이션 캐시 전용 버전 — 체크포인트 계산 알고리즘(_sentence_checkpoints)이 바뀌면
# narration·duration이 그대로여도 결과가 달라지므로 올려야 한다.
_ANIM_CODEGEN_VERSION = "2"

# 확정되지 않은 수치·문구 표식. 1차 제작 때 "⚠확인"이 붙은 채로 최종 프레임까지
# 흘러가 화면에 그대로 박힌 사고가 있었다. 렌더 전에 차단한다.
GATE_MARKERS = ("[확인", "⚠", "(대본 확인 필요)", "TBD")


def _probe_dur(path: str) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


# ---------------------------------------------------------------- 캐시

def _load_cache() -> dict:
    try:
        with open(CACHE, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _save_cache(c: dict) -> None:
    os.makedirs(BUILD, exist_ok=True)
    with open(CACHE, "w", encoding="utf-8") as f:
        json.dump(c, f, ensure_ascii=False, indent=1)


def _stamp(path: str) -> str:
    """입력 파일의 지문 — 내용 해시 대신 크기+mtime(대용량 영상이라 해싱은 낭비)."""
    try:
        st = os.stat(path)
        return f"{st.st_size}:{int(st.st_mtime)}"
    except OSError:
        return "missing"


def _voice_key(sc, m) -> str:
    """나레이션 음성이 달라지는 입력만 — 대본·스타일·보이스."""
    return hashlib.sha1(
        json.dumps([sc.narration, m.tts_style, m.voice], ensure_ascii=False).encode()
    ).hexdigest()[:16]


def _slide_no(path: str) -> int:
    """`deck/slide_07.png` → 7. 매칭 안 되면 None(=PPT 슬라이드가 아닌 파일)."""
    mo = _SLIDE_NO_RE.search((path or "").replace("\\", "/"))
    return int(mo.group(1)) if mo else None


def _anim_path(slide_no: int) -> str:
    return os.path.join(ANIM_DIR, f"slide_{slide_no:02d}.mp4")


def _scene_key(sc, m, wav: str) -> str:
    """세그먼트 영상이 달라지는 모든 입력."""
    inputs = [sc.file, m.source_file if sc.type in ("VO", "ORIGINAL") else "", wav]
    no = _slide_no(sc.file) if sc.type == "SLIDE" else None
    if no is not None:
        inputs.append(_anim_path(no))
    return hashlib.sha1(json.dumps(
        [_CODEGEN_VERSION, sc.__dict__, [_stamp(p) for p in inputs if p]],
        ensure_ascii=False, sort_keys=True
    ).encode()).hexdigest()[:16]


# ---------------------------------------------------------------- 게이트

def check_gate(m) -> list:
    """미확정 표식이 남은 씬 목록을 돌려준다(비어 있어야 렌더 가능)."""
    hits = []
    for sc in m.scenes:
        for marker in GATE_MARKERS:
            if marker in (sc.narration or "") or marker in (sc.note or ""):
                hits.append(f"{sc.id}: {marker}")
                break
    return hits


# ---------------------------------------------------------------- render

def _narrate(sc, m, cache: dict, force: bool, dry: bool = False) -> str:
    """VO/SLIDE 씬의 나레이션 WAV를 확보 — 대본이 안 바뀌었으면 재호출하지 않는다."""
    wav = os.path.join(AUDIO, f"{sc.id}.wav")
    key = _voice_key(sc, m)
    if not force and os.path.exists(wav) and cache.get(f"voice:{sc.id}") == key:
        return wav
    if dry:
        print(f"[voice] {sc.id} 재합성 예정 (TTS 호출)")
        return wav
    revoice_tts.synth_scene(sc.narration, m.tts_style, m.voice, wav)
    cache[f"voice:{sc.id}"] = key
    print(f"[voice] {sc.id} → {wav}")
    return wav


def _ass_lines(path: str):
    """.ass 자막의 대사 텍스트 목록 — 없으면 None."""
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return [ln.split(",,0,0,0,,", 1)[1].strip()
                for ln in f if ln.startswith("Dialogue:")]


def cmd_trust_audio():
    """캐시 도입 이전에 만든 나레이션 WAV를 재합성 없이 이어 쓴다.

    빈 캐시로 시작하면 대본이 그대로인 씬까지 TTS를 다시 호출해 크레딧을 태운다.
    그렇다고 WAV 존재만 보고 믿으면 대본을 고친 씬에서 낡은 음성이 나가므로,
    옆에 남아 있는 자막(렌더 당시 대본으로 생성됨)을 지금 대본으로 다시 만든 것과
    대조해 실제로 일치하는 씬만 인정한다.
    """
    m = load_manifest(MANIFEST)
    cache = _load_cache()
    ok, stale = [], []
    for sc in m.scenes:
        if sc.type not in ("VO", "SLIDE"):
            continue
        wav = os.path.join(AUDIO, f"{sc.id}.wav")
        was = _ass_lines(os.path.join(BUILD, f"sub_{sc.id}.ass"))
        if not os.path.exists(wav) or was is None:
            stale.append(sc.id)
            continue
        now = _ass_lines(compose.create_scene_srt(
            sc.narration, _probe_dur(wav), os.path.join(BUILD, "_trustcmp.srt"),
            start_offset=compose._LEAD_IN))
        if was == now:
            cache[f"voice:{sc.id}"] = _voice_key(sc, m)
            ok.append(sc.id)
        else:
            stale.append(sc.id)
    tmp = os.path.join(BUILD, "_trustcmp.ass")
    if os.path.exists(tmp):
        os.remove(tmp)
    _save_cache(cache)
    print(f"[trust] 대본 일치 확인 {len(ok)}개 — 재합성 없이 사용: {', '.join(ok) or '없음'}")
    if stale:
        print(f"        재합성 필요 {len(stale)}개: {', '.join(stale)}")


def _composite_video_base(video: str, wav: str, tts_dur: float, srt: str, seg: str,
                          lead_in: float = None) -> None:
    """신규 화면(영상)에 나레이션·자막을 얹는다 — 구 자막이 없으니 마스킹은 안 한다.

    사전 렌더한 슬라이드 애니메이션이든, 다른 곳에서 만든 VO용 영상이든 같은 조립.
    정지 이미지 경로(build_slide_segment_cmd)와 똑같이 리드인만큼 나레이션을 늦춰야
    자막 표시 시점(create_scene_srt의 start_offset)과 실제 발화가 맞물린다 — 리드인 없이
    바로 붙이면 자막이 오디오보다 lead_in초 늦게 뜨는 것처럼 보인다.
    PPT 애니메이션은 요청한 노출 시간(AdvanceTime)대로 만들지만 인코더의 프레임레이트
    반올림으로 근소하게 짧아질 수 있다 — 영상이 먼저 끝나고 오디오만 남는 사고를 막기
    위해 마지막 프레임을 살짝 고정(freeze)해 여유를 둔다.
    """
    lead_in = compose._LEAD_IN if lead_in is None else lead_in
    vf = compose._VNORM + ",tpad=stop_mode=clone:stop_duration=0.6"
    if srt and os.path.exists(srt):
        vf += "," + compose.ass_filter(srt)
    af = compose._ANORM
    if lead_in > 0:
        af += f",adelay={int(lead_in * 1000)}:all=1"
    compose.run_ffmpeg([
        "ffmpeg", "-y", "-i", video, "-i", wav,
        "-vf", vf, "-af", af,
        "-c:v", "libx264", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", compose.FPS,
        "-c:a", "aac", "-ar", "48000", "-ac", "2", "-t", f"{tts_dur + lead_in:.3f}", seg])


def _render_scene(sc, m, wav: str, seg: str) -> None:
    if sc.type in ("ORIGINAL", "EXTERNAL", "CLIP"):
        src = sc.file if sc.type in ("EXTERNAL", "CLIP") else m.source_file
        compose.run_ffmpeg(compose.build_original_segment_cmd(
            src, sc.src_in or "0:00", sc.src_out or "0:30", seg))
        return

    tts_dur = _probe_dur(wav)
    srt = compose.create_scene_srt(sc.narration, tts_dur,
                                   os.path.join(BUILD, f"sub_{sc.id}.srt"),
                                   start_offset=compose._LEAD_IN)

    if sc.type == "SLIDE":
        no = _slide_no(sc.file)
        anim = _anim_path(no) if no is not None else None
        if anim and os.path.exists(anim):
            _composite_video_base(anim, wav, tts_dur, srt, seg)
        else:
            # PPT 요소 애니메이션을 못 만들었을 때의 대체 — 정지 이미지 + 느린 푸시인.
            compose.run_ffmpeg(compose.build_slide_segment_cmd(
                sc.file, wav, tts_dur, seg, srt_file=srt))
        return

    # VO: file이 지정되면 그 영상을 화면으로 쓰고, 없으면 원본 설명회 영상 구간을 쓴다.
    if sc.file:
        _composite_video_base(sc.file, wav, tts_dur, srt, seg)
        return

    plan = reconcile(parse_tc(sc.src_out) - parse_tc(sc.src_in), tts_dur)
    compose.run_ffmpeg(compose.build_vo_segment_cmd(
        m.source_file, sc.src_in, sc.src_out, wav, plan, seg,
        srt_file=srt, is_new_slide=False))


def _sentence_checkpoints(narration: str, words: list, total_dur: float) -> list:
    """나레이션을 문장 단위로 나누고, 각 문장이 실제로 다 말해지는 시각을 돌려준다.

    문자열 매칭이 아니라 '단어 개수' 비율로 위치를 찾는다 — TTS가 원문을 그대로
    읽어도 whisper 전사 철자(숫자 표기·붙여쓰기 등)는 원문과 달라지기 쉬워 문자열
    매칭은 깨지기 쉽지만, 단어 개수 비율은 안정적이다. 이 체크포인트가 PPT 요소
    애니메이션의 등장 타이밍이 된다 — "화면 요소가 전부 처음 2초 안에 뜨고 나머지
    구간은 정적"이던 문제를, 나레이터가 그 대목을 말하는 시점에 맞춰 등장하게 바꾼다.
    """
    parts = [s.strip() for s in re.split(r'(?<=[.?!])\s+|(?<=—)\s+', narration.replace("\n", " "))
             if s.strip()]
    if not parts:
        return [total_dur]
    word_counts = [max(1, len(p.split())) for p in parts]
    total_words_script = sum(word_counts)
    total_words_audio = len(words)
    if total_words_audio == 0 or abs(total_words_audio - total_words_script) / total_words_script > 0.4:
        # whisper 전사가 원문과 단어 수부터 크게 어긋나면(오인식 등) 위치 추정을
        # 신뢰할 수 없다 — 균등 분배로 폴백. 그래도 "전부 처음 2초"보다는 낫다.
        n = len(parts)
        return [total_dur * (i + 1) / n for i in range(n)]
    cum = 0
    checkpoints = []
    for wc in word_counts:
        cum += wc
        idx = max(0, min(int(round(cum / total_words_script * total_words_audio)),
                        total_words_audio) - 1)
        checkpoints.append(words[idx]["end"])
    checkpoints[-1] = total_dur    # 마지막 체크포인트는 항상 씬 전체 길이로 고정
    return checkpoints


def _narration_words(sc, wav: str) -> list:
    """씬 나레이션 WAV를 전사해 단어 타임스탬프를 얻는다 — 대본이 바뀌면 다시 전사."""
    words_path = os.path.join(AUDIO, f"{sc.id}.words.json")
    key = hashlib.sha1(_stamp(wav).encode()).hexdigest()[:12]
    stamp_path = words_path + ".stamp"
    if os.path.exists(words_path) and os.path.exists(stamp_path):
        with open(stamp_path, encoding="utf-8") as f:
            if f.read().strip() == key:
                with open(words_path, encoding="utf-8") as wf:
                    return json.load(wf)
        os.remove(words_path)
    transcribe.transcribe(wav, out=words_path)
    with open(stamp_path, "w", encoding="utf-8") as f:
        f.write(key)
    with open(words_path, encoding="utf-8") as f:
        return json.load(f)


def _ensure_slide_animations(m, wavs: dict, cache: dict, only, rebuild_all: bool,
                             dry: bool, use_anim: bool) -> None:
    """대상 SLIDE 씬들의 요소 애니메이션 mp4를 한 PowerPoint 세션에서 일괄 생성.

    슬라이드마다 따로 호출하면 PowerPoint를 그만큼 열고 닫아 느리다 — 이번 빌드에서
    새로 필요한 슬라이드를 모아 한 번에 넘긴다(revoice/deck.py의 Hidden 토글 방식).
    각 슬라이드의 등장 타이밍은 그 씬 나레이션을 실제로 전사(whisper)해 문장별로
    체크포인트를 계산해 넘긴다 — 균등 배분이 아니라 나레이션 진행에 맞춘 등장.
    """
    if not use_anim:
        return
    outline_path = os.path.join("deck", "outline.json")
    if not os.path.exists(outline_path):
        return
    with open(outline_path, encoding="utf-8") as f:
        pptx = json.load(f).get("source_pptx")
    if not pptx or not os.path.exists(pptx):
        return

    todo = {}          # slide_no -> {duration, checkpoints}
    for sc in m.scenes:
        if sc.type != "SLIDE":
            continue
        no = _slide_no(sc.file)
        if no is None:
            continue
        targeted = only is None or sc.id in only
        if not targeted:
            continue
        wav = wavs.get(sc.id, "")
        if not wav or not os.path.exists(wav):
            continue
        dur = _probe_dur(wav) + compose._LEAD_IN
        key = hashlib.sha1(json.dumps(
            [_ANIM_CODEGEN_VERSION, _stamp(pptx), no, round(dur, 1), sc.narration],
            ensure_ascii=False).encode()
        ).hexdigest()[:16]
        anim = _anim_path(no)
        if rebuild_all or not os.path.exists(anim) or cache.get(f"anim:{no}") != key:
            todo[no] = {"dur": dur, "key": key, "sc": sc, "wav": wav}

    if not todo:
        return
    if dry:
        for no in sorted(todo):
            print(f"[anim]  slide_{no:02d} 애니메이션 재렌더 예정 ({todo[no]['dur']:.1f}s)")
        return

    print(f"[anim]  {len(todo)}개 슬라이드 애니메이션 렌더 중 (전사 + PowerPoint COM)...")
    payload = {}
    for no, t in todo.items():
        words = _narration_words(t["sc"], t["wav"])
        # 리드인(정적) 만큼 체크포인트를 뒤로 밀어 — 애니메이션은 씬 전체(리드인+발화) 기준.
        raw_dur = t["dur"] - compose._LEAD_IN
        checkpoints = [compose._LEAD_IN + c for c in
                      _sentence_checkpoints(t["sc"].narration, words, raw_dur)]
        payload[no] = {"duration": t["dur"], "checkpoints": checkpoints}

    rendered = deck.render_animated_slides(pptx, payload, out_dir=ANIM_DIR)
    for no, t in todo.items():
        if no in rendered:
            cache[f"anim:{no}"] = t["key"]
            print(f"[anim]  slide_{no:02d} → {rendered[no]}")
    _save_cache(cache)


def cmd_render(only=None, rebuild_all=False, force_gate=False, new_bgm=False, dry=False,
               use_anim=True, manifest_path=None):
    m = load_manifest(manifest_path or MANIFEST)
    os.makedirs(BUILD, exist_ok=True)
    # 프로젝트에 매니페스트가 여러 개 병존할 수 있다(예: 기존 리컷용 manifest.json과
    # 신규 PPT용 manifest_client.json) — 중간 산출물 이름을 output 파일명에서 파생시켜
    # 서로 다른 매니페스트의 빌드가 list.txt·베이스 영상·BGM을 덮어쓰지 않게 한다.
    prefix = os.path.splitext(os.path.basename(m.output))[0]

    gate = check_gate(m)
    if gate and not force_gate:
        print("[gate] 미확정 표식이 남아 있어 렌더를 중단합니다 "
              "(그대로 렌더하면 화면에 박힙니다):")
        for g in gate:
            print(f"        - {g}")
        print("       확정 후 다시 실행하거나, 의도한 것이면 --force 를 붙이세요.")
        raise SystemExit(2)

    cache = _load_cache()

    # 1단계: 나레이션 WAV 확보 (SLIDE 애니메이션 길이를 정하려면 TTS 길이를 먼저 알아야 함).
    wavs = {}
    for sc in m.scenes:
        if sc.type in ("VO", "SLIDE"):
            targeted = only is None or sc.id in only
            wavs[sc.id] = _narrate(sc, m, cache, force=rebuild_all and targeted, dry=dry)

    # 2단계: 그 길이에 맞춰 SLIDE 씬의 PPT 요소 애니메이션을 한 세션에서 일괄 렌더.
    _ensure_slide_animations(m, wavs, cache, only, rebuild_all, dry, use_anim)

    # 3단계: 씬별 최종 세그먼트 합성(신규/변경분만).
    seg_paths, rebuilt = [], 0

    for sc in m.scenes:
        seg = os.path.join(BUILD, f"seg_{sc.id}.mp4")
        seg_paths.append(seg)
        targeted = only is None or sc.id in only
        wav = wavs.get(sc.id, "")

        key = _scene_key(sc, m, wav)
        if not targeted or (not rebuild_all and os.path.exists(seg)
                            and cache.get(f"seg:{sc.id}") == key):
            print(f"[skip]  {sc.id}")
            continue

        if dry:
            print(f"[seg]   {sc.id} 재렌더 예정 ({sc.type})")
            rebuilt += 1
            continue

        _render_scene(sc, m, wav, seg)
        cache[f"seg:{sc.id}"] = key
        _save_cache(cache)      # 씬마다 저장 — 중간에 끊겨도 앞부분은 재활용된다
        rebuilt += 1
        print(f"[seg]   {sc.id} → {seg}")

    if dry:
        print(f"[dry]   재빌드 대상 {rebuilt}개 씬 — 실제로 만들려면 --dry-run 을 빼세요.")
        return

    missing = [p for p in seg_paths if not os.path.exists(p)]
    if missing:
        raise SystemExit(f"세그먼트 누락: {missing} — --all 로 전체 빌드하세요.")

    list_file = os.path.join(BUILD, f"{prefix}_list.txt")
    with open(list_file, "w", encoding="utf-8") as f:
        for p in seg_paths:
            f.write(f"file '{os.path.basename(p)}'\n")

    base = os.path.join(BUILD, f"{prefix}_base.mp4")
    compose.run_ffmpeg(compose.build_concat_cmd(list_file, base))

    # BGM은 매 빌드마다 새로 생성하면 씬 하나만 고쳐도 영상 전체의 배경음악이
    # 달라진다. 이미 만든 트랙이 있으면 그대로 쓴다.
    bgm = os.path.join("bgm", f"{prefix}.wav")
    if new_bgm or not os.path.exists(bgm):
        bgm = lyria_bgm.generate_bgm(m.bgm.get("prompt", "warm ambient"), out=bgm, seconds=90)
    else:
        print(f"[bgm]   기존 트랙 재사용 → {bgm} (바꾸려면 --new-bgm)")

    compose.run_ffmpeg(compose.build_bgm_duck_cmd(base, bgm, m.output))
    print(f"[done]  {rebuilt}개 씬 재빌드 · 최종 → {m.output}")


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    cmd = argv[0] if argv else ""
    if cmd == "trust-audio":
        cmd_trust_audio()
    elif cmd == "render":
        only = None
        if "--only" in argv:
            only = set(argv[argv.index("--only") + 1].split(","))
        manifest_path = None
        if "--manifest" in argv:
            manifest_path = argv[argv.index("--manifest") + 1]
        cmd_render(only=only, rebuild_all="--all" in argv,
                   force_gate="--force" in argv, new_bgm="--new-bgm" in argv,
                   dry="--dry-run" in argv, use_anim="--static-slides" not in argv,
                   manifest_path=manifest_path)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
