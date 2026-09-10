---
name: arcads-meta-ad-builder
description: Deploy finished video/image creatives as live Meta (Facebook/Instagram) ads via Marketing API. Use when user says "deploy to Meta", "publish Facebook ad", "create Facebook campaign", "run this as an ad".
---

# Meta Ad Builder

Deploy creatives as Meta ads via the Marketing API.

## Setup Required

Add to `.env`:
```
META_ACCESS_TOKEN=your_token
META_AD_ACCOUNT_ID=act_xxxxxxxxx
```

## Three Phases

### Phase 1 — Research (optional)
- Pull top-performing ads ranked by ROAS
- Pull competitor ads from Ad Library
- Informs copy strategy

### Phase 2 — Copy Writing
Write variants:
- 5 body copy options
- 5 headline options
- 3 description options
Mirror patterns from Phase 1 winning ads.

### Phase 3 — Deploy

**ALWAYS dry-run first:**
```bash
python deploy_ad.py --dry-run
```
Review payload, then execute live:
```bash
python deploy_ad.py --live
```

## Critical Rules

- Ads deploy in **PAUSED** status always
- NEVER add `--active` flag or unpause without explicit user instruction
- Video uploads are async — may take several minutes
- Requires existing ad set (does NOT create campaigns)
- Dry-run before EVERY real deployment

## Trigger Phrases

- "deploy this to Meta"
- "publish as a Facebook ad"
- "pull my top ads"
- "research competitor ads"
- "run this ad on Instagram"

## Out of Scope

- Generating creative assets → use arcads-video or arcads-image-ad
- Creating campaigns from scratch → user must provide ad set ID
