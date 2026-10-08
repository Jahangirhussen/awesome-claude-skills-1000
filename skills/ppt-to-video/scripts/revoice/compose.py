"""ffmpeg 명령 빌더(순수) + 기존 자막 마스킹 + 신규 자막 합성 헬퍼."""
import os
import re
import subprocess
from revoice.timecode import parse_tc
from revoice.timing import ReconcilePlan

W, H, FPS = "1920", "1080", "30"
_VNORM = f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={FPS}"
_ANORM = "aresample=48000,aformat=sample_rates=48000:channel_layouts=stereo"

# 원본 영상(source/base.mp4)의 구 자막은 인터뷰 구간(노트 박스)과 VO 대체 구간(타이틀카드/브롤)의
# 스타일이 다르다. VO씬이 실제로 대체하는 구간의 구 자막은 심플한 화이트 박스(또는 무배경)+
# 검정 굵은 텍스트로, 실측 결과 y≈963~1038에 고정 배치됨(여러 씬 샘플링으로 확인).
# 화면 전체 폭을 덮을 필요는 없으므로 폭 1600px(중앙 정렬)·높이 110px로 축소해
# 구 자막을 가리되 화면 하단을 불필요하게 넓게 덮지 않는다. 새 자막 박스와 같은
# 아이보리 톤으로 채워 아래 ASS 자동 박스와 이어져 보이도록 한다.
_BAR_W = 1600
_BAR_X = (1920 - _BAR_W) // 2
_BAR_Y = 930
_BAR_H = 110
_MASK_BOX = f"drawbox=x={_BAR_X}:y={_BAR_Y}:w={_BAR_W}:h={_BAR_H}:color=0xF5F1E8@1.0:t=fill"

# 신규 나레이션 자막: SRT+force_style은 subtitles 필터가 내부적으로 임의의 PlayRes로
# 스케일링하면서 줄바꿈·위치가 어긋나는 문제가 있어(1920x1080 명시해도 재현됨),
# PlayResX/Y를 직접 못박은 .ass로 렌더링해 좌표계 모호성을 제거한다.
# WrapStyle=2(자동 줄바꿈 금지)로 두 줄로 밀리는 문제도 원천 차단 — 대신 청크를
# max_chars 이하로 미리 쪼개 한 줄에 들어가도록 보장한다.
# BorderStyle=3(불투명 박스)으로 텍스트 길이에 맞춰 배경 박스가 자동으로 좁아지거나
# 넓어지게 해, 화면 하단 전체를 덮는 고정폭 바 대신 실제 텍스트만큼만 덮도록 한다.
# 원본 영상(구 자막)의 톤(아이보리 박스+짙은 텍스트)에 맞춰 색을 지정했다.
# 텍스트는 순검정 대신 브랜드 그레이 팔레트의 가장 짙은 톤(#464646)으로 톤다운.
# 폰트는 브랜드 폰트 Wanted Sans ExtraBold(시스템 미설치라 _FONTS_DIR로 런타임 로드, 아래 참고).
_ASS_HEADER = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Wanted Sans ExtraBold,56,&H00464646,&H000000FF,&H00E8F1F5,&H00E8F1F5,0,0,0,0,100,100,0,0,3,20,0,2,80,80,70,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

# Wanted Sans는 시스템에 설치돼 있지 않아(브랜드 폰트, 프로젝트 assets에만 존재),
# ffmpeg의 ass 필터에 fontsdir로 직접 지정해 설치 없이 렌더링에 사용한다.
_FONTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "fonts").replace("\\", "/")


def ass_filter(srt_file: str) -> str:
    """ffmpeg 필터 문자열용 ass= 절.

    필터 인자 안에서 경로의 콜론은 옵션 구분자로 먹히므로 이스케이프해야 한다.
    fontsdir는 미설치 브랜드 폰트(Wanted Sans)를 설치 없이 로드하기 위한 것.
    """
    path = srt_file.replace("\\", "/").replace(":", r"\:")
    fonts = _FONTS_DIR.replace(":", r"\:")
    return f"ass='{path}':fontsdir='{fonts}'"


