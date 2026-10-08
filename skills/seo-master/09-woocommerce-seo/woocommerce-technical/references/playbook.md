# Playbook: Woo technical

## How to do it
1. Noindex cart, checkout, my-account, wishlist, compare
2. Sitemap: products, categories only; exclude tags/attributes if thin
3. Speed: object cache, page cache excluding cart, optimized images, remove unused scripts (wc-cart-fragments where possible)
4. Check canonical and hreflang with multilingual plugins

## Common problems and fixes
- Cart fragments slowing pages -> restrict to cart pages
- Session cookies breaking cache -> exclude only needed endpoints

## Output
Technical fix list.

## Tools and data sources
WooCommerce admin, Yoast/Rank Math, Query Monitor, Screaming Frog, WP-CLI, Rich Results Test.

## Related
- Parent: `../SKILL.md` (scope, installed skills, method)
- `ROUTER.md` and `DEPENDENCIES.md` at the seo-master root for other categories that may apply.

## Verify
- Re-fetch or re-crawl the changed URLs and confirm the fix is live (status, rendered HTML, schema validator, GSC URL Inspection as relevant).
- Compare against the baseline you recorded before the change.
- Report what changed, the evidence, and any remaining issue in a short DONE summary.
