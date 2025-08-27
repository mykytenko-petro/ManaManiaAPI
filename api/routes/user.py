import fastapi

from application import (
    user_auth,
    save_game_data,
    load_game_data,
    get_email
)


user_router = fastapi.APIRouter()

user_router.add_api_route(
    path="/get_email",
    endpoint=get_email,
    methods=["GET"]
)

user_router.add_api_route(
    path="/user_auth",
    endpoint=user_auth,
    methods=["POST"]
)

user_router.add_api_route(
    path="/save_game_data",
    endpoint=save_game_data,
    methods=["POST"]
)

user_router.add_api_route(
    path="/load_game_data",
    endpoint=load_game_data,
    methods=["GET"]
)