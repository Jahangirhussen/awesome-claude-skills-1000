# Erp Charts

Open only the module section needed. IDs are in `../GRAPH-REGISTRY.md`.

## ERP: Executive
Role: Admin / Executive. Data: ledger, orders, expenses (date, amount, branch_id).

| Graph | Chart | Question |
|---|---|---|
| Revenue Trend | Line Chart | How has Revenue Trend changed over time and is the trend healthy? |
| Profit Trend | Line Chart | How has Profit Trend changed over time and is the trend healthy? |
| Expense Trend | Line Chart | How has Expense Trend changed over time and is the trend healthy? |
| Net Profit Trend | Line Chart | How has Net Profit Trend changed over time and is the trend healthy? |
| Gross Profit Trend | Line Chart | How has Gross Profit Trend changed over time and is the trend healthy? |
| Revenue vs Expense | Grouped Bar | Are we on plan for Revenue vs Expense? |
| Revenue vs Profit | Grouped Bar | Are we on plan for Revenue vs Profit? |
| Profit Margin Trend | Line Chart | How has Profit Margin Trend changed over time and is the trend healthy? |
| Cash Flow Trend | Area / Line | How has Cash Flow Trend changed over time and is the trend healthy? |
| Sales Target vs Actual | Grouped Bar | Are we on plan for Sales Target vs Actual? |
| Budget vs Actual | Grouped Bar | Are we on plan for Budget vs Actual? |
| KPI Summary | KPI Card + Sparkline | What is the current level of KPI Summary, and how does it compare with the previous period? |
| Department Performance | KPI Card + Line Chart | How has Department Performance changed over time and is the trend healthy? |
| Branch Performance | KPI Card + Line Chart | How has Branch Performance changed over time and is the trend healthy? |
| Region Performance | Choropleth / Bubble Map | Where is Region Performance concentrated geographically? |
| Business Growth | Line Chart | How has Business Growth changed over time and is the trend healthy? |
| Monthly Performance | Line Chart | How has Monthly Performance changed over time and is the trend healthy? |
| Quarterly Performance | Line Chart | How has Quarterly Performance changed over time and is the trend healthy? |
| Year-over-Year Growth | Line Chart | How has Year-over-Year Growth changed over time and is the trend healthy? |
| Month-over-Month Growth | Line Chart | How has Month-over-Month Growth changed over time and is the trend healthy? |

## ERP: Manufacturing
Role: Production Manager. Data: work_orders, production_logs, machines, bom (date, qty, status, machine_id, downtime_min).

| Graph | Chart | Question |
|---|---|---|
| Production Trend | Line Chart | How has Production Trend changed over time and is the trend healthy? |
| Production by Product | Horizontal Bar | Which segments drive Production by Product? |
| Production by Factory | Horizontal Bar | Which segments drive Production by Factory? |
| Production by Machine | Horizontal Bar | Which segments drive Production by Machine? |
| Production Target vs Actual | Grouped Bar | Are we on plan for Production Target vs Actual? |
| Production Efficiency | KPI Card + Line Chart | How has Production Efficiency changed over time and is the trend healthy? |
| Machine Utilization | Bullet Chart / Progress | Are we on plan for Machine Utilization? |
| Downtime | Histogram / Box Plot | What is the current level of Downtime, and how does it compare with the previous period? |
| Defect Rate | KPI Card + Sparkline | What is the current level of Defect Rate, and how does it compare with the previous period? |
| Scrap Rate | KPI Card + Sparkline | What is the current level of Scrap Rate, and how does it compare with the previous period? |
| Wastage | Stacked Bar / Donut | What is the composition of Wastage? |
| Production Cost | KPI Card + Line Chart | How has Production Cost changed over time and is the trend healthy? |
| Material Consumption | KPI Card + Line Chart | How has Material Consumption changed over time and is the trend healthy? |
| Raw Material Usage | KPI Card + Line Chart | How has Raw Material Usage changed over time and is the trend healthy? |
| Work Order Status | Stacked Bar / Donut | What is the composition of Work Order Status? |
| Production Lead Time | Histogram / Box Plot | What is the current level of Production Lead Time, and how does it compare with the previous period? |
| Capacity Utilization | Bullet Chart / Progress | Are we on plan for Capacity Utilization? |
| Maintenance Status | Stacked Bar / Donut | What is the composition of Maintenance Status? |
| Maintenance Cost | KPI Card + Line Chart | How has Maintenance Cost changed over time and is the trend healthy? |
| Production Forecast | Line with confidence band | How has Production Forecast changed over time and is the trend healthy? |

