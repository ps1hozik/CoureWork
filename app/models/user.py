from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(128), index=True)
    login: Mapped[str] = mapped_column(String(20))
    password_hash: Mapped[str] = mapped_column()
    post: Mapped[str] = mapped_column(String(255), index=True)

    organizations: Mapped["Organization"] = relationship()
    warehouses: Mapped["Warehouse"] = relationship()
    products: Mapped["Product"] = relationship()
