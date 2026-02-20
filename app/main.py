from fastapi import FastAPI
from core.config import settings
from app.user.user_routes import router as user_router

app = FastAPI(title=settings.APP_NAME , version="1.0")

app.include_router(user_router, prefix=settings.ROUTE_PREFIX)


@app.get("/", tags=["Health"] )
async def read_root():
    return {"status": "ok"}

