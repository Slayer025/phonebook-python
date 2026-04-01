from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime
import re

class ContactCreate(BaseModel):
    name: str
    phone_number: str
    email: Optional[EmailStr] = None
    address: Optional[str] = None

    # ✅ Name validation (no numbers only)
    @field_validator("name")
    def validate_name(cls, value):
        if not re.match(r"^[A-Za-z\s]+$", value):
            raise ValueError("Name must contain only letters")
        return value

    # ✅ Phone validation (basic)
    @field_validator("phone_number")
    def validate_phone(cls, value):
        if not re.match(r"^\+?\d{10,15}$", value):
            raise ValueError("Invalid phone number format")
        return value


class ContactResponse(ContactCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True