def _fmt_ass_tc(sec: float) -> str:
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = int(sec % 60)
    cs = int(round((sec - int(sec)) * 100))
    if cs >= 100:
        s += 1
        cs -= 100
    return f"{h:d}:{m:02d}:{s:02d}.{cs:02d}"


def _pack_words(part: str, max_chars: int) -> list:
    """공백 경계에서 max_chars 이하로 욕심쟁이 재분할(절 경계가 없을 때의 최종 폴백)."""
    words = part.split(' ')
    chunks, cur = [], ''
    for w in words:
        cand = f"{cur} {w}".strip()
        if cur and len(cand) > max_chars:
            chunks.append(cur)
            cur = w
        else:
            cur = cand
    if cur:
        chunks.append(cur)
    return chunks


def _split_long(part: str, max_chars: int) -> list:
    """max_chars를 넘는 구문을 쉼표(자연스러운 끊어읽기 지점) 경계로 우선 분할하고,
    그래도 한 절이 너무 길면 공백 경계로 재분할한다.

    쉼표 없이 공백 경계로만 자르면 "...운영하는 법, PTR과..."처럼 절 중간에서
    잘려 부자연스러운 자막이 나오는 문제가 있었다(사용자 피드백 2026-07-27).
    """
    if len(part) <= max_chars:
        return [part]

    # 절 하나가 max_chars를 살짝 넘는 정도(=합리적인 끊어읽기 단위)까지는
    # 억지로 쪼개지 않고 한 줄로 허용한다.
    hard_cap = int(max_chars * 1.4)

    clauses = [c.strip() for c in re.split(r'(?<=,)\s+', part) if c.strip()]
    if len(clauses) <= 1:
        return _pack_words(part, max_chars)

    chunks, cur = [], ''
    for c in clauses:
        cand = f"{cur} {c}".strip()
        if cur and len(cand) > max_chars:
            chunks.append(cur)
            cur = c
        else:
            cur = cand
    if cur:
        chunks.append(cur)

    refined = []
    for ch in chunks:
        if len(ch) <= hard_cap:
            refined.append(ch)
        else:
            refined.extend(_pack_words(ch, max_chars))
    return refined


_LEAD_IN = 0.5  # 씬 시작부터 나레이션이 시작되기까지의 정지 여백(초).


def create_scene_srt(narration: str, total_dur: float, srt_path: str, max_chars: int = 28,
                      start_offset: float = 0.0) -> str:
    """나레이션 문장을 구문 단위로 분할해 타임코드 .ass 자막 파일 생성(반환 경로는 .ass).

    한 줄에 안전하게 들어가도록 max_chars(기본 28자)를 넘는 구문은
    공백 경계에서 추가로 쪼갠다. WrapStyle=2라 자동 줄바꿈이 없으므로
    이 사전 분할이 곧 실제 표시 줄 단위가 된다. total_dur은 실제 발화 구간
    길이(리드인 제외)이고, start_offset만큼 모든 타임코드를 뒤로 민다 —
    리드인 동안에는 자막이 뜨지 않고 발화 시작과 정확히 맞물리게 하기 위함.
    """
    if not narration or not narration.strip():
        return None

    # 문장 및 구문 분할 (. ? ! — 기준). "—"는 나레이션 대본에서 TTS 호흡 지점을
    # 표시하는 연출 기호(분할 기준)일 뿐 화면에 보일 내용이 아니므로, 분할에는
    # 쓰되 표시 텍스트에서는 제거한다.
    raw_parts = [p.strip() for p in re.split(r'(?<=[.?!])\s+|(?<=—)\s+', narration) if p.strip()]
    parts = [q for q in (re.sub(r'—\s*$', '', p).strip() for p in raw_parts) if q]
    if not parts:
        parts = [narration.strip()]

    refined = []
    for p in parts:
        refined.extend(_split_long(p, max_chars))
    parts = refined

    # 각 구문 글자수 비율에 맞게 시간 분배
    char_counts = [max(1, len(p)) for p in parts]
    total_chars = sum(char_counts)

    events = []
    t_curr = 0.0
    for idx, text in enumerate(parts, 1):
        dur = total_dur * (char_counts[idx - 1] / total_chars)
        t_start = t_curr
        t_end = min(total_dur, t_curr + dur)
        t_curr = t_end
        safe_text = text.replace("{", "(").replace("}", ")")
        events.append(
            f"Dialogue: 0,{_fmt_ass_tc(t_start + start_offset)},{_fmt_ass_tc(t_end + start_offset)},"
            f"Default,,0,0,0,,{safe_text}")

    ass_path = os.path.splitext(srt_path)[0] + ".ass"
    os.makedirs(os.path.dirname(ass_path), exist_ok=True)
    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(_ASS_HEADER + "\n".join(events) + "\n")
    return ass_path


