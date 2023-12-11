from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, delete
from database import get_async_session
from typing import List

from .models import Product
from .schemas import ProductCreate, ProductUpdate


router = APIRouter(
    prefix="/product/{w_id}",
    tags=["Product"],
)


@router.post("/")
async def create(
    w_id: int,
    data: ProductCreate,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        stmt = (
            select(Product)
            .where(Product.warehouse_id == w_id)
            .where(Product.name == data.name)
            .where(Product.manufacturer == data.manufacturer)
        )
        product: Product | None = await session.scalar(stmt)
        if product != None:
            raise ValueError
        stmt = insert(Product).values(**data.dict(), warehouse_id=w_id)
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "details": None,
        }
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "success",
                "data": None,
                "details": f"Product with name: {data.name} manufacturer: {data.manufacturer} already exist!",
            },
        )


@router.patch("/{id}")
async def update(
    w_id: int,
    id: int,
    data: ProductUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        stmt = (
            select(Product).where(Product.warehouse_id == w_id).where(Product.id == id)
        )
        product: Product | None = await session.scalar(stmt)
        if product == None:
            raise
        stmt = (
            select(Product)
            .where(Product.warehouse_id == w_id)
            .where(Product.name == data.name)
            .where(
                Product.manufacturer == data.manufacturer
                or Product.barcode == data.barcode
            )
        )
        check_product: Product | None = await session.scalar(stmt)
        if check_product != None and check_product.id != id:
            raise ValueError

        product.name = data.name
        product.manufacturer = data.manufacturer
        product.barcode = data.barcode
        product.description = data.description
        product.price = data.price
        product.total_quantity = data.total_quantity
        product.booked_quantity = data.booked_quantity
        product.updated_at = data.updated_at

        await session.commit()
        return {
            "status": "success",
            "data": product,
            "details": None,
        }
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "data": None,
                "details": f"Product with name: {data.name} and manufacturer: {data.manufacturer} or barcode: {data.barcode} already exist!",
            },
        )
    except:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "data": None,
                "details": "Warehouse or product dosen't exist",
            },
        )


@router.get("/{id}")
async def get_by_id(
    w_id: int, id: int, session: AsyncSession = Depends(get_async_session)
):
    try:
        stmt = (
            select(Product).where(Product.warehouse_id == w_id).where(Product.id == id)
        )
        product: Product | None = await session.scalar(stmt)
        if product == None:
            raise ValueError
        return {
            "status": "success",
            "data": product,
            "details": None,
        }
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "error",
                "data": None,
                "details": f"Product dosen't exist!",
            },
        )
    except:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "data": None,
                "details": None,
            },
        )


@router.get("/")
async def get_all(w_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = select(Product).where(Product.warehouse_id == w_id)
        result: Result = await session.execute(stmt)
        products: list[Product] | None = result.scalars().all()
        return {
            "status": "success",
            "data": products,
            "details": None,
        }
    except:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "data": None,
                "details": None,
            },
        )


@router.delete("/{id}", status_code=204)
async def delet_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = delete(Product).where(Product.id == id)
        result: Result = await session.execute(stmt)
        if result.rowcount == 0:
            raise ValueError
        await session.commit()
        return {"status": "success", "data": None, "details": "Successful remove"}
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "error",
                "data": None,
                "details": f"Product {id} dosen't exist!",
            },
        )
    except:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "data": None,
                "details": None,
            },
        )
