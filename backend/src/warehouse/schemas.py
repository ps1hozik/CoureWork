from typing import Optional

from pydantic import BaseModel


class WarehouseCreate(BaseModel):
    name: str
    description: Optional[str] = None
    address: str


class WarehouseUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
