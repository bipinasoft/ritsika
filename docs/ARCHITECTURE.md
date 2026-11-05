# Architecture decisions
- Modular monolith FastAPI backend; do not split into microservices prematurely.
- Three independently deployable React apps in one monorepo.
- PostgreSQL is source of truth; Redis is cache/ephemeral coordination only.
- Use Decimal and NUMERIC for money, never float.
- Orders preserve product, SKU, price, tax and address snapshots.
- Razorpay requests originate on backend; client callbacks are not authoritative.
- Webhooks use raw-body signature verification and idempotent event processing.
- Single seller is the initial operating model; seller portal is scaffolded but can remain disabled.
