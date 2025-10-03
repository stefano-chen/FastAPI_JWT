from api.models.user_model import UserModel
from .base_model import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

