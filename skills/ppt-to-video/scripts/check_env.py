# -*- coding: utf-8 -*-
"""ppt-to-video 스킬 환경 점검. 무엇이 빠졌는지만 보고한다 — 설치는 하지 않는다.

사용자 동의 없이 무언가 설치하면 안 되므로, 이 스크립트는 순수 읽기 전용 진단이다.
Claude는 이 스크립트의 출력을 읽고, 빠진 항목이 있으면 사용자에게 설치해도 되는지
물은 뒤 각 항목의 "설치 명령"을 실행한다.

실행: python check_env.py
"""
import os
import shutil
import subprocess
import sys


def _ok(label, detail=""):
    print(f"[OK]      {label}" + (f" — {detail}" if detail else ""))


def _missing(label, fix):
    print(f"[MISSING] {label}")
    print(f"          설치: {fix}")


def check_powerpoint():
    """PPT 요소 애니메이션은 PowerPoint COM 전용 — Windows + 정품 오피스 필수."""
    if os.name != "nt":
        _missing("PowerPoint (Windows COM)",
                 "이 스킬의 PPT 요소 애니메이션 기능은 Windows + 데스크톱 PowerPoint에서만 "
                 "동작합니다. macOS/Linux에서는 --static-slides로 정지+푸시인 방식만 가능.")
        return False
    try:
        r = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command",
             "try { $a = New-Object -ComObject PowerPoint.Application; $a.Quit(); "
             "Write-Output 'OK' } catch { Write-Output 'FAIL' }"],
            capture_output=True, text=True, timeout=30)
        if "OK" in r.stdout:
            _ok("PowerPoint COM")
            return True
    except Exception:
        pass
    _missing("PowerPoint COM", "Microsoft 365 데스크톱 앱(PowerPoint 포함) 설치 필요")
    return False


def check_ffmpeg():
    path = shutil.which("ffmpeg")
    if path:
        _ok("ffmpeg", path)
        return True
    _missing("ffmpeg", "winget install Gyan.FFmpeg  (또는 https://ffmpeg.org/download.html)")
    return False


def check_node():
    """yt-dlp가 유튜브 서명 해독에 Node.js를 쓴다(--js-runtimes node)."""
    path = shutil.which("node")
    if path:
        _ok("Node.js", path)
        return True
    _missing("Node.js", "winget install OpenJS.NodeJS.LTS  (유튜브 인터뷰 클립을 쓸 때만 필요)")
    return False


def check_python_packages():
    pkgs = ["pptx", "google.genai", "faster_whisper", "yt_dlp"]
    pip_names = {"pptx": "python-pptx", "google.genai": "google-genai",
                "faster_whisper": "faster-whisper", "yt_dlp": "yt-dlp"}
    all_ok = True
    for mod in pkgs:
        try:
            __import__(mod)
            _ok(f"python: {pip_names[mod]}")
        except ImportError:
            _missing(f"python: {pip_names[mod]}", f"pip install {pip_names[mod]}")
            all_ok = False
    return all_ok


def check_gemini_key():
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key and os.name == "nt":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as k:
                key, _ = winreg.QueryValueEx(k, "GEMINI_API_KEY")
        except Exception:
            pass
    if key:
        _ok("GEMINI_API_KEY", f"{len(key)}자")
        return True
    _missing("GEMINI_API_KEY",
             "https://aistudio.google.com/apikey 에서 발급 후 "
             "`setx GEMINI_API_KEY <키>` (Windows) 또는 `export GEMINI_API_KEY=<키>`")
    return False


def main():
    print("=== ppt-to-video 환경 점검 ===\n")
    results = {
        "PowerPoint COM (요소 애니메이션, Windows 전용)": check_powerpoint(),
        "ffmpeg (합성·인코딩, 필수)": check_ffmpeg(),
        "Node.js (유튜브 클립 다운로드 시에만 필요)": check_node(),
        "Python 패키지": check_python_packages(),
        "GEMINI_API_KEY (TTS·BGM 생성, 필수)": check_gemini_key(),
    }
    print()
    missing = [k for k, v in results.items() if not v]
    if not missing:
        print("모든 항목 준비 완료 — 바로 사용 가능합니다.")
    else:
        print(f"빠진 항목 {len(missing)}개. 위 '설치' 안내를 따르세요.")
        print("(PowerPoint 없이도 --static-slides로 정지+푸시인 방식은 가능,")
        print(" Node.js 없이도 유튜브 클립 없는 프로젝트는 가능)")
    return 0 if not missing else 1


if __name__ == "__main__":
    sys.exit(main())
