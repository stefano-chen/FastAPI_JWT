from pydantic import BaseModel, EmailStr
from models.user_model import UserModel
from common.roles import Roles
from typing import Dict, Any, List, Optional

class UserSchema(BaseModel):
    id: int
    email: str
    role: Roles

class UserResponseSchema(UserSchema):
    @classmethod
    def from_user_model(cls, user: UserModel):
        return UserResponseSchema(
            id=user.id,
            email=user.email, 
            role=user.role
        )
    
    @classmethod
    def from_token_payload(cls, payload: Dict[str, Any]):
        return UserResponseSchema(id=payload["sub"], email=payload["email"], role=payload["role"])


class UserWithOrdersResponseSchema(UserSchema):
    orders: List[int]

    @classmethod
    def from_user_model(cls, user: UserModel):
        orders = [order.id for order in user.orders]
        return UserWithOrdersResponseSchema(
            id=user.id,
            email=user.email, 
            role=user.role, 
            orders=orders
        )
    

class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str
    role: Roles
