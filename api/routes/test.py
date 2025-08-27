import fastapi

test_router = fastapi.APIRouter()

@test_router.get(path="/")
async def test() -> dict[str, str]:
    return {"message": "test is succesful!"}