import uuid
from decimal import Decimal
from sqlalchemy import String, Boolean, ForeignKey, Numeric, Integer, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID, JSONB
from app.db.base import Base

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    slug: Mapped[str] = mapped_column(String(140), unique=True, index=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

class Product(Base):
    __tablename__ = "products"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("categories.id", ondelete="SET NULL"))
    name: Mapped[str] = mapped_column(String(220), nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String(240), unique=True, index=True)
    description: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(24), default="draft", nullable=False)
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    variants: Mapped[list["ProductVariant"]] = relationship(back_populates="product", cascade="all, delete-orphan")

class ProductVariant(Base):
    __tablename__ = "product_variants"
    __table_args__ = (UniqueConstraint("sku", name="uq_product_variant_sku"),)
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"))
    sku: Mapped[str] = mapped_column(String(80), nullable=False, index=True)
    attributes: Mapped[dict] = mapped_column(JSONB, default=dict, nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    compare_at_price: Mapped[Decimal | None] = mapped_column(Numeric(12, 2))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    product: Mapped["Product"] = relationship(back_populates="variants")
    inventory: Mapped["Inventory | None"] = relationship(back_populates="variant", uselist=False, cascade="all, delete-orphan")

class Inventory(Base):
    __tablename__ = "inventory"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    variant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("product_variants.id", ondelete="CASCADE"), unique=True)
    available_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    reserved_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    variant: Mapped["ProductVariant"] = relationship(back_populates="inventory")
