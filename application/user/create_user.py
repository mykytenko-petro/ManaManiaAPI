import jwt

from infrastructure import mongoDB_client
from settings import app_secret
from .models import User, Inventory, GameData


async def user_auth(data : User, recursion_count = 0): 
    user = await mongoDB_client.find(
        collection_name="Users",
        filter={"email": data.email}
    )

    print("document user:", user)

    if user != []:
        return user[0]
    else:
        if not recursion_count:
            return await create_user(
                user=User(
                    email=data.email,
                    sub=data.sub
                )
            )
        else:
            return {"error": "cant find user"}

async def create_user(user : User):
    await mongoDB_client.insert_document(
        collection_name="Users",
        data=user.model_dump()
    )

    await mongoDB_client.insert_document(
        collection_name="Inventory",
        data=Inventory(
            email=user.email,
        ).model_dump()
    )

    await mongoDB_client.insert_document(
        collection_name="GameData",
        data=GameData(
            email=user.email
        ).model_dump()
    )

    return await user_auth(data=user, recursion_count=1)