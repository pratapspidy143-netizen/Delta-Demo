from fastapi import FastAPI
from api.routers.health import router as health_router

app = FastAPI(title="Demo Backend Template", version="0.1.0")

app.include_router(health_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:main", host="0.0.0.0", port=8000, reload=True)
