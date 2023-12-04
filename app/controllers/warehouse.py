from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from models.warehouse import Warehouse
from schemas.warehouse import WarehouseCreate, WarehouseUpdate


def create(db: Session, data: WarehouseCreate, org_id: int):
    if db.scalar(
        select(Warehouse)
        .where(Warehouse.organization_id == org_id)
        .where(Warehouse.address == data.address)
    ):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Orginization already has warehouse with address: {data.address}!",
        )

    warehouse = Warehouse(
        name=data.name,
        description=data.description,
        address=data.address,
        organization_id=org_id,
    )
    db.add(warehouse)
    db.commit()
    return warehouse


def update(db: Session, data: WarehouseUpdate, id: int, org_id: int):
    warehouse = db.query(Warehouse).filter(Warehouse.id == id).first()
    if not warehouse or warehouse.organization_id != org_id:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Organization doesn't have warehouse with id {id}!",
        )

    if data.name:
        warehouse.name = data.name
    if data.description:
        warehouse.description = data.description
    if data.address:
        warehouse.address = data.address

    db.commit()
    return warehouse


def get_by_id(db: Session, id: int, org_id: int):
    warehouse = db.query(Warehouse).filter(Warehouse.id == id).first()

    if not warehouse or warehouse.organization_id != org_id:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Organization doesn't have warehouse with id {id}!",
        )
    return warehouse


def get_all(db: Session, org_id: int):
    warehouse = db.query(Warehouse).filter(Warehouse.organization_id == org_id).all()
    if not warehouse:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Organization doesn't have warehouses!",
        )
    return warehouse
