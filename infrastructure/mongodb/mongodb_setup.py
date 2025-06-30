import os

from pymongo.mongo_client import MongoClient

from .utils import parse

class AtlasClient():
    def __init__ (self, altas_uri, dbname):
        self.mongodb_client = MongoClient(altas_uri)
        self.database = self.mongodb_client[dbname]

    def ping(self):
        self.mongodb_client.admin.command('ping')

    def get_collection(self, collection_name):
        collection = self.database[collection_name]
        return collection
    
    def find(self, collection_name, filter={}, limit=0):
        collection = self.database[collection_name]

        items = parse(
            list(
                collection.find(filter=filter, limit=limit)
            )
        )

        print("items:", items)
        return items

atlas_uri = (
    f"mongodb+srv://{os.environ['MONGODB_USER']}:{os.environ['MONGODB_PASSWORD']}"
    "@manamania.avlnl1m.mongodb.net/"
    "?retryWrites=true&w=majority&appName=ManaMania"
)

mongoDB_client = AtlasClient(
    altas_uri=atlas_uri,
    dbname="ManaManiaDB"
)