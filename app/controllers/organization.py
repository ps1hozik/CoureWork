from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from models.organization import Organization
from schemas.organization import OrganizationCreate, OrganizationUpdate, OrganizationGet


def create(db: Session, data: OrganizationCreate):
    if db.scalar(select(Organization).where(Organization.code == data.code)):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Orginization with code {data.code} already exists!",
        )

    organization = Organization(
        name=data.name, code=data.code, description=data.description
    )
    db.add(organization)
    db.commit()
    return organization
