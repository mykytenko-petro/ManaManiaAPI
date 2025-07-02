import fastapi

test_router = fastapi.APIRouter()

@test_router.get("/test")
async def test():
    return {"message": "test is succesful!"}