from fastapi import APIRouter
from api.schemas.health import HealthResponse

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", response_model=HealthResponse)
def get_health():
    """Simple health check endpoint."""
    return HealthResponse(status="ok", message="Service is healthy")
