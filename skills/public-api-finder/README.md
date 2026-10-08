# public-api-finder

Claude Code skill: search, compare, and recommend public/free APIs from a local knowledge base built off the official [Public APIs repository](https://github.com/public-apis/public-apis).

## Contents

- `SKILL.md` — instructions for Claude on how to use this knowledge base.
- `references/INDEX.md` — category index with API counts and links.
- `references/<Category>.md` — one file per category, each a table of every API in that category (API, Description, Auth, HTTPS, CORS, Documentation link).

## Source

Data is parsed directly from the category tables (`### <Category>` sections) in the upstream repo's `README.md`. No entries are invented, reworded, or omitted; missing source fields are marked `—`.

Snapshot stats: 51 categories, 1802 APIs, generated 2026-09-14.

## How Claude uses this

See `SKILL.md`. In short: start at `INDEX.md`, open the relevant category file(s), filter by name/description/auth/HTTPS/CORS, return matches as a table with a short recommendation.

## Updating

Re-fetch `https://raw.githubusercontent.com/public-apis/public-apis/master/README.md` and regenerate all files from source — don't hand-edit `references/*.md`.

## Data integrity rules

- Every API appears exactly once, in its source category.
- No invented auth/HTTPS/CORS/pricing/rate-limit values.
- `—` means the source had no value for that field.

## Limitations

- Snapshot in time — the upstream repo updates continuously; re-generate for guaranteed-current data.
- No pricing, rate-limit, or live-status data (not present in the source tables) — verify against the API's own docs when that matters.
