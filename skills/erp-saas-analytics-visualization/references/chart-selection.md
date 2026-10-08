# Chart selection

| Business question | Recommended | Alternative | Avoid | Reason |
|---|---|---|---|---|
| Change over time | Line | Area | Pie | Position along time axis shows trend best |
| Compare categories | Bar / horizontal bar | Lollipop | Pie with many slices | Length is read accurately |
| Rank | Sorted horizontal bar | Table + bars | Radar | Order and labels need room |
| Part of whole (<=5 parts) | Donut / stacked 100% | Treemap | 3D pie | Shares sum to 100% |
| Many parts / hierarchy | Treemap | Sunburst | Pie | Area encodes size within hierarchy |
| Target vs actual | Bullet chart / grouped bar | Gauge | Speedometer clutter | Compare to a reference line |
| Budget variance | Waterfall | Diverging bar | Stacked pie | Shows contributions to change |
| Distribution | Histogram / box plot | Violin | Average only | Shows spread and outliers |
| Relationship | Scatter | Bubble (3rd metric) | Dual-axis line | Shows correlation and outliers |
| Funnel / conversion | Funnel | Sankey | Pie | Ordered stage drop-off |
| Retention by cohort | Cohort heatmap | Retention curves | Single average | Shows lifecycle by acquisition period |
| Flow between states | Sankey | Alluvial | Stacked bars | Shows movement |
| Schedule | Gantt | Timeline | Table only | Shows overlaps and dependencies |
| Geographic | Choropleth | Bubble map | Pie on map | Spatial pattern |
| Single KPI | KPI card + sparkline + delta | Gauge | Large chart | Fast read with context |
| Daily patterns | Calendar heatmap | Line | Stacked bar | Weekday/season patterns |
