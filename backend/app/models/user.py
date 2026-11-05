import uuid
from sqlalchemy import String, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name: Mapped[str] = mapped_column(String(160), nullable=False)
    email: Mapped[str | None] = mapped_column(String(255), unique=True, index=True)
    phone: Mapped[str | None] = mapped_column(String(20), unique=True, index=True)
    password_hash: Mapped[str | None] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    roles: Mapped[list["UserRole"]] = relationship(back_populates="user", cascade="all, delete-orphan")

class Role(Base):
    __tablename__ = "roles"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)

class UserRole(Base):
    __tablename__ = "user_roles"
    __table_args__ = (UniqueConstraint("user_id", "role_id", name="uq_user_role"),)
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    role_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship(back_populates="roles")
    role: Mapped["Role"] = relationship()
