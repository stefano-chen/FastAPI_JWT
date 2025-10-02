from fastapi import APIRouter, Depends
from ..repositories.user_repository import get_user_repository, UserRepository
from typing import Annotated, List
from ..schemas.user_schema import UserResponseSchema, UserCreateSchema
from ..models.user_model import User

router = APIRouter(tags=["users"])

@router.get("/users")
def get_all_users(user_repo: Annotated[UserRepository, Depends(get_user_repository)]) -> List[UserResponseSchema]:
    users = user_repo.find_all_users()
    response_users = [UserResponseSchema.from_user_model(user) for user in users]
    return response_users

@router.post("/users")
def create_user(body: UserCreateSchema, user_repo: Annotated[UserRepository, Depends(get_user_repository)]) -> UserResponseSchema:
    user = User(email=body.email, password=body.password)
    added_user = user_repo.add_user(user)
    return UserResponseSchema.from_user_model(added_user)