"""타임코드 문자열 ↔ 초 변환 (순수 함수)."""

def parse_tc(tc: str) -> float:
    s = tc.strip()
    if not s:
        raise ValueError("empty timecode")
    parts = s.split(":")
    try:
        nums = [float(p) for p in parts]
    except ValueError as e:
        raise ValueError(f"invalid timecode: {tc!r}") from e
    if any(n < 0 for n in nums):
        raise ValueError(f"negative timecode: {tc!r}")
    if len(nums) == 1:
        total = nums[0]
    elif len(nums) == 2:
        total = nums[0] * 60 + nums[1]
    elif len(nums) == 3:
        total = nums[0] * 3600 + nums[1] * 60 + nums[2]
    else:
        raise ValueError(f"too many parts: {tc!r}")
    return float(total)


def fmt_tc(seconds: float) -> str:
    total = int(round(seconds))
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"
