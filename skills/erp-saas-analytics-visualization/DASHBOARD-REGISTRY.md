# Dashboard Registry

| Dashboard | Role | KPIs | Charts | Filters | Drilldowns | Priority |
|---|---|---|---|---|---|---|
| ERP Executive | Admin / Executive | Revenue, Profit, Cash position, Receivables, Payables | Revenue vs Expense, Profit Trend, Cash Flow, Sales Trend, Top Products, Branch Performance, Inventory Alerts | date, branch, region | branch -> product -> order | Critical |
| ERP Sales | Sales Manager | Sales, AOV, Orders, Target attainment | Sales Trend, Sales by Branch, Top Products, Top Customers, Salesperson Performance, Sales Funnel, Target vs Actual | date, branch, product, category, channel, salesperson | branch -> salesperson -> order | High |
| ERP Inventory | Inventory Manager | Stock value, Low stock count, Out-of-stock, Turnover | Stock Movement, Low Stock, Out of Stock, Fast vs Slow Moving, Stock Aging, Warehouse Performance | warehouse, branch, category, product | category -> product -> batch | High |
| ERP Finance | Finance Manager | Revenue, Expenses, Profit, Cash, AR, AP | Cash Flow, AR/AP Aging, Budget vs Actual, Expense Breakdown, P&L Trend | date, branch, department | account -> transaction | Critical |
| ERP HR | HR Manager | Headcount, Attendance %, Payroll, Turnover | Attendance, Leave, Payroll Trend, Department Distribution, Performance, Turnover | date, department, branch | department -> employee | Medium |
| ERP CRM | Sales Manager | Leads, Pipeline value, Win rate, Cycle length | Sales Funnel, Pipeline by Stage, Lead Sources, Lost Deal Analysis, Win Rate Trend | date, owner, source, stage | stage -> deal | High |
| ERP Manufacturing | Production Manager | Output, Efficiency, Defect rate, Downtime | Production Target vs Actual, Machine Utilization, Defect Rate, Work Order Status, Maintenance | date, factory, machine, product | machine -> work order | Medium |
| ERP Project | Project Manager | Active projects, Overdue tasks, Utilization | Project Progress, Gantt, Team Workload, Budget vs Actual, Profitability | project, team, date | project -> task | Medium |
| SaaS Executive | SaaS Admin / Founder | MRR, ARR, Customers, Active users, Churn, NRR, CAC, LTV, LTV:CAC | MRR Trend + MRR movements, Customer Growth, Churn, Retention, Revenue by Plan, Cohort, Conversion Funnel | date, plan, segment, country | plan -> customer | Critical |
| SaaS Subscription | SaaS Admin / Finance | Active subs, Renewal rate, Failed payments | Plan Distribution, Upgrades/Downgrades, Trial Conversion, Payment Recovery, Subscription Cohort | plan, date, payment method | plan -> subscription | High |
| SaaS Product | Product Manager | DAU/MAU, Activation rate, Feature adoption | Feature Usage, Adoption, Retention curves, User Journey, Power vs Inactive Users | feature, plan, date, cohort | feature -> user | High |
| SaaS Support | Support Manager | Open tickets, FRT, Resolution time, CSAT, SLA | Ticket Trend, Tickets by Category/Priority/Agent, SLA Compliance, Backlog | date, priority, agent, category | category -> ticket | Medium |
| SaaS Marketing | Marketing Manager | Visitors, Signups, CAC, ROAS | Channel Performance, Funnel Conversion, Spend vs Revenue, Attribution | date, channel, campaign | channel -> campaign -> keyword | High |
| SaaS Infrastructure | Engineering / DevOps | Uptime, Error rate, p95 latency, Queue length | API Latency, Error Rate, CPU/Memory, Job Success, Storage | service, env, time range | service -> endpoint -> trace | High |
