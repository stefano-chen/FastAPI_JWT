from ..db.connection import get_db_session
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..models.user_model import User
from ..exceptions.user_exceptions import EmailAlreadyInUseException
from typing import List, Union

class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find_all_users(self) -> List[User]:
        return self.db_session.query(User).all()
    
    def add_user(self, user: User) -> User:
        with self.db_session.begin():
            try:
                self.db_session.add(user)
                self.db_session.commit()
                return user
            except IntegrityError:
                self.db_session.rollback()
                raise EmailAlreadyInUseException
            
    def find_user_by_id(self, id: int) -> Union[User, None]:
        return self.db_session.query(User).filter(User.id == id).first()
    
    def find_user_by_email(self, email: str) -> Union[User, None]:
        return self.db_session.query(User).filter(User.email == email).first()
                
    




def get_user_repository():
    db_session = next(get_db_session())
    return UserRepository(db_session)