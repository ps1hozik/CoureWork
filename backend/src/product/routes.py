from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session


router = APIRouter(
    prefix="/product/{w_id}",
    tags=["Product"],
)


@router.post("/")
def create(
    org_id: int,
    w_id: int,
    # data: ProductCreate,
    session: AsyncSession = Depends(get_async_session),
):
    return


@router.patch("/{id}")
async def update(
    org_id: int,
    w_id: int,
    id: int,
    # data: ProductUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    return


@router.get("/{id}")
async def get_by_id(
    org_id: int, w_id: int, id: int, session: AsyncSession = Depends(get_async_session)
):
    return


@router.get("/")
async def get_all(w_id: int, session: AsyncSession = Depends(get_async_session)):
    return {"w": w_id}
