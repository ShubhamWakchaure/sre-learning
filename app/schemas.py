from pydantic import BaseModel, EmailStr
from typing import Optional

class StudentIn(BaseModel):
    name: str
    email: EmailStr
    status: str

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    status: Optional[str] = None

class StudentOut(StudentIn):
    id: str
