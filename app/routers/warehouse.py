from schemas.warehouse import WarehouseCreate, WarehouseUpdate
from controllers import warehouse

from sqlalchemy.orm import Session

from fastapi import Depends
from models.database import get_db

from fastapi import APIRouter

router = APIRouter()


@router.post("/{org_id}", response_model=WarehouseCreate)
def create(org_id: int, data: WarehouseCreate, db: Session = Depends(get_db)):
    return warehouse.create(db=db, data=data, org_id=org_id)


@router.patch("/{org_id}/{id}", response_model=WarehouseUpdate)
def update(org_id: int, id: int, data: WarehouseUpdate, db: Session = Depends(get_db)):
    return warehouse.update(db=db, data=data, id=id, org_id=org_id)


@router.get("/{org_id}/{id}")
def get_by_id(org_id: int, id: int, db: Session = Depends(get_db)):
    return warehouse.get_by_id(db=db, id=id, org_id=org_id)


@router.get("/{org_id}")
def get_all(org_id: int, db: Session = Depends(get_db)):
    return warehouse.get_all(db=db, org_id=org_id)
