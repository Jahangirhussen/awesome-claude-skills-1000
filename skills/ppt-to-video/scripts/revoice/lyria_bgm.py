"""Lyria RealTime BGM 생성 (API) + 절차적 폴백."""
import os
import wave
import asyncio
import subprocess
from revoice.revoice_tts import get_api_key

LYRIA_MODEL = "models/lyria-realtime-exp"
SR = 48000


def _fallback(out: str, seconds: int) -> str:
    # 기존 방식과 유사한 따뜻한 앰비언트(사인 코드) — ffmpeg 절차 생성
    os.makedirs(os.path.dirname(out), exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i",
                    f"sine=f=220:r=48000:d={seconds}",
                    "-af", "tremolo=f=0.2:d=0.4,lowpass=f=1200,aecho=0.8:0.7:60:0.3,volume=0.3",
                    "-ac", "2", out], check=True)
    print(f"[bgm] fallback ambient → {out}")
    return out


async def _lyria(prompt: str, out: str, seconds: int) -> str:
    from google import genai
    from google.genai import types
    key = get_api_key()
    if not key:
        raise RuntimeError("no GEMINI_API_KEY")
    client = genai.Client(api_key=key, http_options={"api_version": "v1alpha"})
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pcm = bytearray()
    target = SR * 2 * 2 * seconds  # 48k * 2ch * 16bit

    async with client.aio.live.music.connect(model=LYRIA_MODEL) as session:
        await session.set_weighted_prompts(
            prompts=[types.WeightedPrompt(text=prompt, weight=1.0)])
        await session.set_music_generation_config(
            config=types.LiveMusicGenerationConfig(bpm=90, density=0.4, brightness=0.6))
        await session.play()
        async for msg in session.receive():
            chunk = getattr(getattr(msg, "server_content", None), "audio_chunks", None)
            if chunk:
                pcm += chunk[0].data
            if len(pcm) >= target:
                break
    with wave.open(out, "wb") as wf:
        wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR)
        wf.writeframes(bytes(pcm[:target]))
    print(f"[bgm] lyria → {out} ({len(pcm)//(SR*4)}s)")
    return out


def generate_bgm(prompt: str, out: str = "bgm/bgm.wav", seconds: int = 90) -> str:
    try:
        return asyncio.run(_lyria(prompt, out, seconds))
    except Exception as e:
        print(f"[bgm] lyria failed ({e}); falling back")
        return _fallback(out, seconds)
