from config import authjwt_exception_handler, AuthJWT
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from database import get_async_session
from models import User
from schemas import User, UserCreate


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/singin")
async def singin(
    new_user: UserCreate, session: AsyncSession = Depends(get_async_session)
):
    if select(User).where(User.c.login == new_user.login):
        raise HTTPException(
            status_code=400,
            detail=f"User {new_user.login} already exist!",
        )
    stmt = insert(User).values(**new_user.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/login")
async def login(
    user: User,
    session: AsyncSession = Depends(get_async_session),
    Authorize: authjwt_exception_handler = Depends(),
):
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=401, detail="Bad username or password")

    access_token = Authorize.create_access_token(subject=user.username)
    refresh_token = Authorize.create_refresh_token(subject=user.username)

    Authorize.set_access_cookies(access_token)
    Authorize.set_refresh_cookies(refresh_token)
    return {"msg": "Successfully login"}


@router.post("/refresh")
def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    Authorize.set_access_cookies(new_access_token)
    return {"msg": "The token has been refresh"}


@router.delete("/logout")
def logout(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    Authorize.unset_jwt_cookies()
    return {"msg": "Successfully logout"}


@router.get("/protected")
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}
