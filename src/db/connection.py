import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class Connection:

    instance = None

    def __init__(self):
        self.uri = os.environ['URI_DB']
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = Connection()
        return cls.instance
    
    def get_client(self):
        return self.client