from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    code: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]] = mapped_column()
    count_of_warehouses: Mapped[int] = mapped_column(default=0)
    manager_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))

    warehouses: Mapped["Warehouse"] = relationship()
    manager: Mapped["User"] = relationship()
