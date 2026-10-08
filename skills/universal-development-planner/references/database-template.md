# Database template

For each entity:
```
Table: orders
Purpose: ...
Columns: id (uuid pk), tenant_id (fk, indexed), customer_id (fk), status (enum), total_amount (numeric(12,2)), created_at, updated_at, deleted_at (nullable)
Relations: customer 1-N orders; orders 1-N order_items
Indexes: (tenant_id, created_at), (tenant_id, status)
Constraints: total_amount >= 0; status in (...)
Notes: soft delete, audit, retention
```
Checklist: every entity maps to a feature; primary/foreign keys; unique constraints; tenant/branch scoping; money as numeric not float; timestamps in UTC; migrations versioned and reversible; seed data; ER diagram (mermaid `erDiagram`); data retention and PII classification; indexes for every frequent filter/join/sort.
