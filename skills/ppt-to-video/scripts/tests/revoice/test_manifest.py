import json
import pytest
from revoice.manifest import Scene, Manifest, load_manifest, save_manifest, validate_manifest

def _m(scenes):
    return Manifest(source="X", source_file="source/x.mp4", voice="Charon",
                    tts_style="차분: ", output="build/out.mp4",
                    bgm={"engine": "lyria-realtime-exp", "duck": True}, scenes=scenes)

def test_validate_ok():
    validate_manifest(_m([
        Scene(id="SC01", src_in="0:06", src_out="0:32", type="VO", narration="안녕하세요"),
        Scene(id="SC07", src_in="3:15", src_out="3:52", type="ORIGINAL", note="인터뷰"),
    ]))  # no raise

def test_validate_duplicate_id():
    with pytest.raises(ValueError, match="duplicate"):
        validate_manifest(_m([
            Scene(id="SC01", src_in="0:06", src_out="0:32", type="VO", narration="a"),
            Scene(id="SC01", src_in="0:40", src_out="1:02", type="VO", narration="b"),
        ]))

def test_validate_bad_type():
    with pytest.raises(ValueError, match="type"):
        validate_manifest(_m([Scene(id="SC01", src_in="0:06", src_out="0:32", type="XX")]))

def test_validate_vo_requires_narration():
    with pytest.raises(ValueError, match="narration"):
        validate_manifest(_m([Scene(id="SC01", src_in="0:06", src_out="0:32", type="VO")]))

def test_validate_in_before_out():
    with pytest.raises(ValueError, match="src_in"):
        validate_manifest(_m([Scene(id="SC01", src_in="0:32", src_out="0:06", type="VO", narration="a")]))

def test_save_load_roundtrip(tmp_path):
    m = _m([Scene(id="SC01", src_in="0:06", src_out="0:32", type="VO",
                  narration="안녕", flags=["verify-offer"])])
    p = tmp_path / "manifest.json"
    save_manifest(m, str(p))
    data = json.loads(p.read_text(encoding="utf-8"))
    assert data["scenes"][0]["narration"] == "안녕"
    m2 = load_manifest(str(p))
    assert m2.scenes[0].id == "SC01"
    assert m2.scenes[0].flags == ["verify-offer"]
    assert m2.voice == "Charon"
