"""VO 씬 타이밍 재조정 (순수). 스펙 §5 구체화."""
from dataclasses import dataclass


@dataclass
class ReconcilePlan:
    scene_dur: float
    video_setpts: float | None
    video_freeze: float
    audio_pad: float


def reconcile(src_dur: float, tts_dur: float, max_stretch: float = 0.08) -> ReconcilePlan:
    if src_dur <= 0 or tts_dur <= 0:
        raise ValueError("durations must be positive")
    if tts_dur <= src_dur:
        # 오디오가 짧음: 영상 전체 유지, 오디오 뒤 무음 패딩
        return ReconcilePlan(scene_dur=src_dur, video_setpts=None,
                             video_freeze=0.0, audio_pad=src_dur - tts_dur)
    # 오디오가 김: 최대 +max_stretch까지 영상 슬로우다운
    ideal = tts_dur / src_dur                 # >1
    f = min(ideal, 1.0 + max_stretch)         # setpts 배수 (<=1.08)
    after = src_dur * f
    freeze = max(0.0, tts_dur - after)
    setpts = None if abs(f - 1.0) < 1e-9 else f
    return ReconcilePlan(scene_dur=tts_dur, video_setpts=setpts,
                         video_freeze=freeze, audio_pad=0.0)
