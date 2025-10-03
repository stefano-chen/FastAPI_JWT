from fastapi import APIRouter, Depends
from ..common.headers import get_token_payload
from typing import Annotated
from ..schemas.order_schema import OrderCreateSchema, OrderResponseSchema
from ..models.order_model import OrderModel
from ..repositories.order_repository import OrderRepository, get_order_repository

router = APIRouter(tags=["orders"])

order_repository_dependency = Annotated[OrderRepository, Depends(get_order_repository)]


@router.post("/orders")
async def create_order(body: OrderCreateSchema, 
                       order_repo: order_repository_dependency, 
                       payload: Annotated[dict, Depends(get_token_payload)]
                       ) -> OrderResponseSchema:
    new_order = OrderModel(amount=body.amount, user_id=payload["sub"])
    order = order_repo.add_order(new_order)
    return OrderResponseSchema.from_order_model(order)