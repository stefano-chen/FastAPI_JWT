from fastapi import APIRouter, Depends, Header
from ..schemas.auth_schema import LoginBodySchema
from typing import Annotated
from ..repositories.user_repository import get_user_repository, UserRepository
from ..common.hash import get_password_hasher, Hasher
from ..exceptions.auth_exceptions import InvalidCredentialsException, TokenMissingException, InvalidTokenException, NotRefreshTokenException
from ..exceptions.user_exceptions import UserNotFoundException
from ..common.token import get_jwt, JWT
from ..schemas.auth_schema import AccessTokenSchema, TokenResponseSchema
from ..common.headers import get_token_payload

router = APIRouter(tags=["auth"])

user_repository_dependency = Annotated[UserRepository, Depends(get_user_repository)]
password_hasher_dependency = Annotated[Hasher, Depends(get_password_hasher)]
jwt_dependency = Annotated[JWT, Depends(get_jwt)]

@router.post("/auth/token")
async def get_token(
        body: LoginBodySchema, 
        user_repo: user_repository_dependency, 
        hasher: password_hasher_dependency, 
        jwt: jwt_dependency
    ) -> TokenResponseSchema:

    user = user_repo.find_user_by_email(body.email)
    if not user:
        raise InvalidCredentialsException
    if not hasher.verify(body.password, user.password):
        raise InvalidCredentialsException
    payload = AccessTokenSchema.from_user_model(user).model_dump()
    access_token = jwt.generate_access_token(payload)
    refresh_token = jwt.generate_refresh_token(payload)
    return TokenResponseSchema(access_token=access_token, refresh_token=refresh_token, token_type="Bearer")

@router.get("/auth/refresh")
async def refresh_token(
        jwt: jwt_dependency, 
        user_repo: user_repository_dependency, 
        token_payload: Annotated[dict, Depends(get_token_payload)]
    ) -> TokenResponseSchema:
    
    if not token_payload.pop("is_refresh", False):
        raise NotRefreshTokenException
    user = user_repo.find_user_by_id(token_payload["sub"])
    if not user:
        return UserNotFoundException
    access_token = jwt.generate_access_token(token_payload)
    refresh_token = jwt.generate_refresh_token(token_payload)
    return TokenResponseSchema(access_token=access_token, refresh_token=refresh_token, token_type="Bearer")
    
