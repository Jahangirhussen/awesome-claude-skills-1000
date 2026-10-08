"""VO 씬 대본 → Charon TTS WAV (API). tts_gemini.py 설정 재사용."""
import os
import re
import wave
import struct

MODEL = os.environ.get("GEMINI_TTS_MODEL", "gemini-2.5-flash-preview-tts")
SR = 24000
_BEAT = re.compile(r"\[BEAT\s+([0-9.]+)s?\]")


def get_api_key():
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key and os.name == "nt":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as k:
                key, _ = winreg.QueryValueEx(k, "GEMINI_API_KEY")
        except Exception:
            pass
    return key


def _client():
    from google import genai
    key = get_api_key()
    if not key:
        raise SystemExit("GEMINI_API_KEY 환경변수를 설정하세요.")
    return genai.Client(api_key=key)


def _strip_annotations(text: str) -> str:
    # [영상]/⚠[확인] 등 지시문 제거, [BEAT]는 유지(무음 처리)
    text = re.sub(r"[⚠]?\[확인[^\]]*\]", "", text)
    text = re.sub(r"\[영상[^\]]*\]", "", text)
    return text.strip()


def synth_scene(text: str, style: str, voice: str, out_wav: str) -> str:
    from google.genai import types
    client = _client()
    clean = _strip_annotations(text)
    # [BEAT n]를 무음 마커로 분리
    chunks = _BEAT.split(clean)  # [text, secs, text, secs, ...]
    pcm = bytearray()
    for i, part in enumerate(chunks):
        if i % 2 == 1:  # BEAT seconds
            silence = int(float(part) * SR)
            pcm += struct.pack("<%dh" % silence, *([0] * silence))
            continue
        spoken = part.strip()
        if not spoken:
            continue
        resp = client.models.generate_content(
            model=MODEL,
            contents=style + spoken,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice)
                    )
                ),
            ),
        )
        pcm += resp.candidates[0].content.parts[0].inline_data.data
    os.makedirs(os.path.dirname(out_wav), exist_ok=True)
    with wave.open(out_wav, "wb") as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR)
        wf.writeframes(bytes(pcm))
    return out_wav


def revoice_manifest(m, audio_dir: str = "audio") -> dict:
    out = {}
    for sc in m.scenes:
        if sc.type != "VO":
            continue
        wav = os.path.join(audio_dir, f"{sc.id}.wav")
        synth_scene(sc.narration, m.tts_style, m.voice, wav)
        out[sc.id] = wav
        print(f"[revoice] {sc.id} → {wav}")
    return out
