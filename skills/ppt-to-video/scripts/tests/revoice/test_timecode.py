import pytest
from revoice.timecode import parse_tc, fmt_tc

def test_parse_mmss():
    assert parse_tc("4:58") == 298.0

def test_parse_hhmmss():
    assert parse_tc("1:02:03") == 3723.0

def test_parse_seconds_only():
    assert parse_tc("12") == 12.0

def test_parse_strips_whitespace():
    assert parse_tc(" 0:06 ") == 6.0

def test_parse_rejects_garbage():
    with pytest.raises(ValueError):
        parse_tc("abc")

def test_fmt_mmss():
    assert fmt_tc(298.0) == "4:58"

def test_fmt_hhmmss():
    assert fmt_tc(3723.0) == "1:02:03"

def test_roundtrip():
    for tc in ["0:06", "4:58", "10:07"]:
        assert fmt_tc(parse_tc(tc)) == tc
