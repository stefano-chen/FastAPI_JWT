from pydantic import BaseModel, EmailStr, Field
from ..models.user_model import User

class UserResponseSchema(BaseModel):
    id: int
    email: str

    @classmethod
    def from_user_model(cls, user: User):
        return UserResponseSchema(id=user.id, email=user.email)
    

class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str
