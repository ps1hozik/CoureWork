from typing import Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Warehouse(Base):
    __tablename__ = "warehouses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column()
    address: Mapped[str] = mapped_column()
    count_of_employees: Mapped[int] = mapped_column(default=0)
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))

    products: Mapped["Product"] = relationship()

    organization: Mapped["Organization"] = relationship()
    employee: Mapped["User"] = relationship()
