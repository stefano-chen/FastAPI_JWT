from fastapi import HTTPException

class InvalidCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(401, "Invalid login credentials")