import fastapi

import infrastructure

router = fastapi.APIRouter()

@router.post("/login")
async def login():
    ...

@router.post("/mongodb_test")
async def mongodb_test(id : str):
    return infrastructure.mongoDB_client.find(
        collection_name="Users",
        filter={
            "name": "root"
        }
    )