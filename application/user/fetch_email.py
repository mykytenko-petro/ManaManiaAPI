import jwt

from settings import app_secret
from .types import EmailPayload


async def get_email(encoded_data : str) -> dict[str, str]:
    decoded_data: EmailPayload = jwt.decode(
        jwt=encoded_data,
        key=app_secret,
        algorithms=["HS256"]
    )

    return {"email": decoded_data["email"]}