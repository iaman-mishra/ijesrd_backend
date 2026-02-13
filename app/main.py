from fastapi import FastAPI

app = FastAPI(openapi_prefix="api/v1")


@app.get("/")
async def root():
    return {"Status": "Ok"}