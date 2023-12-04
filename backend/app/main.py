from fastapi import FastAPI

from routers.users import router as user_router
from routers.organization import router as organization_router
from routers.warehouse import router as warehouse_router
from routers.product import router as product_router

app = FastAPI()


app.include_router(
    router=user_router,
    prefix="/user",
)

app.include_router(
    router=organization_router,
    prefix="/organization",
)

app.include_router(
    router=warehouse_router,
    prefix="/warehouse",
)

app.include_router(
    router=product_router,
    prefix="/product",
)
