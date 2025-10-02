from fastapi import APIRouter

router = APIRouter(tags=["users"])

@router.get("/users")
def get_all_users():
    pass