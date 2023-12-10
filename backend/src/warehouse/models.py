from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

# from src.database import Base

if TYPE_CHECKING:
    from ..auth.models import User
    from ..organization.models import Organization
    from ..product.models import Product


class Warehouse(Base):
    __tablename__ = "warehouses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column()
    address: Mapped[str] = mapped_column()
    count_of_employees: Mapped[int] = mapped_column(default=0)
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))

    products: Mapped["Product"] = relationship(back_populates="warehouses")
    organizations: Mapped["Organization"] = relationship(back_populates="warehouses")
    users: Mapped["User"] = relationship(back_populates="warehouses")