def _window(src_in: str, src_out: str) -> tuple[str, str]:
    a, b = parse_tc(src_in), parse_tc(src_out)
    def fmt(x):
        return str(int(x)) if float(x).is_integer() else f"{x:.3f}"
    return fmt(a), fmt(b - a)


def build_vo_segment_cmd(src, src_in, src_out, wav, plan: ReconcilePlan, out, srt_file: str = None, is_new_slide: bool = False,
                          lead_in: float = _LEAD_IN) -> list:
    ss, dur = _window(src_in, src_out)
    vfilters = [_VNORM]

    # 원본 비디오 기반 씬일 경우 기존 자막을 100% 가리는 마스킹 박스 필터 적용
    if not is_new_slide:
        vfilters.append(_MASK_BOX)

    if plan.video_setpts is not None:
        vfilters.append(f"setpts={plan.video_setpts:.4f}*PTS")
    if plan.video_freeze > 0:
        vfilters.append(f"tpad=stop_mode=clone:stop_duration={plan.video_freeze:.3f}")
    if lead_in > 0:
        # 씬 시작~나레이션 시작 사이 정지 여백 — 첫 프레임을 lead_in초만큼 유지
        vfilters.append(f"tpad=start_mode=clone:start_duration={lead_in:.3f}")

    if srt_file and os.path.exists(srt_file):
        vfilters.append(ass_filter(srt_file))

    vchain = ",".join(vfilters)

    afilters = [_ANORM]
    if plan.audio_pad > 0:
        afilters.append(f"apad=pad_dur={plan.audio_pad:.3f}")
    if lead_in > 0:
        afilters.append(f"adelay={int(lead_in * 1000)}:all=1")
    achain = ",".join(afilters)

    return [
        "ffmpeg", "-y",
        "-ss", ss, "-t", dur, "-i", src,   # 0: source video window
        "-i", wav,                          # 1: new narration audio only
        "-filter_complex",
        f"[0:v]{vchain}[v];[1:a]{achain}[a]",
        "-map", "[v]", "-map", "[a]",
        "-t", f"{plan.scene_dur + lead_in:.3f}",
        "-c:v", "libx264", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", FPS,
        "-c:a", "aac", "-ar", "48000", "-ac", "2",
        out,
    ]


_CUT_FADE = 0.25  # 원본 구간 앞뒤로 붙이는 짧은 페이드 — 하드컷의 어색함 제거용.


