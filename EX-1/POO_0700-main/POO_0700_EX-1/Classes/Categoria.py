

class Categoria:
    def __init__(self, id, nombre)
        self.id = id
        self.nombre = nombre
        
        
    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id