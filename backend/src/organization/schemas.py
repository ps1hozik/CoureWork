from typing import Optional

from pydantic import BaseModel


class Create(BaseModel):
    name: str
    code: str
    description: Optional[str] = None


class Update(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
