import fastapi

from infrastructure.google import (
    google_oauth2_page_redirect,
    google_oauth2_parse,
    get_id_token
)

google_auth_router = fastapi.APIRouter()

google_auth_router.add_api_route(
    path="/google_login",
    endpoint=google_oauth2_page_redirect,
    methods=["GET"]
)

google_auth_router.add_api_route(
    path="/google_login_parse",
    endpoint=google_oauth2_parse,
    methods=["GET"]
)

google_auth_router.add_api_route(
    path="/get_google_session",
    endpoint=get_id_token,
    methods=["GET"]
)