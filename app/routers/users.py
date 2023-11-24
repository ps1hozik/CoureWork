from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_user():
    pass


@router.get("/{user_id}")
def get_user_by_id(user_id: int):
    return {"i": "h"}
