from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from main import Base
from organization import Organization


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(128), index=True)
    login: Mapped[str] = mapped_column(String(20))
    password_hash: Mapped[str] = mapped_column()
    post: Mapped[str] = mapped_column(String(255), index=True)

    children: Mapped[Organization] = relationship(back_populates="parent")
