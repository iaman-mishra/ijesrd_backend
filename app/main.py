from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.user.user_routes import router as user_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title=settings.APP_NAME, version="1.0")

app.include_router(user_router, prefix=settings.ROUTE_PREFIX)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# GLobal Custom Errors
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail,
        },
    )


# GLobal Handler System Errors
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error",
            "error": str(exc) if settings.DEBUG else None,
        },
    )


@app.get("/", tags=["Health"])
async def read_root():
    return {"status": "ok"}
