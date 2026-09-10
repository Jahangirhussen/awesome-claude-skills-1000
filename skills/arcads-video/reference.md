# Arcads External API — Full Reference

## Authentication

HTTP Basic Auth — API key as username, empty password:
```
Authorization: Basic base64(API_KEY:)
```

## Unified Video Endpoint

```
POST /v2/videos/generate
```

Supports: Sora 2, Sora 2 Pro, Veo 3.1, Kling 2.6, Kling 3.0, Grok Video, Seedance 2.0

## Critical Implementation Notes

**Seedance 2.0 polling difference:**
- Generated via `/v2/videos/generate`
- Returns `type: "seedance_20"`
- Poll at `GET /v1/assets/{id}` — NOT `/v1/videos/{id}`
- Check response `type` field to determine polling path

**Mutually exclusive on Seedance:**
- Image-to-video (`referenceImages`) and video-to-video (`referenceVideos`) cannot coexist
- Combining both causes HTTP 500

**Image input support:**
- Veo, Sora, Grok — currently REJECT image inputs (500 error)
- Workaround: use Kling 3.0 (`startFrame`) or Seedance 2.0 (`referenceImages` + `audioEnabled: false`)

**Presigned URLs are single-use:**
- Re-upload file each time to get fresh path

## Image Generation Endpoint

```
POST /v2/images/generate
```

Models: `gpt-image-2`, `nano-banana-2`, `nano-banana-pro`, `nano-banana-edit`

Supported ratios: `1:1`, `16:9`, `9:16` ONLY

## Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| 401/403 | Auth failure | Check API key |
| 422 | Validation / content moderation | Rewrite prompt |
| 500 | Server error | Retry carefully (Seedance charges on creation) |

## Pricing (per second estimates)

| Model | Cost/sec |
|-------|----------|
| Grok Video | ~0.027¢ |
| Seedance img2vid | ~0.06¢ |
| Sora 2 | ~0.08¢ |
| Kling 3.0 | ~0.09¢ |
| Seedance vid2vid | ~0.10¢ |
| Veo 3.1 | ~0.125¢ |

Always present pricing as ESTIMATES. Direct users to Arcads dashboard for final pricing.
