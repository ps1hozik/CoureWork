from pydantic import BaseModel
from datetime import datetime

from config import SECRET_KEY


class Settings(BaseModel):
    authjwt_secret_key: str = SECRET_KEY
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_csrf_protect: bool = False


class User(BaseModel):
    name: str
    login: str
    post: str


class UserCreate(User):
    password: str


class UserLogin(BaseModel):
    login: str
    password: str


# class requestdetails(BaseModel):
#     login: str
#     password: str


# class TokenSchema(BaseModel):
#     access_token: str
#     refresh_token: str
#     name: str


# class changepassword(BaseModel):
#     login: str
#     old_password: str
#     new_password: str


# class TokenCreate(BaseModel):
#     user_id: str
#     access_token: str
#     refresh_token: str
#     status: bool
#     created_date: datetime
