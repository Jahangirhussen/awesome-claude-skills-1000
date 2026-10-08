# Registry

Canonical skills. Every child/grandchild `SKILL.md` also holds its Use when / Not when / Checks / Dependencies. Add a skill: create its folder + `SKILL.md`, add a row here.

| ID | Skill | Level | Parent | Merged-from | Dependencies | Triggers | Path | Status |
|---|---|---|---|---|---|---|---|---|
| 01 | Core SEO | parent | SEO Master | seo-specialist |  | seo strategy, seo plan, roadmap, keyword research, search intent, ranking factors, topical authority, competitor analysis | 01-core-seo/SKILL.md | active |
| 01.01 | Keyword research | child | Core SEO | seo-keyword, seo-keyword-gap-audit |  | keyword research, keyword clustering, keyword mapping, intent, keyword gap | 01-core-seo/keyword-research/SKILL.md | active |
| 01.02 | SEO strategy and roadmap | child | Core SEO | seo-specialist |  | seo strategy, seo plan, roadmap, kpis, prioritization | 01-core-seo/seo-strategy/SKILL.md | active |
| 01.03 | Competitor SEO analysis | child | Core SEO | seo-competitor |  | competitor, serp overlap, competitive seo, content gap vs competitor | 01-core-seo/competitor-analysis/SKILL.md | active |
| 02 | Google SEO | parent | SEO Master |  |  | google search, search console, gsc, google indexing, core update, discover, serp features, manual action | 02-google-seo/SKILL.md | active |
| 02.01 | Search Console | child | Google SEO |  | 28-seo-analytics/search-console | gsc, search console, performance report, url inspection, page indexing, manual action | 02-google-seo/search-console/SKILL.md | active |
| 02.02 | Google indexing | child | Google SEO |  | 03-technical-seo/indexability | not indexed, crawled currently not indexed, discovered not indexed, index coverage | 02-google-seo/indexing/SKILL.md | active |
| 02.03 | Core updates and volatility | child | Google SEO |  | 32-seo-monitoring/traffic | core update, algorithm update, ranking drop, helpful content | 02-google-seo/core-updates/SKILL.md | active |
| 03 | Technical SEO | parent | SEO Master | seo-technical |  | technical seo, crawl, index, robots, canonical, sitemap, redirect, javascript seo, core web vitals, lcp, inp, cls, page speed, https, mobile, site architecture, seo technical audit | 03-technical-seo/SKILL.md | active |
| 03.01 | Crawlability | child | Technical SEO |  |  | crawl budget, crawl depth, crawl errors, blocked, googlebot | 03-technical-seo/crawlability/SKILL.md | active |
| 03.02 | Indexability | child | Technical SEO |  |  | noindex, index bloat, orphan page, duplicate url, thin page | 03-technical-seo/indexability/SKILL.md | active |
| 03.03 | Canonicals | child | Technical SEO |  |  | canonical, duplicate content, rel canonical | 03-technical-seo/canonical/SKILL.md | active |
| 03.04 | robots.txt | child | Technical SEO |  |  | robots.txt, disallow, blocked resources | 03-technical-seo/robots/SKILL.md | active |
| 03.05 | XML sitemaps | child | Technical SEO |  |  | sitemap, xml sitemap, image sitemap, video sitemap, sitemap index | 03-technical-seo/sitemap/SKILL.md | active |
| 03.06 | Redirects and status codes | child | Technical SEO |  |  | 301, 302, redirect chain, 404, soft 404, status code | 03-technical-seo/redirects/SKILL.md | active |
| 03.07 | JavaScript and rendering SEO | child | Technical SEO |  |  | javascript seo, rendering, ssr, csr, hydration, spa | 03-technical-seo/javascript-seo/SKILL.md | active |
| 03.08 | Core Web Vitals and speed | child | Technical SEO |  | 16-image-seo | core web vitals, lcp, inp, cls, pagespeed, lighthouse, slow site, ttfb, cdn, caching | 03-technical-seo/core-web-vitals/SKILL.md | active |
| 03.08.1 | LCP | grandchild | Core Web Vitals and speed |  |  | lcp, largest contentful paint | 03-technical-seo/core-web-vitals/lcp/SKILL.md | active |
| 03.08.2 | INP | grandchild | Core Web Vitals and speed |  |  | inp, interaction to next paint, responsiveness | 03-technical-seo/core-web-vitals/inp/SKILL.md | active |
| 03.08.3 | CLS | grandchild | Core Web Vitals and speed |  |  | cls, layout shift | 03-technical-seo/core-web-vitals/cls/SKILL.md | active |
| 03.09 | Mobile SEO | child | Technical SEO |  |  | mobile friendly, responsive, mobile first indexing | 03-technical-seo/mobile-seo/SKILL.md | active |
| 03.10 | HTTPS and security headers | child | Technical SEO |  |  | https, ssl, mixed content, hsts, security headers | 03-technical-seo/https/SKILL.md | active |
| 03.11 | Website architecture | child | Technical SEO |  | site-architecture (installed skill) | site structure, url hierarchy, navigation, silo, breadcrumbs, information architecture | 03-technical-seo/website-architecture/SKILL.md | active |
| 04 | On-Page SEO | parent | SEO Master | seo-onpage |  | on-page seo, title tag, meta description, h1, headings, url slug, internal links, content optimization, ctr, entity optimization | 04-on-page-seo/SKILL.md | active |
| 04.01 | Title tags | child | On-Page SEO |  |  | title tag, seo title | 04-on-page-seo/title-tags/SKILL.md | active |
| 04.02 | Meta descriptions | child | On-Page SEO |  |  | meta description, snippet | 04-on-page-seo/meta-descriptions/SKILL.md | active |
| 04.03 | Headings | child | On-Page SEO |  |  | h1, h2, heading structure | 04-on-page-seo/headings/SKILL.md | active |
| 04.04 | URL optimization | child | On-Page SEO |  |  | url, slug, permalink | 04-on-page-seo/url-optimization/SKILL.md | active |
| 04.05 | Internal linking | child | On-Page SEO |  | internal-link-builder (installed skill) | internal links, anchor text, orphan pages, link equity | 04-on-page-seo/internal-linking/SKILL.md | active |
| 04.06 | On-page content optimization | child | On-Page SEO |  |  | optimize content, content score, semantic keywords, readability | 04-on-page-seo/content-optimization/SKILL.md | active |
| 04.07 | Entity optimization | child | On-Page SEO |  |  | entity seo, knowledge graph, sameas, brand entity | 04-on-page-seo/entity-optimization/SKILL.md | active |
| 05 | Off-Page SEO | parent | SEO Master | seo-offpage |  | backlinks, link building, digital pr, guest post, brand mentions, citations, link audit, toxic links, disavow | 05-off-page-seo/SKILL.md | active |
| 05.01 | Link building | child | Off-Page SEO |  |  | link building, outreach, resource links, broken link building | 05-off-page-seo/link-building/SKILL.md | active |
| 05.02 | Backlink analysis | child | Off-Page SEO |  |  | backlink profile, referring domains, anchor distribution | 05-off-page-seo/backlinks/SKILL.md | active |
| 05.03 | Digital PR | child | Off-Page SEO |  |  | digital pr, press, data study | 05-off-page-seo/digital-pr/SKILL.md | active |
| 05.04 | Guest posting | child | Off-Page SEO |  |  | guest post, contributor | 05-off-page-seo/guest-posting/SKILL.md | active |
| 05.05 | Brand mentions and citations | child | Off-Page SEO |  |  | brand mention, unlinked mention, citation | 05-off-page-seo/brand-mentions/SKILL.md | active |
| 05.06 | Link audit | child | Off-Page SEO | seo-backlink-audit |  | toxic links, disavow, link penalty, backlink audit | 05-off-page-seo/link-audit/SKILL.md | active |
| 06 | Content SEO | parent | SEO Master | seo-content-audit |  | content seo, content strategy, topic cluster, pillar page, content gap, seo copywriting, content refresh, content audit, thin content, cannibalization | 06-content-seo/SKILL.md | active |
| 06.01 | Content strategy | child | Content SEO |  | content-strategy (installed skill) | content strategy, content calendar, content brief | 06-content-seo/content-strategy/SKILL.md | active |
| 06.02 | Topical authority | child | Content SEO |  |  | topical authority, topic coverage | 06-content-seo/topical-authority/SKILL.md | active |
| 06.03 | Content clusters | child | Content SEO |  | pillar-content-architecture (installed skill) | topic cluster, pillar, hub and spoke | 06-content-seo/content-clusters/SKILL.md | active |
| 06.04 | Content gap | child | Content SEO | seo-content-gap-audit |  | content gap, missing topics, decay | 06-content-seo/content-gap/SKILL.md | active |
| 06.05 | SEO copywriting | child | Content SEO |  |  | seo copywriting, write seo article | 06-content-seo/seo-copywriting/SKILL.md | active |
| 06.06 | Content audit and refresh | child | Content SEO | seo-content-audit | content-refresh-system (installed skill) | content audit, refresh, prune, thin content, duplicate content, cannibalization | 06-content-seo/content-refresh/SKILL.md | active |
| 07 | Local SEO | parent | SEO Master | local-seo-manager |  | local seo, google business profile, gbp, map pack, nap, citations, reviews, location page, service area | 07-local-seo/SKILL.md | active |
| 07.01 | Google Business Profile | child | Local SEO |  |  | gbp, google business profile, google maps | 07-local-seo/google-business-profile/SKILL.md | active |
| 07.02 | Local keywords and pages | child | Local SEO |  |  | local keywords, location page, service area page | 07-local-seo/local-keywords/SKILL.md | active |
| 07.03 | Citations / NAP | child | Local SEO |  |  | citations, nap, directories | 07-local-seo/citations/SKILL.md | active |
| 07.04 | Local links | child | Local SEO |  |  | local backlinks, sponsorships | 07-local-seo/local-links/SKILL.md | active |
| 07.05 | Reviews | child | Local SEO |  |  | reviews, reputation | 07-local-seo/reviews/SKILL.md | active |
| 07.06 | Local schema | child | Local SEO |  | 27-schema-seo/local-business | localbusiness schema | 07-local-seo/local-schema/SKILL.md | active |
| 08 | E-commerce SEO | parent | SEO Master |  |  | ecommerce seo, product page seo, category page, faceted navigation, product schema, merchant center, out of stock | 08-ecommerce-seo/SKILL.md | active |
| 08.01 | Product SEO | child | E-commerce SEO |  |  | product page seo, product title, product description | 08-ecommerce-seo/product-seo/SKILL.md | active |
| 08.02 | Category SEO | child | E-commerce SEO |  |  | category page, collection page | 08-ecommerce-seo/category-seo/SKILL.md | active |
| 08.03 | Faceted navigation | child | E-commerce SEO |  |  | filters, facets, parameters | 08-ecommerce-seo/faceted-navigation/SKILL.md | active |
| 08.04 | Product schema | child | E-commerce SEO |  | 27-schema-seo/product | product schema, offer, review schema | 08-ecommerce-seo/product-schema/SKILL.md | active |
| 08.05 | Merchant Center and Shopping | child | E-commerce SEO |  |  | merchant center, google shopping, product feed | 08-ecommerce-seo/merchant-center/SKILL.md | active |
| 08.06 | E-commerce content | child | E-commerce SEO |  |  | buying guide, ecommerce blog | 08-ecommerce-seo/ecommerce-content/SKILL.md | active |
| 09 | WooCommerce SEO | parent | SEO Master |  |  | woocommerce seo, woo product not indexed, shop page, product attributes, variable product, cart noindex | 09-woocommerce-seo/SKILL.md | active |
| 09.01 | Products | child | WooCommerce SEO |  | 08-ecommerce-seo/product-seo | woocommerce product seo, variable product | 09-woocommerce-seo/products/SKILL.md | active |
| 09.02 | Categories | child | WooCommerce SEO |  |  | woocommerce category, shop page | 09-woocommerce-seo/categories/SKILL.md | active |
| 09.03 | Attributes | child | WooCommerce SEO |  |  | product attributes, tags | 09-woocommerce-seo/attributes/SKILL.md | active |
| 09.04 | Filters | child | WooCommerce SEO |  | 08-ecommerce-seo/faceted-navigation | woocommerce filter, layered nav | 09-woocommerce-seo/filters/SKILL.md | active |
| 09.05 | Product schema in Woo | child | WooCommerce SEO |  | 27-schema-seo/product | woocommerce schema | 09-woocommerce-seo/product-schema/SKILL.md | active |
| 09.06 | Woo technical | child | WooCommerce SEO |  | 03-technical-seo | woocommerce sitemap, woo speed, woo permalink | 09-woocommerce-seo/woocommerce-technical/SKILL.md | active |
| 10 | Shopify SEO | parent | SEO Master |  |  | shopify seo, collection, liquid, shopify canonical, shopify app conflict, robots.txt.liquid | 10-shopify-seo/SKILL.md | active |
| 10.01 | Products | child | Shopify SEO |  |  | shopify product seo | 10-shopify-seo/products/SKILL.md | active |
| 10.02 | Collections | child | Shopify SEO |  |  | shopify collection seo | 10-shopify-seo/collections/SKILL.md | active |
| 10.03 | Shopify technical | child | Shopify SEO |  | 03-technical-seo | shopify sitemap, shopify robots, shopify speed, shopify duplicate | 10-shopify-seo/shopify-technical/SKILL.md | active |
| 10.04 | Liquid / theme SEO | child | Shopify SEO |  |  | liquid, theme seo | 10-shopify-seo/liquid-seo/SKILL.md | active |
| 10.05 | Shopify structured data | child | Shopify SEO |  | 27-schema-seo/product | shopify schema | 10-shopify-seo/structured-data/SKILL.md | active |
| 10.06 | Shopify migration | child | Shopify SEO |  | 31-seo-migration/platform-migration | migrate to shopify | 10-shopify-seo/shopify-migration/SKILL.md | active |
| 11 | WordPress SEO | parent | SEO Master |  |  | wordpress seo, yoast, rank math, permalink, wp plugin conflict, wp theme seo, wp speed | 11-wordpress-seo/SKILL.md | active |
| 11.01 | WordPress technical | child | WordPress SEO |  | 03-technical-seo | wordpress sitemap robots canonical | 11-wordpress-seo/wordpress-technical/SKILL.md | active |
| 11.02 | SEO plugin conflicts | child | WordPress SEO |  |  | plugin conflict, duplicate meta, duplicate schema | 11-wordpress-seo/plugins/SKILL.md | active |
| 11.03 | Rank Math | child | WordPress SEO |  |  | rank math | 11-wordpress-seo/rank-math/SKILL.md | active |
| 11.04 | Yoast SEO | child | WordPress SEO |  |  | yoast | 11-wordpress-seo/yoast/SKILL.md | active |
| 11.05 | WordPress schema | child | WordPress SEO |  | 27-schema-seo | wordpress schema | 11-wordpress-seo/wordpress-schema/SKILL.md | active |
| 11.06 | WordPress performance | child | WordPress SEO |  | 03-technical-seo/core-web-vitals | wordpress speed, wp rocket, cache | 11-wordpress-seo/wordpress-performance/SKILL.md | active |
| 12 | SaaS SEO | parent | SEO Master |  |  | saas seo, landing page, feature page, use case page, integration page, comparison page, alternative page, free tool, docs seo, product-led seo | 12-saas-seo/SKILL.md | active |
| 12.01 | Landing pages | child | SaaS SEO |  |  | saas landing page | 12-saas-seo/landing-pages/SKILL.md | active |
| 12.02 | Feature pages | child | SaaS SEO |  |  | feature page, use case | 12-saas-seo/feature-pages/SKILL.md | active |
| 12.03 | Comparison and alternative pages | child | SaaS SEO |  | competitor-alternatives (installed skill) | vs, alternative, comparison, alternatives to | 12-saas-seo/comparison-pages/SKILL.md | active |
| 12.04 | Integration pages | child | SaaS SEO |  |  | integration page, app marketplace | 12-saas-seo/integration-pages/SKILL.md | active |
| 12.05 | Programmatic SaaS pages | child | SaaS SEO |  | 15-programmatic-seo | programmatic saas, templates at scale | 12-saas-seo/programmatic-saas/SKILL.md | active |
| 13 | ERP SEO | parent | SEO Master |  |  | erp seo, accounting software, inventory software, hr payroll software, crm module, manufacturing software | 13-erp-seo/SKILL.md | active |
| 14 | POS SEO | parent | SEO Master |  |  | pos seo, point of sale, restaurant pos, grocery pos, pharmacy pos, retail pos, multi-branch pos, pos hardware | 14-pos-seo/SKILL.md | active |
| 15 | Programmatic SEO | parent | SEO Master | programmatic-seo |  | programmatic seo, pages at scale, template pages, location pages, database pages, directory | 15-programmatic-seo/SKILL.md | active |
| 15.01 | Template pages | child | Programmatic SEO |  |  | template, dynamic landing pages | 15-programmatic-seo/template-pages/SKILL.md | active |
| 15.02 | Database-driven pages | child | Programmatic SEO |  |  | database seo, directory | 15-programmatic-seo/database-pages/SKILL.md | active |
| 15.03 | Location pages | child | Programmatic SEO |  | 07-local-seo | location x service | 15-programmatic-seo/location-pages/SKILL.md | active |
| 15.04 | Programmatic comparisons | child | Programmatic SEO |  | 12-saas-seo/comparison-pages | comparison at scale | 15-programmatic-seo/comparison-pages/SKILL.md | active |
| 15.05 | Programmatic internal linking | child | Programmatic SEO |  |  | internal linking automation, index bloat | 15-programmatic-seo/programmatic-internal-linking/SKILL.md | active |
| 16 | Image SEO | parent | SEO Master |  |  | image seo, alt text, image filename, webp, avif, image compression, image sitemap, google images | 16-image-seo/SKILL.md | active |
| 16.01 | Alt text | child | Image SEO |  |  | alt text, image alt | 16-image-seo/alt-text/SKILL.md | active |
| 16.02 | Filenames | child | Image SEO |  |  | image filename | 16-image-seo/filenames/SKILL.md | active |
| 16.03 | Compression and formats | child | Image SEO |  | 03-technical-seo/core-web-vitals | image compression, webp, avif, lazy loading, responsive images | 16-image-seo/image-compression/SKILL.md | active |
| 16.04 | Image sitemap | child | Image SEO |  |  | image sitemap | 16-image-seo/image-sitemap/SKILL.md | active |
| 16.05 | Image structured data | child | Image SEO |  |  | image schema, imageobject | 16-image-seo/image-schema/SKILL.md | active |
| 17 | Video SEO | parent | SEO Master |  |  | video seo, youtube seo, video schema, video sitemap, transcript, thumbnail | 17-video-seo/SKILL.md | active |
| 17.01 | YouTube SEO | child | Video SEO |  |  | youtube seo | 17-video-seo/youtube-seo/SKILL.md | active |
| 17.02 | Video schema | child | Video SEO |  | 27-schema-seo/schema-validation | videoobject | 17-video-seo/video-schema/SKILL.md | active |
| 17.03 | Video sitemap | child | Video SEO |  |  | video sitemap | 17-video-seo/video-sitemap/SKILL.md | active |
| 17.04 | Video content on page | child | Video SEO |  |  | video page | 17-video-seo/video-content/SKILL.md | active |
| 18 | International SEO | parent | SEO Master |  |  | international seo, hreflang, multilingual, country targeting, translation seo, cctld, subdirectory | 18-international-seo/SKILL.md | active |
| 18.01 | Hreflang | child | International SEO |  |  | hreflang, x-default | 18-international-seo/hreflang/SKILL.md | active |
| 18.02 | Multilingual content | child | International SEO |  |  | translation, localization | 18-international-seo/multilingual/SKILL.md | active |
| 18.03 | Country targeting | child | International SEO |  |  | geo targeting, cctld | 18-international-seo/country-targeting/SKILL.md | active |
| 18.04 | International architecture | child | International SEO |  |  | international site structure | 18-international-seo/international-architecture/SKILL.md | active |
| 19 | AI SEO | parent | SEO Master | ai-seo, seo-aeo-amplifier |  | ai seo, ai search, ai visibility, ai citations, machine-readable content, ai referral traffic, ai content seo | 19-ai-seo/SKILL.md | active |
| 19.01 | AI search optimization | child | AI SEO |  |  | ai search optimization, ai overviews | 19-ai-seo/ai-search/SKILL.md | active |
| 19.02 | AI-ready content | child | AI SEO |  |  | ai readable content, machine readable | 19-ai-seo/ai-content/SKILL.md | active |
| 19.03 | AI citations | child | AI SEO |  |  | ai citation, citability, source selection | 19-ai-seo/ai-citations/SKILL.md | active |
| 19.04 | AI visibility tracking | child | AI SEO |  |  | ai visibility, ai mention tracking, ai referral | 19-ai-seo/ai-visibility/SKILL.md | active |
| 20 | GEO | parent | SEO Master | seo-aeo-geo |  | geo, generative engine optimization, ai overviews, generative search, ai brand visibility, entity authority | 20-geo/SKILL.md | active |
| 20.01 | Generative search | child | GEO |  |  | generative search, google ai overviews, copilot | 20-geo/generative-search/SKILL.md | active |
| 20.02 | Entity visibility | child | GEO |  | 04-on-page-seo/entity-optimization | entity authority, knowledge graph | 20-geo/entity-visibility/SKILL.md | active |
| 20.03 | Citation optimization | child | GEO |  | 19-ai-seo/ai-citations | citation optimization | 20-geo/citation-optimization/SKILL.md | active |
| 20.04 | AI brand visibility | child | GEO |  | 19-ai-seo/ai-visibility | brand visibility in ai | 20-geo/ai-brand-visibility/SKILL.md | active |
| 21 | AEO | parent | SEO Master | aeo |  | aeo, answer engine optimization, featured snippet, faq, people also ask, voice search, direct answer | 21-aeo/SKILL.md | active |
| 21.01 | Answer optimization | child | AEO |  |  | direct answer, answer-first | 21-aeo/answer-optimization/SKILL.md | active |
| 21.02 | Featured snippets and PAA | child | AEO |  |  | featured snippet, people also ask, paa | 21-aeo/featured-snippets/SKILL.md | active |
| 21.03 | FAQ | child | AEO |  | 27-schema-seo/faq | faq, faq schema | 21-aeo/faq/SKILL.md | active |
| 21.04 | Voice and conversational | child | AEO |  |  | voice search, conversational | 21-aeo/voice-search/SKILL.md | active |
| 22 | ChatGPT SEO | parent | SEO Master |  |  | chatgpt seo, chatgpt search, chatgpt citations, openai search, chatgpt referral | 22-chatgpt-seo/SKILL.md | active |
| 23 | Claude SEO | parent | SEO Master |  |  | claude seo, claude visibility, anthropic search | 23-claude-seo/SKILL.md | active |
| 24 | Gemini SEO | parent | SEO Master |  |  | gemini seo, google ai ecosystem, gemini visibility | 24-gemini-seo/SKILL.md | active |
| 25 | Perplexity SEO | parent | SEO Master |  |  | perplexity seo, perplexity citations | 25-perplexity-seo/SKILL.md | active |
| 26 | AI Agent / Agentic SEO | parent | SEO Master |  |  | ai agent seo, agentic, llms.txt, webmcp, machine-readable website, agent discoverability | 26-ai-agent-seo/SKILL.md | active |
| 26.01 | Agent discoverability | child | AI Agent / Agentic SEO |  |  | agent discoverability, llms.txt | 26-ai-agent-seo/agent-discoverability/SKILL.md | active |
| 26.02 | Machine-readable content | child | AI Agent / Agentic SEO |  |  | machine readable | 26-ai-agent-seo/machine-readable-content/SKILL.md | active |
| 26.03 | Structured content | child | AI Agent / Agentic SEO |  |  | structured content | 26-ai-agent-seo/structured-content/SKILL.md | active |
| 26.04 | Agent accessibility | child | AI Agent / Agentic SEO |  |  | agent accessible forms | 26-ai-agent-seo/agent-accessibility/SKILL.md | active |
| 27 | Schema / Structured Data | parent | SEO Master | schema-markup |  | schema, json-ld, structured data, rich results, schema validation | 27-schema-seo/SKILL.md | active |
| 27.01 | Organization | child | Schema / Structured Data |  |  | organization schema | 27-schema-seo/organization/SKILL.md | active |
| 27.02 | LocalBusiness | child | Schema / Structured Data |  |  | localbusiness schema | 27-schema-seo/local-business/SKILL.md | active |
| 27.03 | Product and Offer | child | Schema / Structured Data |  |  | product schema, offer, price | 27-schema-seo/product/SKILL.md | active |
| 27.04 | Article / BlogPosting | child | Schema / Structured Data |  |  | article schema | 27-schema-seo/article/SKILL.md | active |
| 27.05 | FAQPage | child | Schema / Structured Data |  |  | faq schema | 27-schema-seo/faq/SKILL.md | active |
| 27.06 | BreadcrumbList | child | Schema / Structured Data |  |  | breadcrumb schema | 27-schema-seo/breadcrumb/SKILL.md | active |
| 27.07 | Review and AggregateRating | child | Schema / Structured Data |  |  | review schema, rating | 27-schema-seo/review/SKILL.md | active |
| 27.08 | Schema validation | child | Schema / Structured Data |  |  | validate schema, rich results test | 27-schema-seo/schema-validation/SKILL.md | active |
| 28 | SEO Analytics | parent | SEO Master |  |  | seo analytics, ga4, search console data, seo reporting, keyword tracking, organic traffic analysis | 28-seo-analytics/SKILL.md | active |
| 28.01 | GA4 | child | SEO Analytics |  |  | ga4, google analytics | 28-seo-analytics/google-analytics/SKILL.md | active |
| 28.02 | Search Console analysis | child | SEO Analytics |  |  | gsc analysis, queries, pages | 28-seo-analytics/search-console/SKILL.md | active |
| 28.03 | SEO reporting | child | SEO Analytics |  |  | seo report | 28-seo-analytics/seo-reporting/SKILL.md | active |
| 28.04 | Keyword tracking | child | SEO Analytics |  | 32-seo-monitoring/rankings | keyword tracking | 28-seo-analytics/keyword-tracking/SKILL.md | active |
| 28.05 | Performance analysis | child | SEO Analytics |  |  | organic performance | 28-seo-analytics/performance-analysis/SKILL.md | active |
| 29 | SEO Tools and APIs | parent | SEO Master |  |  | seo tools, ahrefs, semrush, screaming frog, dataforseo, pagespeed api, gsc api, seo scraping | 29-seo-tools-api/SKILL.md | active |
| 29.01 | Keyword tools | child | SEO Tools and APIs |  |  | keyword planner, google trends, ahrefs keywords | 29-seo-tools-api/keyword-tools/SKILL.md | active |
| 29.02 | Backlink tools | child | SEO Tools and APIs |  |  | ahrefs backlinks, semrush backlinks | 29-seo-tools-api/backlink-tools/SKILL.md | active |
| 29.03 | SEO APIs | child | SEO Tools and APIs |  |  | gsc api, ga4 api, pagespeed api, dataforseo | 29-seo-tools-api/seo-apis/SKILL.md | active |
| 29.04 | Data collection | child | SEO Tools and APIs |  |  | export data, crawl data, screaming frog | 29-seo-tools-api/data-collection/SKILL.md | active |
| 29.05 | Scraping (compliant) | child | SEO Tools and APIs |  |  | scrape serp, scraping | 29-seo-tools-api/scraping/SKILL.md | active |
| 30 | SEO Audit | parent | SEO Master | seo-audit, seo-audit-orchestration |  | seo audit, site audit, technical audit, on-page audit, backlink audit, ecommerce audit, full audit, seo health check | 30-seo-audit/SKILL.md | active |
| 30.01 | Full audit | child | SEO Audit | seo-audit | 30-seo-audit/technical-audit; 30-seo-audit/onpage-audit | seo audit, full site audit, what is wrong with my seo | 30-seo-audit/full-audit/SKILL.md | active |
| 30.02 | Technical audit | child | SEO Audit | seo-site-health-audit | 03-technical-seo | technical audit, site health, crawl audit | 30-seo-audit/technical-audit/SKILL.md | active |
| 30.03 | On-page audit | child | SEO Audit |  | 04-on-page-seo | on-page audit | 30-seo-audit/onpage-audit/SKILL.md | active |
| 30.04 | Backlink audit | child | SEO Audit |  | 05-off-page-seo/link-audit | backlink audit | 30-seo-audit/backlink-audit/SKILL.md | active |
| 30.05 | E-commerce audit | child | SEO Audit |  | 08-ecommerce-seo; 09-woocommerce-seo; 10-shopify-seo | ecommerce audit, woocommerce audit, shopify audit | 30-seo-audit/ecommerce-audit/SKILL.md | active |
| 31 | SEO Migration | parent | SEO Master |  |  | seo migration, domain change, https migration, replatform, redirect map, relaunch, ranking recovery | 31-seo-migration/SKILL.md | active |
| 31.01 | Domain migration | child | SEO Migration |  |  | domain change, rebrand domain | 31-seo-migration/domain-migration/SKILL.md | active |
| 31.02 | Platform migration | child | SEO Migration |  |  | replatform, wordpress to shopify | 31-seo-migration/platform-migration/SKILL.md | active |
| 31.03 | URL migration | child | SEO Migration |  |  | url structure change, redirect mapping, http to https | 31-seo-migration/url-migration/SKILL.md | active |
| 31.04 | Migration monitoring | child | SEO Migration |  |  | post migration, ranking recovery | 31-seo-migration/migration-monitoring/SKILL.md | active |
| 32 | SEO Monitoring | parent | SEO Master |  |  | seo monitoring, rank tracking, traffic drop, indexing monitoring, technical errors, alerts, seo drift | 32-seo-monitoring/SKILL.md | active |
| 32.01 | Rank tracking | child | SEO Monitoring | seo-rank-tracking |  | rank tracking, keyword rankings | 32-seo-monitoring/rankings/SKILL.md | active |
| 32.02 | Indexing monitoring | child | SEO Monitoring |  |  | index monitoring | 32-seo-monitoring/indexing/SKILL.md | active |
| 32.03 | Traffic diagnosis | child | SEO Monitoring | seo-traffic-diagnosis |  | traffic drop, traffic decline | 32-seo-monitoring/traffic/SKILL.md | active |
| 32.04 | Technical error monitoring | child | SEO Monitoring |  |  | 5xx, 404 spike, cwv regression | 32-seo-monitoring/technical-errors/SKILL.md | active |
| 32.05 | Alerts | child | SEO Monitoring |  |  | seo alerts | 32-seo-monitoring/alerts/SKILL.md | active |
| 33 | SEO Automation | parent | SEO Master |  |  | automate seo, automated audit, automated reporting, seo workflow, seo agent, bulk metadata | 33-seo-automation/SKILL.md | active |
| 33.01 | Automated audits | child | SEO Automation |  |  | scheduled audit | 33-seo-automation/automated-audits/SKILL.md | active |
| 33.02 | Automated reporting | child | SEO Automation |  |  | automated seo report | 33-seo-automation/automated-reporting/SKILL.md | active |
| 33.03 | Automated monitoring | child | SEO Automation |  | 32-seo-monitoring | automated monitoring | 33-seo-automation/automated-monitoring/SKILL.md | active |
| 33.04 | Workflow automation | child | SEO Automation |  |  | bulk metadata, internal link automation, schema generation, sitemap automation | 33-seo-automation/workflow-automation/SKILL.md | active |
| 33.05 | SEO agents | child | SEO Automation |  |  | seo agent | 33-seo-automation/seo-agents/SKILL.md | active |
