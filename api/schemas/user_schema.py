from pydantic import BaseModel
from ..models.user_model import User

class UserResponseSchema(BaseModel):
    id: int
    email: str

    @classmethod
    def from_user_model(cls, user: User):
        return UserResponseSchema(id=user.id, email=user.email)