from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class ContactCreate(BaseModel):
    name: str
    phone_number: str
    email: Optional[EmailStr] = None
    address: Optional[str] = None

class ContactResponse(ContactCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True