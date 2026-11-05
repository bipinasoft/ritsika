# Ritsika
Single-seller Indian e-commerce platform scaffold.

## Stack
React + Vite + TypeScript + Ant Design (storefront/admin/seller), FastAPI, SQLAlchemy 2, Alembic, PostgreSQL, Redis, Docker Compose, Razorpay integration boundary.

## Start
1. `cp .env.example .env` (Windows: `copy .env.example .env`)
2. Change all secrets in `.env`.
3. `docker compose up --build`
4. Storefront: http://localhost:5173 | Admin: http://localhost:5174 | Seller: http://localhost:5175 | API docs: http://localhost:8000/docs

This is a production-oriented foundation, not a finished commerce platform. Follow `docs/IMPLEMENTATION_PLAN.md` before enabling live payments.
