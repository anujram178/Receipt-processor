import uuid

class Database:

    def __init__(self):
        self._store = {}
    
    def add(self, data):
        """Add data to db and return uuid"""
        # generate a UUID
        newId = uuid.uuid4()
        newIdString = str(newId)
        self._store[newIdString] = data
        return newIdString

    def get(self, id):
        """Return receipt associated with id. Return none if id is invalid"""
        return self._store.get(id, None)

    def get_all(self):
        """Retrieve all records"""
        return self._store

    def delete(self, id):
        """Delete data associated with id if it exists.
        Returns boolean to indicate if record was deleted or not"""
        if id in self._store:
            self._store.pop(id)
            return True
        return False

