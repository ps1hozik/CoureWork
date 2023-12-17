from typing import Optional

from pydantic import BaseModel

from decimal import Decimal
from datetime import datetime


class ProductCreate(BaseModel):
    name: str
    manufacturer: str
    barcode: Optional[int] = None
    description: Optional[str] = None
    price: Decimal
    total_quantity: int
    booked_quantity: Optional[int] = None
    last_employee_id: int


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    barcode: Optional[int] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    total_quantity: Optional[int] = None
    booked_quantity: Optional[int] = None
    updated_at: datetime = datetime.utcnow()
    last_employee_id: int
