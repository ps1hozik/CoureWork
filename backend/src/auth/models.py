from typing import Optional
from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(128), index=True)
    login: Mapped[str] = mapped_column(String(20), unique=True)
    hashed_password: Mapped[str] = mapped_column()
    post: Mapped[str] = mapped_column(String(255), index=True)
    warehouse_id: Mapped[Optional[int]] = mapped_column(ForeignKey("warehouses.id"))

    organizations: Mapped["Organization"] = relationship()
    warehouses: Mapped["Warehouse"] = relationship()
    products: Mapped["Product"] = relationship()
    token: Mapped["Token"] = relationship()


class Token(Base):
    __tablename__ = "tokens"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    refresh_token: Mapped[str] = mapped_column(String(450), nullable=False)
    status: Mapped[bool] = mapped_column()
    created_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    user: Mapped["User"] = relationship()
