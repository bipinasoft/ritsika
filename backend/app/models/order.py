import uuid
from decimal import Decimal
from sqlalchemy import String, ForeignKey, Numeric, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID, JSONB
from app.db.base import Base

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_number: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    status: Mapped[str] = mapped_column(String(30), default="pending_payment", nullable=False)
    currency: Mapped[str] = mapped_column(String(3), default="INR", nullable=False)
    subtotal: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    tax_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0, nullable=False)
    shipping_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0, nullable=False)
    discount_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0, nullable=False)
    total_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    shipping_address_snapshot: Mapped[dict] = mapped_column(JSONB, nullable=False)

class OrderItem(Base):
    __tablename__ = "order_items"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"))
    variant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("product_variants.id"))
    product_name_snapshot: Mapped[str] = mapped_column(String(220), nullable=False)
    sku_snapshot: Mapped[str] = mapped_column(String(80), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    tax_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0, nullable=False)

class Payment(Base):
    __tablename__ = "payments"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("orders.id"))
    gateway: Mapped[str] = mapped_column(String(30), default="razorpay", nullable=False)
    gateway_order_id: Mapped[str | None] = mapped_column(String(100), index=True)
    gateway_payment_id: Mapped[str | None] = mapped_column(String(100), unique=True)
    status: Mapped[str] = mapped_column(String(30), default="created", nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), default="INR", nullable=False)
