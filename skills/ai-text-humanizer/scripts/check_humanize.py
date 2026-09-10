#!/usr/bin/env python3
"""Flag AI-sounding text patterns: banned words, uniform rhythm, forced triads, punctuation overuse."""
import sys
import re
import statistics

BANNED_WORDS = [
    "delve", "pivotal", "crucial", "robust", "vibrant", "meticulous",
    "enduring", "showcase", "foster", "garner", "bolster", "landscape",
    "tapestry", "testament", "underscore", "serves as", "boasts",
]

BANNED_PHRASES = [
    "not only", "not just", "plays a vital role", "in today's world",
    "it is important to note", "stands as a testament",
]


def load_text(arg: str) -> str:
    try:
        with open(arg, "r", encoding="utf-8") as f:
            return f.read()
    except (FileNotFoundError, OSError):
        return arg


def split_sentences(text: str):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p]


def check(text: str):
    issues = []
    lower = text.lower()

    for w in BANNED_WORDS:
        count = lower.count(w)
        if count:
            issues.append(f"banned word '{w}' used {count}x")

    for p in BANNED_PHRASES:
        if p in lower:
            issues.append(f"banned phrase '{p}' found")

    sentences = split_sentences(text)
    lengths = [len(s.split()) for s in sentences if s.split()]
    if len(lengths) >= 4:
        stdev = statistics.pstdev(lengths)
        mean = statistics.mean(lengths)
        if stdev < mean * 0.25:
            issues.append(
                f"sentence lengths too uniform (mean={mean:.1f}, stdev={stdev:.1f}) — vary rhythm"
            )

    em_dash = text.count("—") + text.count("--")
    if em_dash > max(1, len(sentences) // 8):
        issues.append(f"em dash overuse ({em_dash} occurrences)")

    colons = text.count(":")
    if colons > max(1, len(sentences) // 6):
        issues.append(f"colon overuse ({colons} occurrences)")

    bullets = len(re.findall(r"^\s*[-*•]\s", text, re.MULTILINE))
    if bullets > 5:
        issues.append(f"heavy bullet use ({bullets} lines) — consider prose")

    triads = re.findall(r"\b(\w+), (\w+),? and (\w+)\b", text)
    if len(triads) >= 2:
        issues.append(f"forced groups-of-three pattern found ({len(triads)}x)")

    exclam = text.count("!")
    if exclam > 1:
        issues.append(f"exclamation marks overused ({exclam})")

    return issues


def main():
    if len(sys.argv) < 2:
        print("usage: check_humanize.py <file_path_or_text>")
        sys.exit(1)

    text = load_text(sys.argv[1])
    issues = check(text)

    if not issues:
        print("OK: no obvious AI-pattern issues found")
        return

    print(f"FLAGGED: {len(issues)} issue(s)")
    for i in issues:
        print(f"- {i}")
    sys.exit(1)


if __name__ == "__main__":
    main()
