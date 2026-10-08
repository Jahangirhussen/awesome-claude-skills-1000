# Subscription Metrics

Open only the module section needed. IDs are in `../GRAPH-REGISTRY.md`.

## SaaS: Subscription
Role: SaaS Admin / Finance. Data: subscriptions, plans, payments (status, plan_id, started_at, canceled_at, renewed_at).

| Graph | Chart | Question |
|---|---|---|
| Active Subscriptions | KPI Card + Line Chart | How has Active Subscriptions changed over time and is the trend healthy? |
| New Subscriptions | KPI Card + Line Chart | How has New Subscriptions changed over time and is the trend healthy? |
| Cancelled Subscriptions | KPI Card + Line Chart | How has Cancelled Subscriptions changed over time and is the trend healthy? |
| Subscription Growth | Line Chart | How has Subscription Growth changed over time and is the trend healthy? |
| Plan Distribution | Donut / 100% Stacked Bar | What is the composition of Plan Distribution? |
| Revenue by Plan | Horizontal Bar | Which segments drive Revenue by Plan? |
| Users by Plan | Horizontal Bar | Which segments drive Users by Plan? |
| Trial Users | KPI Card + Line Chart | How has Trial Users changed over time and is the trend healthy? |
| Trial Conversion | KPI Card + Sparkline | What is the current level of Trial Conversion, and how does it compare with the previous period? |
| Subscription Churn | KPI Card + Sparkline | What is the current level of Subscription Churn, and how does it compare with the previous period? |
| Upgrade Rate | KPI Card + Sparkline | What is the current level of Upgrade Rate, and how does it compare with the previous period? |
| Downgrade Rate | KPI Card + Sparkline | What is the current level of Downgrade Rate, and how does it compare with the previous period? |
| Renewal Rate | KPI Card + Sparkline | What is the current level of Renewal Rate, and how does it compare with the previous period? |
| Failed Payments | KPI Card + Line Chart | How has Failed Payments changed over time and is the trend healthy? |
| Payment Recovery | KPI Card + Line Chart | How has Payment Recovery changed over time and is the trend healthy? |
| Subscription Cohort | Cohort Heatmap | How do cohorts differ in Subscription Cohort over their lifetime? |
| Subscription Lifetime | Histogram / Box Plot | What is the current level of Subscription Lifetime, and how does it compare with the previous period? |
| Plan Migration | Sankey | What is the current level of Plan Migration, and how does it compare with the previous period? |

## Definitions and formulas (use consistently)
- MRR = sum of normalized monthly recurring revenue of active subscriptions (annual plan / 12). Exclude one-time fees, taxes.
- ARR = MRR x 12.
- New MRR = MRR from customers whose first paid subscription started in period. Expansion = upgrades/add-ons/seats. Contraction = downgrades. Churned = MRR of cancelled subscriptions.
- Net New MRR = New + Expansion - Contraction - Churned.
- Customer (logo) churn % = customers lost in period / customers at start of period.
- Revenue churn % = (Churned + Contraction MRR) / MRR at start.
- NRR = (Start MRR + Expansion - Contraction - Churned) / Start MRR (excludes new customers). GRR = (Start MRR - Contraction - Churned) / Start MRR (max 100%).
- ARPU = MRR / active paying customers.
- LTV (simple) = ARPU x gross margin % / monthly churn rate. CAC = (sales + marketing cost) / new customers. LTV:CAC target >= 3. CAC payback (months) = CAC / (ARPU x gross margin %).
- Quick ratio = (New + Expansion MRR) / (Contraction + Churned MRR); >4 is strong.
- Trial conversion = trials that became paid / trials started (cohort by trial start date).
- DAU/MAU stickiness = average DAU / MAU in the same month.
- Always state period, currency, timezone, and handling of refunds, discounts, and failed payments.
