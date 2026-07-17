from fastapi import APIRouter

router = APIRouter(
    prefix="/security",
    tags=["Security"]
)

@router.get("/alerts")
def alerts():
    return {
        "alerts": []
    }
