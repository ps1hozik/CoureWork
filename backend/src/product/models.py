from typing import TYPE_CHECKING
from decimal import Decimal
from datetime import datetime

from sqlalchemy import String, Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

# from src.database import Base

if TYPE_CHECKING:
    from ..auth.models import User
    from ..warehouse.models import Warehouse


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    manufacturer: Mapped[str] = mapped_column(String(255))
    barcode: Mapped[int | None] = mapped_column(Integer())
    description: Mapped[str | None] = mapped_column()
    price: Mapped[Decimal] = mapped_column()
    total_quantity: Mapped[int] = mapped_column()
    booked_quantity: Mapped[int | None] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    last_employee_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
    warehouse_id: Mapped[int] = mapped_column(ForeignKey("warehouses.id"))

    warehouses: Mapped["Warehouse"] = relationship(back_populates="products")
    users: Mapped["User"] = relationship(back_populates="products")
