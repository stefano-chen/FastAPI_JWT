from fastapi import APIRouter, Depends, Header
from ..repositories.user_repository import get_user_repository, UserRepository
from typing import Annotated, List
from ..schemas.user_schema import UserResponseSchema, UserCreateSchema
from ..models.user_model import UserModel
from ..exceptions.user_exceptions import UserNotFoundException
from ..exceptions.auth_exceptions import NotAuthorizedException
from ..common.hash import get_password_hasher, Hasher
from ..common.headers import get_token_payload
from ..common.roles import Roles

router = APIRouter(tags=["users"])

user_repository_dependency = Annotated[UserRepository, Depends(get_user_repository)]
password_hasher_dependency = Annotated[Hasher, Depends(get_password_hasher)]

@router.get("/users")
async def get_all_users(
        user_repo: user_repository_dependency, 
        token_payload: Annotated[dict, Depends(get_token_payload)]
    ) -> List[UserResponseSchema]:

    if token_payload["role"] != Roles.ADMIN.value:
        raise NotAuthorizedException
    users = user_repo.find_all_users()
    response_users = [UserResponseSchema.from_user_model(user) for user in users]
    return response_users

@router.post("/users")
async def create_user(
        body: UserCreateSchema, 
        user_repo: user_repository_dependency,
        hasher: password_hasher_dependency
      ) -> UserResponseSchema:
    
    hashed_password = hasher.hash(body.password)
    user = UserModel(email=body.email, password=hashed_password, role=Roles(body.role))
    added_user = user_repo.add_user(user)
    return UserResponseSchema.from_user_model(added_user)

@router.get("/users/{user_ID}")
async def get_user_by_id(user_ID: int, user_repo: user_repository_dependency) -> UserResponseSchema:
    user = user_repo.find_user_by_id(user_ID)
    if not user:
        raise UserNotFoundException
    return UserResponseSchema.from_user_model(user)

@router.get("/whoami")
async def get_whoami(token_payload: Annotated[dict, Depends(get_token_payload)]):
    return UserResponseSchema.from_token_payload(token_payload)