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


@router.patch("/", response_model=OrganizationUpdate)
def update():
    ...


@router.get("/{id}", response_model=OrganizationGet)
def get_by_id():
    ...
