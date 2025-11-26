from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    message: str | None = None

    class Config:
        schema_extra = {"example": {"status": "ok", "message": "Service is healthy"}}
