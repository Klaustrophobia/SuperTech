from Classes.DbMongo import DbMongo

class Estudiantes: 
      
    def __init__(self, nombre, apellido, numero, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.correo = correo
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
        
    def save(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        client.close()

    def update(self):
        myquery = {"Nombre": {"$regex" :"^C"}}
        NValue = {"$set": {"Nombre": "Alejandra"}}
        collection = ['Estudiantes']
        collection.update_one(myquery, NValue)        

        for x in collection.find():
            print(x)