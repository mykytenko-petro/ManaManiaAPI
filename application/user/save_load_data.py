from typing import Any

from infrastructure import mongoDB_client
from .models import Inventory, GameData, DataPayload


async def save_game_data(
    data : DataPayload
) -> None:
    inventory: Inventory = data.inventory
    game_data: GameData = data.game_data
    
    inventory_dict: dict[str, Any] = inventory.model_dump()

    await mongoDB_client.update_document(
        collection_name="Inventory",
        filter={"email": inventory.email},
        data=inventory_dict
    )

    game_data_dict: dict[str, Any] = game_data.model_dump()

    await mongoDB_client.update_document(
        collection_name="GameData",
        filter={"email": game_data.email},
        data=game_data_dict
    )

async def load_game_data(
    email : str
):
    
    inventory_dict = await mongoDB_client.find_document(
        collection_name="Inventory",
        filter={"email": email}
    )

    game_data_dict = await mongoDB_client.find_document(
        collection_name="GameData",
        filter={"email": email}
    )

    return {
        "inventory": inventory_dict,
        "game_data": game_data_dict
    }