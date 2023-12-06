from typing import Annotated
from schemas.organization import OrganizationCreate, OrganizationUpdate
from controllers import organization

from sqlalchemy.orm import Session

from fastapi import Depends
from models.database import get_db

from schemas.user import oauth2_scheme

from fastapi import APIRouter

router = APIRouter()


@router.post("/", response_model=OrganizationCreate, status_code=201)
async def create(
    token: Annotated[str, Depends(oauth2_scheme)],
    data: OrganizationCreate,
    db: Session = Depends(get_db),
):
    return organization.create(
        data=data,
        db=db,
    )


@router.patch("/{code}", response_model=OrganizationUpdate)
async def update(code: str, data: OrganizationUpdate, db: Session = Depends(get_db)):
    return organization.update(code=code, data=data, db=db)


@router.get("/{code}")
async def get_by_code(code: str, db: Session = Depends(get_db)):
    return organization.get(db=db, code=code)
