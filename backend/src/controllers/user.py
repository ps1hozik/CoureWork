from datetime import datetime, timedelta
from typing import Annotated, Optional

from fastapi import Depends, FastAPI, HTTPException, status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordRequestForm
from controllers.secure import verify_password, get_password_hash, pwd_context

from sqlalchemy.orm import Session
from models.user import User
from models.token import Token

from starlette.status import HTTP_400_BAD_REQUEST
from schemas.user import UserCreate, requestdetails
from sqlalchemy import select

from .secure import create_access_token, create_refresh_token


app = FastAPI()


def create_user(db: Session, data: UserCreate):
    if db.scalar(select(User).where(User.login == data.login)):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"User {data.login} already exist!",
        )

    user = User(
        name=data.name,
        login=data.login,
        post=data.post,
        password_hash=get_password_hash(data.password),
    )
    db.add(user)
    db.commit()
    return {
        "name": user.name,
        "login": user.login,
        "post": user.post,
        "password_hash": user.password_hash,
    }


def login(request: requestdetails, db: Session):
    user = db.query(User).filter(User.login == request.login).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect login"
        )
    hashed_pass = user.password_hash
    if not verify_password(request.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password"
        )

    access = create_access_token(user.id)
    refresh = create_refresh_token(user.id)

    token_db = Token(user_id=user.id, refresh_token=refresh, status=True)
    db.add(token_db)
    db.commit()
    db.refresh(token_db)
    print({"access_token": access, "refresh_token": refresh, "name": user.name})
    return {"access_token": access, "refresh_token": refresh, "name": user.name}


# def get_by_login(db: Session, login: str):
#     user = db.query(User).filter(User.login == login).first()

#     if not user:
#         raise HTTPException(
#             status_code=HTTP_400_BAD_REQUEST,
#             detail=f"User {login} doesn't exist!",
#         )
#     return user


# def authenticate_user(db: Session, data: UserCreate):
#     user = get_by_login(db=db, login=data.username)
#     if not user:
#         return False
#     if not verify_password(data.password, user.password_hash):
#         return False
#     return user


# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         print("_" * 200)
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         login: str = payload.get("sub")
#         print("_" * 200)
#         print(f"{login=}")
#         if login is None:
#             raise credentials_exception
#         token_data = TokenData(login=login)
#     except JWTError:
#         raise credentials_exception
#     user = get_by_login(login=login)
#     if user is None:
#         raise credentials_exception
#     return user


# async def get_current_active_user(
#     current_user: Annotated[UserSchema, Depends(get_current_user)],
# ):

#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# async def login_for_access_token(data: UserCreate):
#     user = authenticate_user(db=Session, data=data)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}
