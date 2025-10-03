from .base_model import Base
from sqlalchemy import Column, Integer, String, Enum
from common.roles import Roles
from .order_model import OrderModel
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(256), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    role = Column(Enum(Roles), nullable=False, default=Roles.USER)

    orders = relationship(OrderModel, back_populates="user")