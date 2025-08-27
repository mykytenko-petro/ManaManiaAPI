from datetime import datetime

from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    email: str

class User(BaseSchema):
    sub: str
    created_at: datetime = Field(default_factory=datetime.now)

class Inventory(BaseSchema):
    inventory_size: int = 3
    inventory: list = Field(default_factory=list)

class GameData(BaseSchema):
    last_location: str = "DesertHub"
    coin: int = 0

class DataPayload(BaseModel):
    inventory: Inventory
    game_data: GameData