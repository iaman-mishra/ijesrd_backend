from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter(
    prefix="/users",
    tags=["User"]
)

@router.get("")
async def getUser():
    return {"sucess":True}

@router.post("/register")
async def register():
    return Response(
        status_code=200,
        
    )
