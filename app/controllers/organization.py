from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

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


def update(code: str, db: Session, data: OrganizationUpdate):
    organization = db.query(Organization).filter(Organization.code == code).first()
    if not organization:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Organization with code {code} does not exist!",
        )

    if data.name:
        organization.name = data.name
    if data.description:
        organization.description = data.description
    if data.code:
        organization.code = data.code

    db.commit()
    return organization


def get(db: Session, code: str):
    organization = db.query(Organization).filter(Organization.code == code).first()
    if not organization:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Organization with code {code} does not exist!",
        )
    return organization
