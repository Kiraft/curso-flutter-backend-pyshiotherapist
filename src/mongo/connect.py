from pymongo import MongoClient


class ConnectionMongo:

    def __init__(self):
        #_ NAME DB
        db = "app"

        connection: MongoClient = MongoClient('mongodb://localhost:27017', uuidRepresentation='standard')
        self.con = connection[db]

