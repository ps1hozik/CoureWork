from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

# from src.database import Base

if TYPE_CHECKING:
    from auth.models import User
    from warehouse.models import Warehouse


class Organization(Base):
    __tablename__ = "organizations"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    code: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None] = mapped_column()
    count_of_warehouses: Mapped[int] = mapped_column(default=0)
    manager_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    users: Mapped["User"] = relationship("User", foreign_keys=[manager_id])
    warehouses: Mapped["Warehouse"] = relationship(back_populates="organizations")
