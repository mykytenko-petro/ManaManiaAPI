import fastapi

from application import user_auth

user_router = fastapi.APIRouter()

user_router.add_api_route(
    path="/user_auth",
    endpoint=user_auth,
    methods=["POST"]
)