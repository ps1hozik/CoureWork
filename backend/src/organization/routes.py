from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session

import organization.schemas as schemas


router = APIRouter(
    prefix="/organization",
    tags=["Organization"],
)


@router.post("/")
async def create(
    data: schemas.Create,
    session: AsyncSession = Depends(get_async_session),
):
    return


@router.patch(
    "/{id}",
)
async def update(
    id: str,
    data: schemas.Update,
    session: AsyncSession = Depends(get_async_session),
):
    return


@router.get("/{id}")
async def get(id: str, session: AsyncSession = Depends(get_async_session)):
    return
