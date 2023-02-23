from Classes.DbMongo import DbMongo

class TipoEstudiante: 
      
    def __init__(self, tipo, id = ""):
        self.tipo = tipo
        self.__id = id
        self.__collection = "Tipo_Estudiante"
        
    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id
        
    def update(self, db):
        collection = db[self.__collection]
        filterToUse = {'_id': self.__id}
        objStore = {'$set' : self.__dict__}
        collection.update_one(filterToUse, objStore)
    
    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = {'_id': self.__id}
        collection.delete_one(filterToUse)
        
    @staticmethod
    def get_list(db):
        collection = db["Tipo_Estudiante"]
        tipos = collection.find()
        
        list_tipo_estudiante = []
        for e in tipos:
            temp_tipo = TipoEstudiante(
                e["tipo"]
                , e ["_id"]
            )
            
            list_tipo_estudiante.append(temp_tipo)
        return list_tipo_estudiante
    
         
    @staticmethod
    def get_dict(db):
        collection = db["Tipo_Estudiante"]
        tipos = collection.find()
        
        dict_tipo_estudiante = {}
        for e in tipos:
            dict_tipo_estudiante[e["tipo"]] = e["_id"]
            
        return dict_tipo_estudiante
    
    @staticmethod
    def delete_all(db):
        lista_e = TipoEstudiante.get_list(db)
        for e in lista_e:
            e.delete(db)
        
        
        
        