from typing import TYPE_CHECKING


from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


if TYPE_CHECKING:
    from organization.models import Organization
    from warehouse.models import Warehouse
    from product.models import Product
    from admin.models import Role


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(128))
    login: Mapped[str] = mapped_column(String(20), unique=True)
    hashed_password: Mapped[str] = mapped_column()
    post: Mapped[str] = mapped_column(String(255))
    organization_id: Mapped[int | None] = mapped_column(
        ForeignKey("organizations.id", ondelete="SET NULL")
    )
    warehouse_id: Mapped[int | None] = mapped_column(
        ForeignKey("warehouses.id", ondelete="SET NULL")
    )

    organizations: Mapped["Organization"] = relationship(
        "Organization",
        back_populates="users",
        foreign_keys=[organization_id],
    )
    warehouses: Mapped["Warehouse"] = relationship(
        "Warehouse",
        back_populates="users",
        foreign_keys=[warehouse_id],
    )
    products: Mapped["Product"] = relationship(back_populates="users")
    roles: Mapped["Role"] = relationship(back_populates="users")
