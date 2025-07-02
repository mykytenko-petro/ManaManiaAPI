from infrastructure import mongoDB_client
from .models import User

def user_auth(data : User, recursion_count = 0): 
    user = mongoDB_client.find(
        collection_name="Users",
        filter={"email": data.email}
    )

    print("document user:", user)

    if user != []:
        return user
    else:
        if not recursion_count:
            return create_user(
                user=User(
                    email=data.email,
                    sub=data.sub
                )
            )
        else:
            return {"error": "cant find user"}

def create_user(user : User):
    mongoDB_client.insert_document(
        collection_name="Users",
        data=user.model_dump()
    )

    return user_auth(data=user, recursion_count=1)