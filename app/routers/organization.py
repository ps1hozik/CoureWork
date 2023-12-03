from schemas.organization import OrganizationCreate, OrganizationUpdate, OrganizationGet
from controllers import organization

from sqlalchemy.orm import Session

from fastapi import Depends
from models.database import get_db

from fastapi import APIRouter

router = APIRouter()


@router.post("/", response_model=OrganizationCreate, status_code=201)
def create(data: OrganizationCreate, db: Session = Depends(get_db)):
    return organization.create(data=data, db=db)


@router.patch("/{code}", response_model=OrganizationUpdate)
def update(code: str, data: OrganizationUpdate, db: Session = Depends(get_db)):
    return organization.update(code=code, data=data, db=db)


@router.get("/{code}")
def get_by_code(code: str, db: Session = Depends(get_db)):
    return organization.get(db=db, code=code)
