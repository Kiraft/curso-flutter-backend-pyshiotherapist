from ...mongo.connect import ConnectionMongo

class MongodUser:
    def __init__(self):
        self.connect = ConnectionMongo()

    def user_connect(self, user, pasw):
        db = self.connect.con
        col = db["users"]

        raw = col.find_one({"username": user, "password": pasw, "state": True}, {'_id': False, 'state': False, 'role': False})
        return raw

