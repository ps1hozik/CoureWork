from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from sqlalchemy.engine import Result
from database import get_async_session

from .models import Warehouse
from .schemas import WarehouseCreate, WarehouseUpdate
from auth.models import User
from warehouse_manager.utils import check_role

router = APIRouter(
    prefix="/warehouse/{org_id}",
    tags=["Warehouse"],
)


@router.post("/")
async def create(
    current_id: int,
    org_id: int,
    data: WarehouseCreate,
    session: AsyncSession = Depends(get_async_session),
):
    await check_role(current_id, session)
    stmt = (
        select(Warehouse)
        .where(Warehouse.organization_id == org_id)
        .where(Warehouse.name == data.name or Warehouse.address == data.address)
    )
    warehouse: Warehouse | None = await session.scalar(stmt)
    if warehouse != None:
        raise HTTPException(
            status_code=400,
            detail=f"Warehouse already exist!",
        )
    stmt = insert(Warehouse).values(**data.dict(), organization_id=org_id)
    await session.execute(stmt)
    await session.commit()
    stmt = (
        select(Warehouse)
        .where(Warehouse.name == data.name)
        .where(Warehouse.organization_id == org_id)
    )
    warehouse: Warehouse | None = await session.scalar(stmt)

    stmt = select(User).where(User.id == current_id)
    user: User | None = await session.scalar(stmt)
    user.warehouse_id = warehouse.id
    await session.commit()
    return {
        "status": "success",
        "data": None,
        "details": "Successful createtion",
    }


@router.patch("/{id}")
async def update(
    current_id: int,
    org_id: int,
    id: int,
    data: WarehouseUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    await check_role(current_id, session)
    stmt = (
        select(Warehouse)
        .where(Warehouse.organization_id == org_id)
        .where(Warehouse.id == id)
    )
    warehouse: Warehouse | None = await session.scalar(stmt)
    if warehouse == None:
        raise HTTPException(
            status_code=404,
            detail=f"Warehouse dosen't exist!",
        )
    stmt = (
        select(Warehouse)
        .where(Warehouse.organization_id == org_id)
        .where(Warehouse.name == data.name)
    )
    check_warehouse: Warehouse | None = await session.scalar(stmt)
    if check_warehouse != None and check_warehouse.id != id:
        raise HTTPException(
            status_code=400,
            detail=f"Warehouse with name: {data.name} or address: {data.address} already exist!",
        )
    if data.name:
        warehouse.name = data.name
    if data.address:
        warehouse.address = data.address
    if data.description:
        warehouse.description = data.description
    await session.commit()
    return {
        "status": "success",
        "data": warehouse,
        "details": None,
    }


@router.get("/{id}")
async def get_by_id(
    current_id: int,
    org_id: int,
    id: int,
    session: AsyncSession = Depends(get_async_session),
):
    await check_role(current_id, session)
    stmt = (
        select(Warehouse)
        .where(Warehouse.organization_id == org_id)
        .where(Warehouse.id == id)
    )
    warehouse: Warehouse | None = await session.scalar(stmt)
    if warehouse == None:
        raise HTTPException(
            status_code=404,
            detail=f"Warehouse dosen't exist!",
        )
    return {
        "status": "success",
        "data": warehouse,
        "details": None,
    }


@router.get("/")
async def get_all(
    current_id: int,
    org_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    await check_role(current_id, session)
    stmt = select(Warehouse).where(Warehouse.organization_id == org_id)
    result: Result = await session.execute(stmt)
    warehouses: List[Warehouse] | None = result.scalars().all()
    if warehouses == None:
        raise HTTPException(
            status_code=404,
            detail=f"Organization doesn't have warehouses",
        )
    return {
        "status": "success",
        "data": warehouses,
        "details": None,
    }
