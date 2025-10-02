from fastapi import APIRouter, Depends
from ..repositories.user_repository import get_user_repository, UserRepository
from typing import Annotated, List
from ..schemas.user_schema import UserResponseSchema, UserCreateSchema
from ..models.user_model import User
from ..exceptions.user_exceptions import UserNotFoundException

router = APIRouter(tags=["users"])

user_repository_dependency = Annotated[UserRepository, Depends(get_user_repository)]

@router.get("/users")
def get_all_users(user_repo: user_repository_dependency) -> List[UserResponseSchema]:
    users = user_repo.find_all_users()
    response_users = [UserResponseSchema.from_user_model(user) for user in users]
    return response_users

@router.post("/users")
def create_user(body: UserCreateSchema, user_repo: user_repository_dependency) -> UserResponseSchema:
    user = User(email=body.email, password=body.password)
    added_user = user_repo.add_user(user)
    return UserResponseSchema.from_user_model(added_user)

@router.get("/users/{user_ID}")
def get_user_by_id(user_ID: int, user_repo: user_repository_dependency) -> UserResponseSchema:
    user = user_repo.find_user_by_id(user_ID)
    if not user:
        raise UserNotFoundException
    return UserResponseSchema.from_user_model(user)