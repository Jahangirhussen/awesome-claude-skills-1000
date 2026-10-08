# ppt-to-video

*Read this in: **English** | [한국어](README.ko.md)*

A Claude Code Skill that turns a PowerPoint deck into a narrated video with
real PowerPoint element animation — or re-cuts/re-voices an existing
presentation-style video — without ever re-drawing slides in HTML.

## Why this exists

The common approach to "make a video from a PPT" is to re-render the deck as
HTML/CSS and animate that. In practice this drifts from the brand's actual
look (fonts, photos, exact layout) and looks like a generic template.

This tool instead drives **PowerPoint itself** via COM automation:

- Slides are exported to PNG using PowerPoint's own renderer — pixel-identical
  to the original file, no re-authoring.
- Element entrance animation (fade-in, sequenced) is added through
  PowerPoint's native `Slide.TimeLine` animation engine and rendered to MP4
  via `Presentation.CreateVideo()` — the same engine a human editor would use
  in PowerPoint, not a reimplementation.
- Narration audio is synthesized (Gemini TTS) and then **transcribed back**
  with faster-whisper to get real word-level timestamps, which drive when
  each slide element appears — so elements land in sync with what's actually
  being said, not a fixed generic timing.
- ffmpeg composites everything: slide animation, narration, background music
  (ducked under the voice), and any interview/B-roll clips.

Only works reliably on Windows with a licensed desktop PowerPoint install
(PowerPoint COM automation isn't officially supported server-side by
Microsoft) — see `references/pipeline.md` for the tradeoffs if you want to
run this elsewhere.

## Install

Clone into your Claude Code skills directory:

```bash
git clone https://github.com/olymplan427-rgb/ppt-to-video.git ~/.claude/skills/ppt-to-video
```

Then, from any project where you want to build a video:

```bash
python ~/.claude/skills/ppt-to-video/scripts/check_env.py
```

This only *checks* your environment (PowerPoint, ffmpeg, Node.js, Python
packages, `GEMINI_API_KEY`) — it never installs anything itself. Fix
whatever it flags as missing, following the printed instructions.

Copy `scripts/revoice/` into your project (it's called as
`python -m revoice.<module>` from the project root):

```bash
cp -r ~/.claude/skills/ppt-to-video/scripts/revoice ./revoice
```

## Usage

See [SKILL.md](SKILL.md) for the workflow Claude follows, and
[references/pipeline.md](references/pipeline.md) for the full manifest
schema, animation internals, and known limitations. (Note: this repo's
deeper docs and code comments are written in Korean — only this README
is bilingual for now.)

Quick loop once you have a manifest:

```bash
python -m revoice.build render --manifest manifest.json --dry-run   # preview, no API calls
python -m revoice.build render --manifest manifest.json             # build changed scenes
python -m revoice.build render --manifest manifest.json --only P03  # rebuild one scene
```

## Tests

```bash
cd scripts && python -m pytest tests -q
```

## License

MIT — see [LICENSE](LICENSE).
