from .organization import router


@router.get("/{organizatiom_id}/warehouse")
def get_all():
    return {"1": "1"}
