from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def create():
    ...


@router.patch("/")
def update():
    ...


@router.get("/{id}")
def get_by_id():
    ...
