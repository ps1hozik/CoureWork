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
            raise HTTPException(
                status_code=400,
                detail=f"Product with name: {data.name} manufacturer: {data.manufacturer} already exist!",
            )
        stmt = insert(Product).values(**data.dict(), warehouse_id=w_id)
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "details": None,
        }
    except IntegrityError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Warehouse with id: {w_id} dosen't exist",
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
            raise HTTPException(
                status_code=404,
                detail=f"Product dosen't exist!",
            )
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
            raise HTTPException(
                status_code=400,
                detail=f"Product with name: {data.name} and manufacturer: {data.manufacturer} or barcode: {data.barcode} already exist!",
            )
        if data.name:
            product.name = data.name
        if data.manufacturer:
            product.manufacturer = data.manufacturer
        if data.barcode:
            product.barcode = data.barcode
        if data.description:
            product.description = data.description
        if data.price:
            product.price = data.price
        if data.total_quantity:
            product.total_quantity = data.total_quantity
        if data.booked_quantity:
            product.booked_quantity = data.booked_quantity
        await session.commit()
        return product
    except IntegrityError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Warehouse with id: {w_id} dosen't exist",
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
            raise HTTPException(
                status_code=404,
                detail=f"Product dosen't exist!",
            )
        return product
    except IntegrityError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Warehouse with id: {w_id} dosen't exist",
        )


@router.get("/")
async def get_all(w_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = select(Product).where(Product.warehouse_id == w_id)
        result: Result = await session.execute(stmt)
        products: list[Product] | None = result.scalars().all()
        if not products:
            raise HTTPException(
                status_code=404,
                detail=f"Warehouse doesn't have products",
            )
        return {
            "status": "success",
            "data": products,
            "details": None,
        }
    except IntegrityError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Warehouse with id: {w_id} dosen't exist",
        )


@router.delete("/{id}", status_code=204)
async def delet_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = delete(Product).where(Product.id == id)
        result: Result = await session.execute(stmt)
        if result.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail={
                    "status": "error",
                    "data": None,
                    "details": f"Product {id} dosen't exist!",
                },
            )
        await session.commit()
        return {"status": "success", "data": None, "details": "Successful remove"}
    except IntegrityError:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "data": None,
                "details": "IntegrityError",
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
