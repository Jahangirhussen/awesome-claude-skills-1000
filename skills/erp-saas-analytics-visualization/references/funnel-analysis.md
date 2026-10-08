# Funnel Analysis

Open only the module section needed. IDs are in `../GRAPH-REGISTRY.md`.

## SaaS: Funnel
Role: Growth / Marketing. Data: visitors, signups, activations, trials, subscriptions (stage, timestamp).

| Graph | Chart | Question |
|---|---|---|
| Visitor to Signup | Funnel Chart | Where do we lose people/value in Visitor to Signup? |
| Signup to Activation | Funnel Chart | Where do we lose people/value in Signup to Activation? |
| Activation to Trial | Funnel Chart | Where do we lose people/value in Activation to Trial? |
| Trial to Paid | Funnel Chart | Where do we lose people/value in Trial to Paid? |
| Paid to Retained | Funnel Chart | Where do we lose people/value in Paid to Retained? |
| Lead to Customer | Funnel Chart | Where do we lose people/value in Lead to Customer? |
| Demo to Trial | Funnel Chart | Where do we lose people/value in Demo to Trial? |
| Demo to Paid | Funnel Chart | Where do we lose people/value in Demo to Paid? |

## Method
1. Define ordered stages with one event each and a conversion window (e.g. signup -> activation within 7 days).
2. Count unique users reaching each stage within the window; step conversion = stage n / stage n-1; overall = last / first.
3. Chart: funnel (horizontal, labels with count and step %); compare periods or segments side by side; avoid 3D.
4. Diagnose: biggest absolute drop vs biggest relative drop; segment by channel, device, plan; add time-to-convert distribution.
5. Pitfalls: counting events instead of users, stages out of order, mixing windows, ignoring bots/internal users.
