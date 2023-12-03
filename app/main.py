from fastapi import FastAPI

from routers.users import router as user_router
from routers.organization import router as organization_router

app = FastAPI()


app.include_router(
    router=user_router,
    prefix="/user",
)

app.include_router(
    router=organization_router,
    prefix="/organization",
)
