"""씬/매니페스트 모델과 로드·검증·저장 (순수)."""
import json
from dataclasses import dataclass, field, asdict
from revoice.timecode import parse_tc

# 씬 타입 — 두 제작 방식(신규 PPT 기반 / 기존 영상 리컷)을 별도 파이프라인이 아니라
# 하나의 매니페스트 안 '배합'으로 다룬다. 그래야 둘을 섞을 수 있고, 기존 영상의
# 특정 대목만 새 슬라이드로 갈아끼우는 작업도 같은 엔진으로 처리된다.
#   SLIDE    : 받은 PPT의 슬라이드 PNG + 새 나레이션          (신규 제작 주력)
#   VO       : 기존 설명회 영상 구간 + 새 나레이션 + 자막 마스킹 (기존 리컷 주력)
#   ORIGINAL : 기존 설명회 영상 구간, 원음 유지                (원장·학생 발화)
#   CLIP     : 별도 영상 파일 구간, 원음 유지                  (인터뷰 증언 삽입)
#   EXTERNAL : intro/outro 범퍼
VALID_TYPES = {"SLIDE", "VO", "ORIGINAL", "EXTERNAL", "CLIP"}

# 화면을 원본 영상 타임라인에서 잘라오는 타입 — src_in/src_out이 필수다.
# SLIDE는 길이가 나레이션 TTS 길이로 정해지므로 여기 속하지 않는다.
WINDOWED_TYPES = {"VO", "ORIGINAL", "CLIP", "EXTERNAL"}

# 화면을 외부 파일에서 가져오는 타입 — file이 필수다.
FILE_TYPES = {"SLIDE", "CLIP", "EXTERNAL"}


@dataclass
class Scene:
    id: str
    type: str
    src_in: str = ""      # SLIDE 씬은 길이를 나레이션이 정하므로 비워둔다
    src_out: str = ""
    layout: str = "as-is"
    narration: str = ""
    note: str = ""
    file: str = ""
    flags: list = field(default_factory=list)


@dataclass
class Manifest:
    source: str
    source_file: str
    voice: str
    tts_style: str
    output: str
    bgm: dict
    scenes: list


def validate_manifest(m: Manifest) -> None:
    seen = set()
    for sc in m.scenes:
        if sc.id in seen:
            raise ValueError(f"duplicate scene id: {sc.id}")
        seen.add(sc.id)
        if sc.type not in VALID_TYPES:
            raise ValueError(f"bad type {sc.type!r} in {sc.id} "
                             f"(must be one of {'|'.join(sorted(VALID_TYPES))})")
        if sc.type in FILE_TYPES and not sc.file:
            raise ValueError(f"{sc.type} scene {sc.id} requires file attribute")
        if sc.type in ("VO", "SLIDE") and not sc.narration.strip():
            raise ValueError(f"{sc.type} scene {sc.id} requires narration")
        if sc.type in WINDOWED_TYPES and parse_tc(sc.src_in) >= parse_tc(sc.src_out):
            raise ValueError(f"src_in must precede src_out in {sc.id}")


def load_manifest(path: str) -> Manifest:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    scenes = [Scene(**s) for s in data.pop("scenes")]
    m = Manifest(scenes=scenes, **data)
    validate_manifest(m)
    return m


def save_manifest(m: Manifest, path: str) -> None:
    data = asdict(m)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
