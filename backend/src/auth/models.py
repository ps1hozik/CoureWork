from typing import Optional, TYPE_CHECKING
from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

# from src.database import Base

if TYPE_CHECKING:
    from organization.models import Organization
    from warehouse.models import Warehouse
    from product.models import Product


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(128), index=True)
    login: Mapped[str] = mapped_column(String(20), unique=True)
    hashed_password: Mapped[str] = mapped_column()
    post: Mapped[str] = mapped_column(String(255), index=True)
    organization_id: Mapped[int | None] = mapped_column(ForeignKey("organizations.id"))

    organizations: Mapped["Organization"] = relationship(
        "Organization", foreign_keys=[organization_id]
    )
    # warehouses: Mapped["Warehouse"] = relationship(back_populates="users")
    products: Mapped["Product"] = relationship(back_populates="users")
    tokens: Mapped["Token"] = relationship(back_populates="users")


class Token(Base):
    __tablename__ = "tokens"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    refresh_token: Mapped[str] = mapped_column(String(450), nullable=False)
    status: Mapped[bool] = mapped_column()
    created_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    users: Mapped["User"] = relationship(back_populates="tokens")
