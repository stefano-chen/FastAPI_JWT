from typing import Dict, Any
from ..exceptions.auth_exceptions import TokenMissingException, InvalidTokenException
from ..common.token import JWT

def get_token_payload(authorization_header: str, jwt: JWT) -> Dict[str, Any]:
    if not authorization_header:
        raise TokenMissingException
    try:
        token = authorization_header.split(" ").pop(1)
        payload = jwt.verify(token)
        if not payload:
            raise InvalidTokenException
        return payload
    except IndexError:
        raise TokenMissingException 