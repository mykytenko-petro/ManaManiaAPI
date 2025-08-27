import os

from motor.motor_asyncio import AsyncIOMotorClient

from .utils import parse, dump
from .types import ColectionNames


class AtlasClient():
    def __init__(
            self,
            altas_uri : str,
            dbname : str = "ManaManiaDB"
        ) -> None:

        self.mongodb_client = AsyncIOMotorClient(host=altas_uri)
        self.database = self.mongodb_client[dbname]
    
    async def find(
            self,
            collection_name : ColectionNames,
            filter : dict,
            limit : int = 0
        ):

        collection = self.database[collection_name]

        items = parse(
            data=[
                item async for item in collection.find(
                    filter=filter,
                    limit=limit
                )
            ]
        )

        return items
    
    async def find_document(
            self,
            collection_name : ColectionNames,
            filter : dict
        ):
        documents = await self.find(
            collection_name=collection_name,
            filter=filter
        )
    
        return documents[0] if len(documents) > 0 else {}
    
    async def insert_document(
            self,
            collection_name : ColectionNames,
            data : dict
        ) -> None:

        await self.database[collection_name].insert_one(document=dump(data=data))

    async def update_document(
            self,
            collection_name : ColectionNames,
            filter : dict,
            data : dict
        ) -> None:

        await self.database[collection_name].update_one(
            filter=filter,
            update=dump(data=data)
        )

mongoDB_client = AtlasClient(
    altas_uri=(
        f"mongodb+srv://{os.environ['MONGODB_USER']}:{os.environ['MONGODB_PASSWORD']}"
        "@manamania.avlnl1m.mongodb.net/"
        "?retryWrites=true&w=majority&appName=ManaMania"
    )
)