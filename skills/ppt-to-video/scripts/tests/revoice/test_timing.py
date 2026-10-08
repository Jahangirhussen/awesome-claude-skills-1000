import pytest
from revoice.timing import reconcile, ReconcilePlan

def test_audio_shorter_keeps_full_video_and_pads_audio():
    p = reconcile(src_dur=20.0, tts_dur=16.0)
    assert p.scene_dur == 20.0
    assert p.video_setpts is None
    assert p.video_freeze == 0.0
    assert p.audio_pad == pytest.approx(4.0)

def test_audio_equal_no_changes():
    p = reconcile(src_dur=20.0, tts_dur=20.0)
    assert p.scene_dur == 20.0
    assert p.video_setpts is None
    assert p.video_freeze == 0.0
    assert p.audio_pad == 0.0

def test_audio_slightly_longer_absorbed_by_slowdown():
    # 21 vs 20 → 5% slowdown, within 8% cap → setpts=1.05, no freeze
    p = reconcile(src_dur=20.0, tts_dur=21.0)
    assert p.scene_dur == 21.0
    assert p.video_setpts == pytest.approx(1.05, abs=1e-4)
    assert p.video_freeze == pytest.approx(0.0, abs=1e-6)
    assert p.audio_pad == 0.0

def test_audio_much_longer_caps_slowdown_then_freezes():
    # 30 vs 20 → need 1.5x but cap 1.08 → video=21.6, freeze=8.4
    p = reconcile(src_dur=20.0, tts_dur=30.0)
    assert p.scene_dur == 30.0
    assert p.video_setpts == pytest.approx(1.08, abs=1e-4)
    assert p.video_freeze == pytest.approx(8.4, abs=1e-3)
    assert p.audio_pad == 0.0
