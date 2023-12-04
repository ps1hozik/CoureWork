from schemas.product import ProductCreate, ProductUpdate
from controllers import product

from sqlalchemy.orm import Session

from fastapi import Depends
from models.database import get_db

from fastapi import APIRouter

router = APIRouter()


@router.post("/{org_id}/{w_id}", response_model=ProductCreate)
def create(org_id: int, w_id: int, data: ProductCreate, db: Session = Depends(get_db)):
    return product.create(db=db, data=data, org_id=org_id, w_id=w_id)


@router.patch("/{org_id}/{w_id}/{id}", response_model=ProductUpdate)
def update(
    org_id: int, w_id: int, id: int, data: ProductUpdate, db: Session = Depends(get_db)
):
    return product.update(db=db, data=data, id=id, org_id=org_id, w_id=w_id)


@router.get("/{org_id}/{w_id}/{id}")
def get_by_id(org_id: int, w_id: int, id: int, db: Session = Depends(get_db)):
    return product.get_by_id(db=db, id=id, org_id=org_id, w_id=w_id)


@router.get("/{org_id}/{w_id}")
def get_all(org_id: int, w_id: int, db: Session = Depends(get_db)):
    return product.get_all(db=db, org_id=org_id, w_id=w_id)
