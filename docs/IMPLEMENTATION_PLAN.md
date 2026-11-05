# Ritsika delivery plan

## Phase 1 — Foundation
- [x] Monorepo and three React app boundaries
- [x] Docker Compose for PostgreSQL, Redis, FastAPI and frontends
- [x] FastAPI config, health checks and initial SQLAlchemy models
- [ ] Alembic initial migration and seed roles
- [ ] CI, linting, tests and dependency scanning

## Phase 2 — Identity and access
- Customer/admin authentication, Argon2 password hashing, JWT access/refresh rotation
- RBAC for customer, admin and seller; secure cookie/CSRF design
- OTP provider adapter, expiry, attempt limits and rate limiting

## Phase 3 — Catalog and inventory
- Category/product/variant CRUD, SKU, images and attributes
- Inventory ledger and atomic stock reservation/release
- Search, filters, pagination and product administration

## Phase 4 — Shopping
- Server-authoritative cart, wishlist, addresses, shipping and coupons
- Transactional checkout and immutable order item/address snapshots
- GST/tax rules reviewed for actual products and registrations

## Phase 5 — Razorpay and orders
- Backend creates Razorpay orders using server-calculated amount
- Verify checkout signature server-side; never trust browser success alone
- Verify webhooks using raw body, persist event IDs uniquely and process idempotently
- Reconcile pending states; implement refunds and payment ledger

## Phase 6 — Admin and seller
- Admin users/catalog/orders/promotions/reports
- Seller workspace scaffold remains available but seller onboarding/payouts disabled for single-seller launch

## Phase 7 — Production hardening
- Pytest, Vitest and Playwright; security scanning and load testing
- Secrets manager, TLS reverse proxy, monitoring, backups and restore drills
- CSRF/XSS/IDOR protections, audit trails and privacy controls

## Phase 8 — Launch
- Production images, domain/HTTPS, payment live-mode drills
- Shipping, return, privacy, terms and GST/legal review

Do not enable live payments until webhook idempotency, signature verification, reconciliation, refunds and payment/order state transitions are tested. PostgreSQL and Redis must remain private.


## Current scaffold limitations
The initial migration, authentication flows, catalog CRUD, order checkout and Razorpay create/verify endpoints are not implemented yet. These are deliberate next tasks; do not treat placeholder UI or webhook route as production payment processing.
