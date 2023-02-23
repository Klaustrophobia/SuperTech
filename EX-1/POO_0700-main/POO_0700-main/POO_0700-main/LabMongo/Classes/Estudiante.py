from Classes.DbMongo import DbMongo

class Estudiante: 
      
    def __init__(self, nombre, apellido, numero, correo, tipo_estudiante, id = ""):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.correo = correo
        self.tipo_estudiante = tipo_estudiante
        self.__id = id
        self.__collection = "Estudiantes"
        
    ##AGREGAR UN METODO ESCRIBIR [QUE RECIBA DATOS QUE UNO INGRESA] Y LO MANDE AL MONGODB
    
    def Escribir(self):
        print("Ingrese Nombre:")
        nombre = input()
        print("Ingrese Apellido:")
        apellido = input()
        print("Ingrese numero:")
        numero = input()
        print("Ingrese correo:")
        correo = input()    
        
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
        collection = db["Estudiantes"]
        Estudiantes = collection.find()
        
        list_Estudiantes = []
        for e in Estudiantes:
            temp_Estudiantes = Estudiante(
                e["nombre"]
                , e ["apellido"]
                , e ["numero"]
                , e ["correo"]
                , e ["tipo_estudiante"]
                , e ["_id"]
            )
            
            list_Estudiantes.append(temp_Estudiantes)
        return list_Estudiantes
    
    @staticmethod
    def delete_all(db):
        lista_e = Estudiante.get_list(db)
        for e in lista_e:
            e.delete(db)
        
    @staticmethod
    def print_full_report(db):
        collection = db["Estudiante"]

        for e in collection.find():
            r = {
                "nombre": e["nombre"]
              ,"numero": e["numero"]
              ,"Tipo_estudiante": e["tipo_estudiante"] 
            }
       
            print(r)
        