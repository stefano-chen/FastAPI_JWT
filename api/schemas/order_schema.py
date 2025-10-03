from pydantic import BaseModel

class OrderCreateSchema(BaseModel):
    amount: float