from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from models.product import Product
from schemas.product import ProductCreate, ProductUpdate


def create(db: Session, data: ProductCreate, org_id: int, w_id: int):
    if db.scalar(
        select(Product)
        .where(Product.name == data.name)
        .where(Product.manufacturer == data.manufacturer)
        .where(Product.warehouse_id == w_id)
    ):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Warehouse already has product: {data.manufacturer} {data.name}!",
        )

    product = Product(
        name=data.name,
        manufacturer=data.manufacturer,
        barcode=data.barcode,
        description=data.description,
        price=data.price,
        total_quantity=data.total_quantity,
        booked_quantity=data.booked_quantity,
        created_at=data.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        updated_at=data.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        warehouse_id=w_id,
        last_employee_id=4,
    )
    db.add(product)
    db.commit()
    return product


def update(db: Session, data: ProductUpdate, id: int, org_id: int, w_id: int):
    product = db.query(Product).filter(Product.id == id).first()
    if not product or product.warehouse_id != w_id:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Warehouse doesn't have product with id {id}!",
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
    if data.updated_at:
        product.updated_at = data.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    db.commit()
    return product


def get_by_id(db: Session, id: int, org_id: int, w_id: int):
    product = db.query(Product).filter(Product.id == id).first()

    if not product or product.warehouse_id != w_id:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Warehouse doesn't have product with id {id}!",
        )
    return product


def get_all(db: Session, org_id: int, w_id: int):
    products = db.query(Product).filter(Product.warehouse_id == w_id).all()

    if not products:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Warehouse doesn't have products!",
        )
    return products
