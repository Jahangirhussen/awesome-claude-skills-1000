# Cohort Analysis

Open only the module section needed. IDs are in `../GRAPH-REGISTRY.md`.

## SaaS: Cohort
Role: Product / Growth. Data: users or subscriptions with cohort_date and activity by period.

| Graph | Chart | Question |
|---|---|---|
| User Cohort | Cohort Heatmap | How do cohorts differ in User Cohort over their lifetime? |
| Revenue Cohort | Cohort Heatmap | How do cohorts differ in Revenue Cohort over their lifetime? |
| Retention Cohort | Cohort Heatmap | How do cohorts differ in Retention Cohort over their lifetime? |
| Subscription Cohort Retention | Cohort Heatmap | How do cohorts differ in Subscription Cohort Retention over their lifetime? |
| Churn Cohort | Cohort Heatmap | How do cohorts differ in Churn Cohort over their lifetime? |
| Activation Cohort | Cohort Heatmap | How do cohorts differ in Activation Cohort over their lifetime? |
| Conversion Cohort | Cohort Heatmap | How do cohorts differ in Conversion Cohort over their lifetime? |

## Method
1. Cohort = users (or subscriptions) grouped by signup/first-paid month (or week for fast products).
2. Period index = months since cohort start (0, 1, 2...). Cell = % of cohort still active (or revenue retained / cohort start revenue).
3. Chart: cohort heatmap (rows cohorts, columns period index, sequential color scale, values printed in cells); add a line chart of selected cohorts for retention curves.
4. Read: rows = quality of acquisition over time; columns = lifecycle shape; a flattening curve = a retained core.
5. Pitfalls: partial periods (grey out incomplete cells), tiny cohorts (show n), mixing plans (segment), revenue cohorts above 100% are valid with expansion.
6. Interactions: filter by plan/channel/country; toggle users vs revenue; hover shows n and %.