def build_original_segment_cmd(src, src_in, src_out, out, fade: float = _CUT_FADE) -> list:
    """원본 영상 구간을 그대로 잘라 쓴다(CLIP·ORIGINAL·EXTERNAL).

    유튜브 인터뷰처럼 임의 지점에서 잘라온 구간은 시작·끝이 하드컷으로 뚝 끊기면
    어색하다 — 앞뒤로 짧은 페이드를 걸어 자연스러운 인·아웃을 만든다.
    """
    ss, dur_s = _window(src_in, src_out)
    dur = parse_tc(src_out) - parse_tc(src_in)
    fade = min(fade, dur / 2 - 0.01) if dur > 0.1 else 0
    vf = _VNORM
    af = _ANORM
    if fade > 0:
        vf += f",fade=t=in:st=0:d={fade:.3f},fade=t=out:st={dur - fade:.3f}:d={fade:.3f}"
        af += f",afade=t=in:st=0:d={fade:.3f},afade=t=out:st={dur - fade:.3f}:d={fade:.3f}"
    return [
        "ffmpeg", "-y",
        "-ss", ss, "-t", dur_s, "-i", src,
        "-vf", vf,
        "-af", af,
        "-c:v", "libx264", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", FPS,
        "-c:a", "aac", "-ar", "48000", "-ac", "2",
        out,
    ]


def build_concat_cmd(list_file, out) -> list:
    return [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file,
        "-c", "copy", out,
    ]


def build_bgm_duck_cmd(base, bgm, out, bgm_gain_db: float = -18.0) -> list:
    fc = (
        f"[1:a]volume={bgm_gain_db}dB,aresample=48000[bg];"
        f"[bg][0:a]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=300[duck];"
        f"[0:a][duck]amix=inputs=2:duration=first:normalize=0[a]"
    )
    return [
        "ffmpeg", "-y",
        "-i", base,                          # 0: video + narration/interview audio
        "-stream_loop", "-1", "-i", bgm,     # 1: BGM
        "-filter_complex", fc,
        "-map", "0:v", "-map", "[a]",
        "-c:v", "copy", "-c:a", "aac", "-ar", "48000", "-ac", "2",
        "-shortest", out,
    ]


def run_ffmpeg(args: list) -> None:
    subprocess.run(args, check=True)


def build_slide_segment_cmd(png, wav, dur: float, out, srt_file: str = None,
                            zoom: float = 0.06, lead_in: float = _LEAD_IN) -> list:
    """PPT 슬라이드 PNG + 새 나레이션 → 한 씬.

    정지 이미지를 그대로 40~90초 물리면 '슬라이드쇼'로 보이므로(1차 시도의 실패
    지점), 아주 느린 푸시인을 넣어 영상의 호흡을 만든다. zoom은 전체 구간에 걸친
    확대 비율(기본 6%) — 눈에 띄는 효과가 아니라 화면이 죽지 않을 정도만.
    슬라이드는 신규 화면이라 구 자막 마스킹(_MASK_BOX)은 쓰지 않는다.
    """
    total = dur + lead_in
    frames = max(1, int(round(total * float(FPS))))
    # zoompan은 확대 시 크롭 중심이 흔들리기 쉬워, 미리 2배로 키운 뒤 확대하고
    # 중심(iw/2-(iw/zoom/2))을 고정해 부드럽게 밀어 넣는다.
    vfilters = [
        f"scale={int(W)*2}:-2",
        f"zoompan=z='1+{zoom}*on/{frames}':d={frames}:s={W}x{H}"
        f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':fps={FPS}",
        "setsar=1",
    ]
    if srt_file and os.path.exists(srt_file):
        vfilters.append(ass_filter(srt_file))
    vchain = ",".join(vfilters)

    afilters = [_ANORM]
    if lead_in > 0:
        afilters.append(f"adelay={int(lead_in * 1000)}:all=1")
    achain = ",".join(afilters)

    return [
        "ffmpeg", "-y",
        "-loop", "1", "-i", png,
        "-i", wav,
        "-filter_complex", f"[0:v]{vchain}[v];[1:a]{achain}[a]",
        "-map", "[v]", "-map", "[a]",
        "-t", f"{total:.3f}",
        "-c:v", "libx264", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", FPS,
        "-c:a", "aac", "-ar", "48000", "-ac", "2",
        out,
    ]