## ERP: Project / Operations
Role: Project Manager. Data: projects, tasks, timesheets (status, due_date, hours, cost, assignee_id).

| Graph | Chart | Question |
|---|---|---|
| Project Status | Stacked Bar / Donut | What is the composition of Project Status? |
| Task Status | Stacked Bar / Donut | What is the composition of Task Status? |
| Task Completion | Bullet Chart / Progress | Are we on plan for Task Completion? |
| Project Progress | Bullet Chart / Progress | Are we on plan for Project Progress? |
| Deadline Tracking | Gantt / Timeline | Is Deadline Tracking on schedule? |
| Overdue Tasks | KPI Card + Line Chart | How has Overdue Tasks changed over time and is the trend healthy? |
| Team Workload | Line Chart | How has Team Workload changed over time and is the trend healthy? |
| Resource Utilization | Bullet Chart / Progress | Are we on plan for Resource Utilization? |
| Project Cost | KPI Card + Line Chart | How has Project Cost changed over time and is the trend healthy? |
| Project Budget vs Actual | Grouped Bar | Are we on plan for Project Budget vs Actual? |
| Time Tracking | Histogram / Box Plot | What is the current level of Time Tracking, and how does it compare with the previous period? |
| Billable vs Non-Billable Hours | Grouped Bar | Are we on plan for Billable vs Non-Billable Hours? |
| Project Profitability | KPI Card + Line Chart | How has Project Profitability changed over time and is the trend healthy? |
| Milestone Progress | Gantt / Timeline | Is Milestone Progress on schedule? |
| Project Timeline | Gantt / Timeline | Is Project Timeline on schedule? |

## ERP: Logistics
Role: Logistics Manager. Data: shipments, deliveries, carriers (status, ship_date, delivered_date, cost, region).

| Graph | Chart | Question |
|---|---|---|
| Shipment Status | Stacked Bar / Donut | What is the composition of Shipment Status? |
| Delivery Status | Stacked Bar / Donut | What is the composition of Delivery Status? |
| Delivery Time | Histogram / Box Plot | What is the current level of Delivery Time, and how does it compare with the previous period? |
| Order Fulfillment | KPI Card + Line Chart | How has Order Fulfillment changed over time and is the trend healthy? |
| Pending Shipments | KPI Card + Line Chart | How has Pending Shipments changed over time and is the trend healthy? |
| Delayed Shipments | KPI Card + Line Chart | How has Delayed Shipments changed over time and is the trend healthy? |
| Delivery Success Rate | Bullet Chart / Progress | Are we on plan for Delivery Success Rate? |
| Shipping Cost | KPI Card + Line Chart | How has Shipping Cost changed over time and is the trend healthy? |
| Shipping by Region | Choropleth / Bubble Map | Where is Shipping by Region concentrated geographically? |
| Carrier Performance | Ranked Horizontal Bar | Which segments drive Carrier Performance? |
| Return Rate | KPI Card + Sparkline | What is the current level of Return Rate, and how does it compare with the previous period? |
| Average Delivery Time | Histogram / Box Plot | What is the current level of Average Delivery Time, and how does it compare with the previous period? |

## ERP: Asset Management
Role: Finance / Operations. Data: assets, depreciation, maintenance (value, category, location, purchase_date, status).

| Graph | Chart | Question |
|---|---|---|
| Asset Count | KPI Card + Sparkline | What is the current level of Asset Count, and how does it compare with the previous period? |
| Asset Value | KPI Card + Sparkline | What is the current level of Asset Value, and how does it compare with the previous period? |
| Asset by Category | Horizontal Bar | Which segments drive Asset by Category? |
| Asset by Location | Horizontal Bar | Which segments drive Asset by Location? |
| Asset Depreciation | KPI Card + Line Chart | How has Asset Depreciation changed over time and is the trend healthy? |
| Asset Lifecycle | Histogram / Box Plot | What is the current level of Asset Lifecycle, and how does it compare with the previous period? |
| Maintenance Cost | KPI Card + Line Chart | How has Maintenance Cost changed over time and is the trend healthy? |
| Asset Utilization | Bullet Chart / Progress | Are we on plan for Asset Utilization? |
| Asset Condition | KPI Card + Line Chart | How has Asset Condition changed over time and is the trend healthy? |
| Asset Replacement Forecast | Line with confidence band | How has Asset Replacement Forecast changed over time and is the trend healthy? |
