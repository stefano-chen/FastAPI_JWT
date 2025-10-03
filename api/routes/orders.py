from fastapi import APIRouter, Depends
from ..common.headers import get_token_payload
from typing import Annotated
from ..schemas.order_schema import OrderCreateSchema

router = APIRouter(tags=["orders"])

@router.post("/orders")
async def create_order(body: OrderCreateSchema, payload: Annotated[dict, Depends(get_token_payload)]):
    pass