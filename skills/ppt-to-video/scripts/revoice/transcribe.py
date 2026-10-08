"""faster-whisper로 단어 단위 전사 (IO) + 구간 텍스트 추출."""
import json
import os


def transcribe(src: str, out: str = "transcript/base.words.json",
               model_size: str = "large-v3") -> str:
    from faster_whisper import WhisperModel
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if os.path.exists(out):
        print(f"[transcribe] exists, skip: {out}")
        return out
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, _ = model.transcribe(src, language="ko", word_timestamps=True)
    words = []
    for seg in segments:
        for w in (seg.words or []):
            words.append({"start": float(w.start), "end": float(w.end),
                          "word": w.word.strip()})
    with open(out, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=1)
    print(f"[transcribe] {len(words)} words → {out}")
    return out


def text_between(words: list, t0: float, t1: float) -> str:
    return " ".join(w["word"] for w in words if w["start"] >= t0 and w["end"] <= t1).strip()
