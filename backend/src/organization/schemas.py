from typing import Optional

from pydantic import BaseModel


class OrganizationCreate(BaseModel):
    name: str
    code: str
    description: Optional[str] = None


class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
