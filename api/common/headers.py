from typing import Dict, Any, Annotated
from fastapi import Header
from exceptions.auth_exceptions import TokenMissingException, InvalidTokenException
from common.token import JWT, get_jwt

def get_token_payload(authorization: Annotated[str | None, Header()]) -> Dict[str, Any]:
    jwt = get_jwt()
    if not authorization:
        raise TokenMissingException
    try:
        token = authorization.split(" ").pop(1)
        payload = jwt.verify(token)
        if not payload:
            raise InvalidTokenException
        return payload
    except IndexError:
        raise TokenMissingException 