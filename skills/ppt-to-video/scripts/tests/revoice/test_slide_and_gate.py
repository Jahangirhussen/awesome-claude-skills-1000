"""신규 제작 방식(SLIDE 씬)·확인 게이트·증분 캐시 키에 대한 검증."""
import os
import pytest

from revoice.manifest import Scene, Manifest, validate_manifest
from revoice import compose, build


def _m(scenes):
    return Manifest(source="X", source_file="source/x.mp4", voice="Charon",
                    tts_style="차분: ", output="build/out.mp4",
                    bgm={"engine": "lyria-realtime-exp", "duck": True}, scenes=scenes)


# ------------------------------------------------- SLIDE 씬 유효성

def test_slide_scene_needs_no_timecode():
    """SLIDE는 길이를 나레이션이 정하므로 src_in/src_out 없이도 유효해야 한다."""
    validate_manifest(_m([
        Scene(id="S01", type="SLIDE", file="deck/slide_01.png", narration="안녕하세요"),
    ]))


def test_slide_scene_requires_file():
    with pytest.raises(ValueError, match="requires file"):
        validate_manifest(_m([Scene(id="S01", type="SLIDE", narration="안녕하세요")]))


def test_slide_scene_requires_narration():
    with pytest.raises(ValueError, match="requires narration"):
        validate_manifest(_m([Scene(id="S01", type="SLIDE", file="deck/slide_01.png")]))


def test_clip_scene_requires_file_and_window():
    validate_manifest(_m([
        Scene(id="C01", type="CLIP", file="clips/a.mp4", src_in="0:02", src_out="0:18"),
    ]))
    with pytest.raises(ValueError, match="requires file"):
        validate_manifest(_m([Scene(id="C01", type="CLIP", src_in="0:02", src_out="0:18")]))


# ------------------------------------------------- SLIDE 합성 명령

def test_slide_cmd_duration_is_narration_plus_lead_in():
    cmd = compose.build_slide_segment_cmd("deck/slide_01.png", "audio/S01.wav", 12.0,
                                          "build/seg_S01.mp4")
    total = 12.0 + compose._LEAD_IN
    assert cmd[cmd.index("-t") + 1] == f"{total:.3f}"
    assert "-loop" in cmd                      # 정지 이미지를 영상 길이만큼 늘린다


def test_slide_cmd_pushes_in_and_skips_old_subtitle_mask():
    """정지 화면이 죽지 않게 푸시인을 넣되, 신규 화면이라 구 자막 마스킹은 없어야 한다."""
    cmd = compose.build_slide_segment_cmd("deck/slide_01.png", "audio/S01.wav", 12.0,
                                          "build/seg_S01.mp4")
    fc = cmd[cmd.index("-filter_complex") + 1]
    assert "zoompan" in fc
    assert "drawbox" not in fc


# ------------------------------------------------- 확인 게이트

def test_gate_blocks_unconfirmed_markers():
    """⚠확인이 붙은 대본이 그대로 렌더돼 화면에 박힌 사고의 재발 방지."""
    m = _m([
        Scene(id="S01", type="SLIDE", file="a.png", narration="매년 3억 장학투자 ⚠[확인]"),
        Scene(id="S02", type="SLIDE", file="b.png", narration="캠퍼스 133개"),
    ])
    hits = build.check_gate(m)
    assert [h.split(":")[0] for h in hits] == ["S01"]


def test_gate_passes_when_all_confirmed():
    assert build.check_gate(_m([
        Scene(id="S01", type="SLIDE", file="a.png", narration="캠퍼스 133개"),
    ])) == []


# ------------------------------------------------- 증분 캐시 키

def test_voice_key_changes_only_with_narration_style_or_voice():
    base = Scene(id="S01", type="SLIDE", file="a.png", narration="원본 대본")
    m = _m([base])
    k = build._voice_key(base, m)

    same_text = Scene(id="S01", type="SLIDE", file="b.png", narration="원본 대본")
    assert build._voice_key(same_text, m) == k, "화면만 바뀌면 TTS를 다시 부르지 않는다"

    edited = Scene(id="S01", type="SLIDE", file="a.png", narration="고친 대본")
    assert build._voice_key(edited, m) != k, "대본이 바뀌면 반드시 다시 합성한다"


def test_scene_key_changes_when_visual_source_changes():
    m = _m([])
    a = Scene(id="S01", type="SLIDE", file="deck/slide_01.png", narration="대본")
    b = Scene(id="S01", type="SLIDE", file="deck/slide_02.png", narration="대본")
    assert build._scene_key(a, m, "") != build._scene_key(b, m, "")


# ------------------------------------------------- PPT 요소 애니메이션 배경

def test_slide_no_parses_deck_filename():
    assert build._slide_no("deck/slide_07.png") == 7
    assert build._slide_no("deck\\slide_23.png") == 23


def test_slide_no_none_for_non_deck_file():
    """CLIP처럼 deck 슬라이드가 아닌 파일은 애니메이션 배경 후보가 아니다."""
    assert build._slide_no("clips/interview_a.mp4") is None
    assert build._slide_no("") is None


def test_anim_path_is_two_digit_padded():
    assert build._anim_path(7) == os.path.join("deck", "anim", "slide_07.mp4")
    assert build._anim_path(23) == os.path.join("deck", "anim", "slide_23.mp4")


def test_scene_key_includes_animation_background_for_slide_type(tmp_path, monkeypatch):
    """SLIDE 씬은 정지 PNG가 그대로여도, 사전 렌더한 애니메이션 mp4가 바뀌면 재세그해야 한다."""
    monkeypatch.chdir(tmp_path)
    os.makedirs(os.path.join("deck", "anim"))
    anim = build._anim_path(2)
    with open(anim, "wb") as f:
        f.write(b"v1")

    m = _m([])
    sc = Scene(id="S02", type="SLIDE", file="deck/slide_02.png", narration="대본")
    key_before = build._scene_key(sc, m, "")

    with open(anim, "wb") as f:
        f.write(b"v2-different-size")
    key_after = build._scene_key(sc, m, "")

    assert key_before != key_after


def test_composite_video_base_applies_lead_in_delay_and_duration(monkeypatch):
    """file= 기반 화면(사전 렌더 애니메이션 등)도 정지 이미지 경로와 같은 리드인 규칙을 따라야
    한다 — 빠뜨리면 자막이 create_scene_srt의 start_offset만큼 오디오보다 늦게 뜬다."""
    captured = {}
    monkeypatch.setattr(compose, "run_ffmpeg", lambda args: captured.setdefault("args", args))

    build._composite_video_base("deck/anim/slide_02.mp4", "audio/S02.wav", 10.0, None, "out.mp4")

    args = captured["args"]
    total = 10.0 + compose._LEAD_IN
    assert args[args.index("-t") + 1] == f"{total:.3f}"
    af = args[args.index("-af") + 1]
    assert f"adelay={int(compose._LEAD_IN * 1000)}" in af
