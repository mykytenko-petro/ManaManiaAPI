import pydantic

class User(pydantic.BaseModel):
    email: str
    sub: str