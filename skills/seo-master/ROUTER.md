# Router

Match trigger words to parents; then read only the relevant child files (see `REGISTRY.md`). Several parents per request is normal.

| Parent | Triggers |
|---|---|
| 01-core-seo/SKILL.md | seo strategy, seo plan, roadmap, keyword research, search intent, ranking factors, topical authority, competitor analysis |
| 02-google-seo/SKILL.md | google search, search console, gsc, google indexing, core update, discover, serp features, manual action |
| 03-technical-seo/SKILL.md | technical seo, crawl, index, robots, canonical, sitemap, redirect, javascript seo, core web vitals, lcp, inp, cls, page speed, https, mobile, site architecture, seo technical audit |
| 04-on-page-seo/SKILL.md | on-page seo, title tag, meta description, h1, headings, url slug, internal links, content optimization, ctr, entity optimization |
| 05-off-page-seo/SKILL.md | backlinks, link building, digital pr, guest post, brand mentions, citations, link audit, toxic links, disavow |
| 06-content-seo/SKILL.md | content seo, content strategy, topic cluster, pillar page, content gap, seo copywriting, content refresh, content audit, thin content, cannibalization |
| 07-local-seo/SKILL.md | local seo, google business profile, gbp, map pack, nap, citations, reviews, location page, service area |
| 08-ecommerce-seo/SKILL.md | ecommerce seo, product page seo, category page, faceted navigation, product schema, merchant center, out of stock |
| 09-woocommerce-seo/SKILL.md | woocommerce seo, woo product not indexed, shop page, product attributes, variable product, cart noindex |
| 10-shopify-seo/SKILL.md | shopify seo, collection, liquid, shopify canonical, shopify app conflict, robots.txt.liquid |
| 11-wordpress-seo/SKILL.md | wordpress seo, yoast, rank math, permalink, wp plugin conflict, wp theme seo, wp speed |
| 12-saas-seo/SKILL.md | saas seo, landing page, feature page, use case page, integration page, comparison page, alternative page, free tool, docs seo, product-led seo |
| 13-erp-seo/SKILL.md | erp seo, accounting software, inventory software, hr payroll software, crm module, manufacturing software |
| 14-pos-seo/SKILL.md | pos seo, point of sale, restaurant pos, grocery pos, pharmacy pos, retail pos, multi-branch pos, pos hardware |
| 15-programmatic-seo/SKILL.md | programmatic seo, pages at scale, template pages, location pages, database pages, directory |
| 16-image-seo/SKILL.md | image seo, alt text, image filename, webp, avif, image compression, image sitemap, google images |
| 17-video-seo/SKILL.md | video seo, youtube seo, video schema, video sitemap, transcript, thumbnail |
| 18-international-seo/SKILL.md | international seo, hreflang, multilingual, country targeting, translation seo, cctld, subdirectory |
| 19-ai-seo/SKILL.md | ai seo, ai search, ai visibility, ai citations, machine-readable content, ai referral traffic, ai content seo |
| 20-geo/SKILL.md | geo, generative engine optimization, ai overviews, generative search, ai brand visibility, entity authority |
| 21-aeo/SKILL.md | aeo, answer engine optimization, featured snippet, faq, people also ask, voice search, direct answer |
| 22-chatgpt-seo/SKILL.md | chatgpt seo, chatgpt search, chatgpt citations, openai search, chatgpt referral |
| 23-claude-seo/SKILL.md | claude seo, claude visibility, anthropic search |
| 24-gemini-seo/SKILL.md | gemini seo, google ai ecosystem, gemini visibility |
| 25-perplexity-seo/SKILL.md | perplexity seo, perplexity citations |
| 26-ai-agent-seo/SKILL.md | ai agent seo, agentic, llms.txt, webmcp, machine-readable website, agent discoverability |
| 27-schema-seo/SKILL.md | schema, json-ld, structured data, rich results, schema validation |
| 28-seo-analytics/SKILL.md | seo analytics, ga4, search console data, seo reporting, keyword tracking, organic traffic analysis |
| 29-seo-tools-api/SKILL.md | seo tools, ahrefs, semrush, screaming frog, dataforseo, pagespeed api, gsc api, seo scraping |
| 30-seo-audit/SKILL.md | seo audit, site audit, technical audit, on-page audit, backlink audit, ecommerce audit, full audit, seo health check |
| 31-seo-migration/SKILL.md | seo migration, domain change, https migration, replatform, redirect map, relaunch, ranking recovery |
| 32-seo-monitoring/SKILL.md | seo monitoring, rank tracking, traffic drop, indexing monitoring, technical errors, alerts, seo drift |
| 33-seo-automation/SKILL.md | automate seo, automated audit, automated reporting, seo workflow, seo agent, bulk metadata |

## Combos (examples; choose only what evidence supports)

- WooCommerce product not indexed: 09 -> 08 -> 03 (indexability) -> 02 (search-console) -> 27 (product)
- Improve Google ranking: 02 -> 03 -> 04 -> 06 -> 05 if relevant
- Visible in ChatGPT: 19 -> 20 -> 22 -> 27/entity if needed
- Visible in Google + AI search: 02 -> 19 -> 20 -> 21 + needed 03/06/27
- Start SEO for SaaS/ERP/POS: 12/13/14 -> 01 -> 15 -> 04 -> 03 -> 06
- Audit: 30 -> only the modules the site needs (03, 04, 06, 27, 16, 08-11, 19-20)
- Traffic dropped: 32 (traffic) -> 02 -> 03 -> 06
- Platform or domain move: 31 -> 03 -> 32
- Speed: 03 (core-web-vitals) + 11 (WordPress) or 09 (WooCommerce)
