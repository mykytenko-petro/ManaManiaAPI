import fastapi

test_router = fastapi.APIRouter()

@test_router.post("/test")
async def test():
    return {"message": "test is succesful!"}