from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError, InvalidHashError

class Hasher:
    def __init__(self, password_hasher: PasswordHasher):
        self._password_hasher = password_hasher

    def hash(self, password: str) -> str:
        return self._password_hasher.hash(password)
    
    def verify(self, plain_password: str, hashed_password: str) -> bool:
        try:
            return self._password_hasher.verify(hashed_password, plain_password)
        except:
            return False
            

def get_password_hasher():
    password_hasher = PasswordHasher()
    return Hasher(password_hasher)

    