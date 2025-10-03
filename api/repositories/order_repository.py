from db.connection import get_db_session
from sqlalchemy.orm import Session
from models.order_model import OrderModel
from typing import List, Union

class OrderRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find_all_orders(self) -> List[OrderModel]:
        return self.db_session.query(OrderModel).all()
    
    def add_order(self, order: OrderModel) -> OrderModel:
        with self.db_session.begin():
            self.db_session.add(order)
            self.db_session.commit()
            return order
            
    def find_order_by_id(self, id: int) -> Union[OrderModel, None]:
        return self.db_session.query(OrderModel).filter(OrderModel.id == id).first()
    
    def find_orders_by_user_id(self, user_id: str) -> List[OrderModel]:
        return self.db_session.query(OrderModel).filter(OrderModel.user_id == user_id).all()
                
    




def get_order_repository():
    db_session = next(get_db_session())
    return OrderRepository(db_session)