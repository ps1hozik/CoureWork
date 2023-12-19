from fastapi import Depends, APIRouter, HTTPException
from typing import List, Tuple, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import outerjoin
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
    stmt = select(User, Role.name.label("role_name")).where(User.id == id)
    stmt = stmt.outerjoin(Role, Role.user_id == User.id)
    result = await session.execute(stmt)
    user_role = result.fetchone()
    if user_role == None:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "error",
                "data": None,
                "details": f"User {id} dosen't exist!",
            },
        )
    user, role_name = user_role
    user_dict = {
        "id": user.id,
        "name": user.name,
        "login": user.login,
        "post": user.post,
        "organization_id": user.organization_id if user.organization_id else "null",
        "warehouse_id": user.warehouse_id if user.warehouse_id else "null",
        "role_name": role_name if role_name else "null",
    }
    return {
        "status": "success",
        "data": user_dict,
        "details": None,
    }


@router.get("/")
async def get_all_users(
    current_id: int, session: AsyncSession = Depends(get_async_session)
):
    await check_role(current_id, session)
    stmt = select(User, Role.name.label("role_name"))
    stmt = stmt.outerjoin(Role, Role.user_id == User.id)
    users = await session.execute(stmt)
    if users == None:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "error",
                "data": None,
                "details": "Users dosen't exist!",
            },
        )
    user_dicts = []
    for user, role_name in users:
        user_dict = {
            "id": user.id,
            "name": user.name,
            "login": user.login,
            "post": user.post,
            "organization_id": user.organization_id if user.organization_id else "null",
            "warehouse_id": user.warehouse_id if user.warehouse_id else "null",
            "role_name": role_name if role_name else "null",
        }
        user_dicts.append(user_dict)
    return {
        "status": "success",
        "data": {"users": user_dicts, "roles": roles},
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
