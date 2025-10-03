from pydantic import BaseModel, EmailStr
from ..models.order_model import OrderModel

class OrderCreateSchema(BaseModel):
    amount: float

class OrderResponseSchema(BaseModel):
    id: int
    amount: float
    user_id: int
    user_email: EmailStr

    @classmethod
    def from_order_model(cls, order: OrderModel):
        return OrderResponseSchema(id=order.id, amount=order.amount, user_id=order.user_id, user_email=order.user.email)