from pydantic import BaseModel, EmailStr
from ..models.user_model import UserModel
from ..common.roles import Roles
from typing import Dict, Any

class UserResponseSchema(BaseModel):
    id: int
    email: str
    role: Roles

    @classmethod
    def from_user_model(cls, user: UserModel):
        return UserResponseSchema(id=user.id, email=user.email, role=user.role)
    
    @classmethod
    def from_token_payload(cls, payload: Dict[str, Any]):
        return UserResponseSchema(id=payload["sub"], email=payload["email"], role=payload["role"])
    

class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str
    role: Roles
