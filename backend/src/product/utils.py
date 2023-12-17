from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from admin.models import Role


async def check_role(id: int, session: AsyncSession):
    stmt = select(Role).where(Role.user_id == id)
    role: Role | None = await session.scalar(stmt)

    if not role or role.name not in [
        "Менеджер",
        "Администратор",
        "Завсклада",
        "Кладовщик",
    ]:
        raise HTTPException(
            status_code=403,
            detail={
                "status": "error",
                "data": None,
                "details": "Access allowed only for administrator, manager, warehouse manager or warehouse worker",
            },
        )
    return True
