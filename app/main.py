from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.APP_NAME , openapi_prefix="/api", version="1.0")


@app.get("/", tags=["Health"])
async def read_root():
    return {"status": "ok"}
