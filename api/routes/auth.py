from fastapi import APIRouter

router = APIRouter(tags=["auth"])

@router.get("/auth/token")
async def get_token():
    pass