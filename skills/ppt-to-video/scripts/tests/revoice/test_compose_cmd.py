from revoice.timing import ReconcilePlan
from revoice.compose import (
    build_vo_segment_cmd, build_original_segment_cmd,
    build_concat_cmd, build_bgm_duck_cmd,
)

def _joined(cmd):
    return " ".join(cmd)

def test_vo_segment_trims_source_range():
    plan = ReconcilePlan(scene_dur=20.0, video_setpts=None, video_freeze=0.0, audio_pad=4.0)
    cmd = build_vo_segment_cmd("source/base.mp4", "0:06", "0:32",
                               "audio/SC01.wav", plan, "build/seg_SC01.mp4")
    s = _joined(cmd)
    assert cmd[0] == "ffmpeg"
    assert "-ss" in cmd and "6" in cmd            # 0:06 → 6s
    assert "-t" in cmd and "26" in cmd            # 0:32-0:06 = 26s source window
    assert "audio/SC01.wav" in s                  # new voice audio
    assert "apad" in s                            # audio_pad>0 → apad
    assert "libx264" in s and "aac" in s
    assert "1920" in s and "1080" in s            # normalized to output spec

def test_vo_segment_slowdown_and_freeze():
    plan = ReconcilePlan(scene_dur=30.0, video_setpts=1.08, video_freeze=8.4, audio_pad=0.0)
    cmd = build_vo_segment_cmd("source/base.mp4", "0:40", "1:02",
                               "audio/SC02.wav", plan, "build/seg_SC02.mp4")
    s = _joined(cmd)
    assert "setpts=1.0800*PTS" in s
    assert "tpad=stop_mode=clone" in s            # freeze last frame
    assert "apad" not in s                        # no audio pad when audio drives

def test_original_segment_keeps_audio():
    cmd = build_original_segment_cmd("source/base.mp4", "3:15", "3:52", "build/seg_SC07.mp4")
    s = _joined(cmd)
    assert "-ss" in cmd and "195" in cmd          # 3:15 = 195s
    assert "-t" in cmd and "37" in cmd            # 3:52-3:15 = 37s
    assert "libx264" in s and "aac" in s
    assert "apad" not in s and "setpts" not in s  # original untouched (only normalize)


def test_original_segment_fades_in_and_out():
    """하드컷으로 시작·끝나면 어색하다 — 짧은 페이드가 기본으로 들어가야 한다."""
    cmd = build_original_segment_cmd("clip.mp4", "0:00", "0:20", "build/seg_C.mp4")
    vf = cmd[cmd.index("-vf") + 1]
    af = cmd[cmd.index("-af") + 1]
    assert "fade=t=in:st=0:d=0.250" in vf
    assert "fade=t=out:st=19.750:d=0.250" in vf
    assert "afade=t=in:st=0:d=0.250" in af
    assert "afade=t=out:st=19.750:d=0.250" in af


def test_original_segment_fade_shrinks_for_very_short_clips():
    """0.5초짜리 구간에서 기본 0.25초 페이드 두 번을 걸면 서로 겹친다 — 자동으로 줄어야 한다."""
    cmd = build_original_segment_cmd("clip.mp4", "0:00", "0:00.4", "build/seg_C.mp4")
    vf = cmd[cmd.index("-vf") + 1]
    assert "fade=t=in:st=0:d=0.190" in vf  # 0.4/2 - 0.01 = 0.19, 기본값 0.25보다 작음

def test_concat_cmd():
    cmd = build_concat_cmd("build/list.txt", "build/revoice_base.mp4")
    s = _joined(cmd)
    assert "concat" in s and "build/list.txt" in s and "build/revoice_base.mp4" in s

def test_bgm_duck_uses_sidechaincompress():
    cmd = build_bgm_duck_cmd("build/revoice_base.mp4", "bgm/bgm.wav", "build/revoice_final.mp4")
    s = _joined(cmd)
    assert "sidechaincompress" in s
    assert "bgm/bgm.wav" in s
    assert "build/revoice_final.mp4" in s
