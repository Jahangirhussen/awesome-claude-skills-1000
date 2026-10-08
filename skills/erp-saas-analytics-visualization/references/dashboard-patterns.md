# Dashboard patterns

Layout: top row KPI cards (value, delta vs previous period, sparkline) -> trend charts -> comparison/composition -> diagnostic/drill-down table. Max ~8-12 widgets per dashboard; one question per widget.

Chart roles: KPI (single number), Trend (over time), Comparison (across segments), Composition (shares), Diagnostic (why: cohort, funnel, outliers).

Global filters: date range (with compare period), branch/region, product/category, customer segment, plan, channel, department. Persist filter state in URL.

Interactions that add value: hover tooltip, legend toggle, drill-down (card -> chart -> table -> record), click-to-filter, export CSV/PDF, table view, fullscreen. Skip those that do not help the decision.

Performance: aggregate in SQL/materialized views, cache by filter key, refresh cadence per metric (real-time for ops, hourly/daily for finance), pre-compute heavy cohorts.

Permissions: filter rows by branch/tenant, hide finance and salary widgets from unauthorized roles, enforce server-side, never only hide in UI.

Responsive: stack cards on mobile, reduce legends, truncate labels with tooltip, horizontal scroll only for wide tables.
