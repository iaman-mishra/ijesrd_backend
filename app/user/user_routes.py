from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get("")
async def getUser():
    return {"sucess":True}

@router.post("/register")
async def register():
    return {"sucess":True}
