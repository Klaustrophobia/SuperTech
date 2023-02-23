import pymongo
from Classes import Estudiante, DbMongo, TipoEstudiante
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()
    # estudiante = Estudiantes("Maria", "Ocon", "***-***", "****@***")
    
    #SU FUNCION ES GUARDAR Y ENVIAR AL MONGODB
    
    # estudiante.save(db) 
    # estudiante.apellido = "Ocon Rosales"
    
    ## print(estudiante.__dict__)
    ## collection.insert_one(estudiante.__dict__)
    
    # estudiante.update(db)
    
    # estudiante.get_list(db)
    # estudiante.delete(db)
     
    ## MUESTRA LA LISTA DE LA COLECCION ##
    # lista_estudiantes = Estudiante.get_list(db)
    # lista_estudiantes[0].delete(db) 
    
    ## ELIMINA TODA LA LISTA DE DATOS DE LA COLECCION ##
    
    Estudiante.delete_all(db)
    TipoEstudiante.delete_all(db)
    ################################
    TipoEstudiante("Primaria").save(db)
    TipoEstudiante("Secundaria").save(db)
    TipoEstudiante("Superior").save(db)
    
    ################################
    dictTipos = TipoEstudiante.get_dict(db)    
    estudiante = Estudiante("Maria", "Ocon", "***-***", "****@***", dictTipos["Superior"])
    
    Estudiante.print_full_report(db)
    #SU FUNCION ES GUARDAR Y ENVIAR AL MONGODB
    
    estudiante.save(db) 
       
    client.close()

if __name__ == '__main__':
    load_dotenv()
    main()

    #CAPTURA DE DATOS
    ## collection.insert_one({ "Nombre" : " Kevin"})

    ## for document in collection.find():
        ## print(document)