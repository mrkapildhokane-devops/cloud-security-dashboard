from fastapi import APIRouter

router = APIRouter(
    prefix="/aws",
    tags=["AWS"]
)

@router.get("/status")
def aws_status():
    return {
        "aws": "Not connected yet"
    }
