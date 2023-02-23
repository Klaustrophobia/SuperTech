import pymongo
from Classes import Estudiantes, DbMongo
from dotenv import load_dotoenv

def main():
    estudiante = Estudiantes("Maria", "Ocon", "***-***", "****@***")
    #SU FUNCION ES GUARDAR Y ENVIAR AL MONGODB
    estudiante.save() 
    
    estudiante.update() 
    
    ## print(estudiante.__dict__)
    ## collection.insert_one(estudiante.__dict__)

if __name__ == '__main__':
    load_dotoenv()
    main()

#CAPTURA DE DATOS
## collection.insert_one({ "Nombre" : " Kevin"})

## for document in collection.find():
    ## print(document)