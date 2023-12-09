from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session


router = APIRouter(
    prefix="/warehouse/{org_id}",
    tags=["Warehouse"],
)


@router.post("/")
async def create(
    org_id: int,
    # data: WarehouseCreate,
    session: AsyncSession = Depends(get_async_session),
):
    return


@router.patch("/{id}")
async def update(
    org_id: int,
    id: int,
    # data: WarehouseUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    return


@router.get("/{id}")
def get_by_id(org_id: int, id: int, session: AsyncSession = Depends(get_async_session)):
    return


@router.get("/")
def get_all(org_id: int, session: AsyncSession = Depends(get_async_session)):
    return
