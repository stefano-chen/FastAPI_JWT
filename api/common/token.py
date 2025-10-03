import jwt
from typing import Dict, Any
from datetime import datetime, timezone, timedelta
from common.settings import get_settings

class JWT:
    def __init__(self, secret: str, algorithm: str, access_token_duration: int, refresh_token_duration: int):
        self._secret = secret
        self._algorithm = algorithm
        self._access_token_duration = int(access_token_duration)
        self._refresh_token_duration = int(refresh_token_duration)

    def generate_access_token(self, payload: Dict[str, Any]) -> str:
        expire_time = datetime.now(timezone.utc) + timedelta(minutes=self._access_token_duration)
        payload.update({"exp": expire_time})
        access_token = jwt.encode(payload, self._secret, self._algorithm)
        return access_token
    
    def generate_refresh_token(self, payload: Dict[str, Any]) -> str:
        payload.update({"is_refresh": True})
        expire_time = datetime.now(timezone.utc) + timedelta(minutes=self._refresh_token_duration)
        payload.update({"exp": expire_time})
        access_token = jwt.encode(payload, self._secret, self._algorithm)
        return access_token
        
    
    def verify(self, token: str) -> Dict[str, Any] | None:
        try:
            payload = jwt.decode(token, self._secret, self._algorithm, options={"require": ["exp"]})
            return payload
        except jwt.exceptions.InvalidTokenError:
            return None
        

def get_jwt():
    settings = get_settings()
    return JWT(
        secret=settings.JWT_SECRET, 
        algorithm=settings.JWT_ALGORITHM, 
        access_token_duration=settings.ACCESS_TOKEN_DURATION,
        refresh_token_duration=settings.REFRESH_TOKEN_DURATION
    )