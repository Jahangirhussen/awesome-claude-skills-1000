"""yt-dlp로 베이스 영상 다운로드 (IO)."""
import os
import subprocess


def download_source(video_id: str, out: str = "source/base.mp4") -> str:
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if os.path.exists(out):
        print(f"[download] exists, skip: {out}")
        return out
    url = f"https://www.youtube.com/watch?v={video_id}"
    cmd = [
        "python", "-m", "yt_dlp",
        "-f", "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b",
        "--merge-output-format", "mp4",
        "-o", out, url,
    ]
    print("[download]", " ".join(cmd))
    subprocess.run(cmd, check=True)
    return out
