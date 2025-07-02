from typing import TypedDict

class TokenPayload(TypedDict):
    sub: str
    email: str
    email_verified: bool
    iat: int
    exp: int