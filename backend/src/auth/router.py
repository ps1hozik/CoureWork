from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from database import get_async_session

from .utils import get_password_hash, verify_password
from .schemas import UserCreate, UserLogin
from .models import User
from admin.models import Role
from organization.models import Organization
from warehouse.models import Warehouse

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/singin", status_code=201)
async def create(data: UserCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = select(User).where(User.login == data.login)
    user: User | None = await session.scalar(stmt)
    if user != None:
        raise HTTPException(
            status_code=400,
            detail=f"User already exist!",
        )
    hashed_password = get_password_hash(data.password)
    data = data.dict()
    data.pop("password")
    stmt = insert(User).values(**data, hashed_password=hashed_password)
    await session.execute(stmt)
    await session.commit()
    return {
        "status": "success",
        "data": None,
        "details": "Successful create",
    }


@router.post("/login")
async def login(data: UserLogin, session: AsyncSession = Depends(get_async_session)):
    stmt = select(User).where(User.login == data.login)
    user: User | None = await session.scalar(stmt)
    if user == None:
        raise HTTPException(
            status_code=400,
            detail=f"User dosen't exist!",
        )
    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=404,
            detail=f"Incorrect login or password!",
        )
    query = select(Role).where(Role.user_id == user.id)
    role: Role | None = await session.scalar(query)
    return {
        "status": "success",
        "data": {
            "name": user.name,
            "id": user.id,
            "org_id": user.organization_id,
            "role": role.name,
        },
        "details": "Successful login",
    }


@router.post("/set_organization/{id}/{code}")
async def set_organization_id(
    id: int, code: str, session: AsyncSession = Depends(get_async_session)
):
    stmt = select(User).where(User.id == id)
    user: User | None = await session.scalar(stmt)
    if user == None:
        raise HTTPException(
            status_code=400,
            detail=f"User dosen't exist!",
        )
    if user.organization_id != None:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "data": None,
                "details": f"User '{id}' already has organization_id '{user.organization_id}'",
            },
        )
    query = select(Organization).where(Organization.code == code)
    organization: Organization | None = await session.scalar(query)
    if organization == None:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "data": None,
                "details": f"Organization doesn't exist!",
            },
        )
    org_id = organization.id
    user.organization_id = org_id
    await session.commit()
    return {
        "status": "success",
        "data": None,
        "details": None,
    }


@router.post("/set_warehouse/{id}/{warehouse_id}")
async def set_warehouse_id(
    id: int, warehouse_id: int, session: AsyncSession = Depends(get_async_session)
):
    stmt = select(User).where(User.id == id)
    user: User | None = await session.scalar(stmt)
    if user == None:
        raise HTTPException(
            status_code=400,
            detail=f"User dosen't exist!",
        )
    if user.warehouse_id != None:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "data": None,
                "details": f"User '{id}' already has warehouse_id '{user.warehouse_id}'",
            },
        )
    query = select(Warehouse).where(Warehouse.id == warehouse_id)
    warehouse: Warehouse | None = await session.scalar(query)
    if warehouse == None:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "data": None,
                "details": f"Warehouse doesn't exist!",
            },
        )
    user.warehouse_id = warehouse_id
    await session.commit()
    return {
        "status": "success",
        "data": None,
        "details": None,
    }
