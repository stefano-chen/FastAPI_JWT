from fastapi import HTTPException

class InvalidCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(401, "Invalid login credentials")

class TokenMissingException(HTTPException):
    def __init__(self):
        super().__init__(401, "Token not Found")

class InvalidTokenException(HTTPException):
    def __init__(self):
        super().__init__(401, "Invalid Token")

class NotRefreshTokenException(HTTPException):
    def __init__(self):
        super().__init__(401, "Not a refresh token")

class NotAuthorizedException(HTTPException):
    def __init__(self):
        super().__init__(403, "Not Authorized")