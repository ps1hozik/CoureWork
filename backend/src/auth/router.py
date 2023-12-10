from fastapi import Depends, APIRouter, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from database import get_async_session

from .utils import get_password_hash, verify_password
from .schemas import UserCreate, UserLogin
from .models import User

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/singin", status_code=201)
async def create(data: UserCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = select(User).where(User.login == data.login)
    user: User | None = await session.scalar(stmt)
    if user != None:
        raise HTTPException(
            status_code=400,
            detail=f"User already exist!",
        )
    hashed_password = get_password_hash(data.password)
    data = data.dict()
    data.pop("password")
    stmt = insert(User).values(**data, hashed_password=hashed_password)
    await session.execute(stmt)
    await session.commit()
    return {"message": "Successful creation"}


@router.post("/login")
async def login(data: UserLogin, session: AsyncSession = Depends(get_async_session)):
    stmt = select(User).where(User.login == data.login)
    user: User | None = await session.scalar(stmt)
    if user == None:
        raise HTTPException(
            status_code=400,
            detail=f"User dosen't exist!",
        )
    if verify_password(data.password, user.hashed_password):
        return {"status": "success", "data": user.name, "details": "Successful remove"}
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Uncorrect login or passeord!",
        )


@router.get("/{id}")
async def get(id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = select(User).where(User.id == id)
    user: User | None = await session.scalar(stmt)
    if user == None:
        raise HTTPException(
            status_code=404,
            detail=f"User {id} dosen't exist!",
        )
    return user
