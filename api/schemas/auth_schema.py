from pydantic import BaseModel, EmailStr
from models.user_model import UserModel
from common.roles import Roles

class LoginBodySchema(BaseModel):
    email: EmailStr
    password: str


class AccessTokenSchema(BaseModel):
    sub: str
    email: EmailStr
    role: Roles

    @classmethod
    def from_user_model(cls, user: UserModel):
        return AccessTokenSchema(sub=str(user.id), email=user.email, role=user.role)
    
class TokenResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str