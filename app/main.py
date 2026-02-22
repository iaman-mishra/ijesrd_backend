from fastapi import FastAPI
from app.core.config import settings
from app.user.user_routes import router as user_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title=settings.APP_NAME , version="1.0")

app.include_router(user_router, prefix=settings.ROUTE_PREFIX)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"] )
async def read_root():
    return {"status": "ok"}

