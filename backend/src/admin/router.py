from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import insert, select, delete
from database import get_async_session

from .utils import check_role
from auth.models import User
from .models import Role
from .config import roles

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.get("/{id}")
async def get_user(
    id: int, current_id: int, session: AsyncSession = Depends(get_async_session)
):
    await check_role(current_id, session)
    stmt = select(User).where(User.id == id)
    user: User | None = await session.scalar(stmt)
    if user == None:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "error",
                "data": None,
                "details": f"User {id} dosen't exist!",
            },
        )
    return {
        "status": "success",
        "data": user,
        "details": None,
    }


@router.get("/")
async def get_all_users(
    current_id: int, session: AsyncSession = Depends(get_async_session)
):
    await check_role(current_id, session)
    stmt = select(User)
    users: List[User] | None = await session.scalars(stmt)
    if users == None:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "error",
                "data": None,
                "details": "Users dosen't exist!",
            },
        )
    return {
        "status": "success",
        "data": users.all(),
        "details": None,
    }


@router.post("/role/{id}")
async def set_role(
    id: int,
    current_id: int,
    role_num: int,
    session: AsyncSession = Depends(get_async_session),
):
    await check_role(current_id, session)
    if role_num not in roles.keys():
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "data": None,
                "details": f"Please write correct role num: {roles}",
            },
        )
    stmt = select(Role).where(Role.user_id == id)
    user_role: Role | None = await session.scalar(stmt)
    if user_role != None:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "data": None,
                "details": f"User {id} already has role: '{user_role.name}'",
            },
        )
    stmt = insert(Role).values(user_id=id, name=roles[role_num])
    result: Result = await session.execute(stmt)
    await session.commit()
    return {
        "status": "success",
        "data": None,
        "details": f"User {id} now '{roles[role_num]}'",
    }


@router.delete("/role/{id}")
async def delete_role(
    id: int,
    current_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    await check_role(current_id, session)
    if id == current_id:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "data": None,
                "details": f"You cannot delete your role!",
            },
        )
    stmt = select(Role).where(Role.user_id == id)
    user_role: Role | None = await session.scalar(stmt)
    if user_role == None:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "data": None,
                "details": f"User {id} does not have a role!",
            },
        )
    stmt = delete(Role).where(Role.user_id == id)
    result: Result = await session.execute(stmt)
    await session.commit()
    return {
        "status": "success",
        "data": None,
        "details": "Successful remove",
    }
