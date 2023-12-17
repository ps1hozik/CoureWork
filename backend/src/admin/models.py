from typing import TYPE_CHECKING


from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

if TYPE_CHECKING:
    from auth.models import User


class Role(Base):
    __tablename__ = "roles"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(128), index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    users: Mapped["User"] = relationship(back_populates="roles")
