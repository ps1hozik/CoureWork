from decimal import Decimal
from datetime import datetime

from sqlalchemy import String, Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    manufacturer: Mapped[str] = mapped_column(String(255))
    barcode: Mapped[int | None] = mapped_column(Integer())
    description: Mapped[str | None] = mapped_column()
    price: Mapped[Decimal] = mapped_column(Numeric(precision=2))
    total_quantity: Mapped[int] = mapped_column()
    booked_quantity: Mapped[int | None] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    last_employee_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
    warehouse_id: Mapped[int] = mapped_column(ForeignKey("warehouses.id"))

    warehouse: Mapped["Warehouse"] = relationship()
    last_employee: Mapped["User"] = relationship()
