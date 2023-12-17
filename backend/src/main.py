from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from admin.router import router as admin_router
from manager.router import router as manager_router
from warehouse_manager.router import router as warehouse_manager_router
from auth.router import router as auth_router
from organization.router import router as organization_router
from warehouse.router import router as warehouse_router
from product.router import router as product_router

app = FastAPI()


app.include_router(
    router=admin_router,
)

app.include_router(
    router=auth_router,
)

app.include_router(
    router=manager_router,
)

app.include_router(
    router=organization_router,
)

app.include_router(
    router=warehouse_manager_router,
)

app.include_router(
    router=warehouse_router,
)

app.include_router(
    router=product_router,
)

origins = ["http://localhost:5173", "localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
