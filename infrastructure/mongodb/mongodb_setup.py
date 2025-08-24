import os

from pymongo.mongo_client import MongoClient

from .utils import parse, dump
from .types import ColectionNames

class AtlasClient():
    def __init__(
            self,
            altas_uri : str,
            dbname : str = "ManaManiaDB"
        ):

        self.mongodb_client = MongoClient(host=altas_uri)
        self.database = self.mongodb_client[dbname]

    def get_collection(
            self,
            collection_name : ColectionNames
        ):

        collection = self.database[collection_name]
        return collection
    
    def find(
            self,
            collection_name : ColectionNames,
            filter : dict = {},
            limit : int = 0
        ):
        collection = self.database[collection_name]

        items = parse(
            data=list(
                collection.find(filter=filter, limit=limit)
            )
        )

        return items
    
    def insert_document(
            self,
            collection_name : ColectionNames,
            data : dict
        ) -> None:

        self.database[collection_name].insert_one(document=dump(data))

    def update_document(
            self,
            collection_name : ColectionNames,
            data : dict
        ): ...

mongoDB_client = AtlasClient(
    altas_uri=(
        f"mongodb+srv://{os.environ['MONGODB_USER']}:{os.environ['MONGODB_PASSWORD']}"
        "@manamania.avlnl1m.mongodb.net/"
        "?retryWrites=true&w=majority&appName=ManaMania"
    )
)