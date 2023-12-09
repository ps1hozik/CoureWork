from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from organization.routes import router as organization_router
from warehouse.routes import router as warehouse_router
from product.routes import router as product_router

app = FastAPI()


app.include_router(
    router=organization_router,
)

app.include_router(
    router=warehouse_router,
)

app.include_router(
    router=product_router,
)

# origins = ["http://localhost:5173", "localhost:5173"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
