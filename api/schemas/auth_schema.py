from pydantic import BaseModel, EmailStr
from ..models.user_model import User

class LoginBodySchema(BaseModel):
    email: EmailStr
    password: str


class AccessTokenSchema(BaseModel):
    sub: str
    email: EmailStr

    @classmethod
    def from_user_model(cls, user: User):
        return AccessTokenSchema(sub=str(user.id), email=user.email)
    
class LoginResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str