import os

import fastapi
import requests
import jwt
from google.oauth2 import id_token

from settings import app_secret
from .settings import google_request
from .types import TokenPayload

token_storage: dict[str, TokenPayload] = {}

async def google_oauth2_page_redirect(device_id : str):
    state = jwt.encode(
        payload={"device_id": device_id},
        key=app_secret,
        algorithm="HS256"
    )

    login_url = (
        "https://accounts.google.com/o/oauth2/auth"
        f"?client_id={os.environ['CLIENT_ID']}"
        f"&redirect_uri={os.environ['REDIRECT_URI']}"
        f"&state={state}"
        "&response_type=code"
        "&scope=email"
    )
    return {"url": login_url}

async def google_oauth2_parse(request : fastapi.Request):
    state_data = jwt.decode(
        jwt=request.query_params.get("state"),
        key=app_secret,
        algorithms=["HS256"]
    )

    code = request.query_params.get("code")
    if not code:
        return {"error": "Invalid authorization code"}

    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        "code": code,
        "client_id": os.environ['CLIENT_ID'],
        "client_secret": os.environ['CLIENT_SECRET'],
        "redirect_uri": os.environ['REDIRECT_URI'],
        "grant_type": "authorization_code",
    }

    token_response = requests.post(token_url, data=token_data).json()

    if "id_token" not in token_response:
        return {"error": f"Invalid token: {token_response}"}
    
    token_data = id_token.verify_oauth2_token(
        id_token=token_response["id_token"],
        request=google_request,
        audience=os.environ["CLIENT_ID"],
        clock_skew_in_seconds=5
    )
    
    token_storage[state_data["device_id"]] = token_data

    return {"message": "success!"}

async def get_id_token(device_id : str):
    id_token = token_storage.get(device_id)

    if id_token: token_storage.pop(device_id)

    if id_token:
        return {"id_token": id_token}
    else:
        return {"message": "please wait"}