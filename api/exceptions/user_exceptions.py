from fastapi import HTTPException

class EmailAlreadyInUseException(HTTPException):
    def __init__(self):
        super().__init__(422, "Email already in use")