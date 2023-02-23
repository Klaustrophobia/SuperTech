
import pymongo
import os

class DbMongo:
    
    #@staticmethod = DECORADOR => QUE TIPO DE ESTRUCTURA VA A TENER EL SIGUIENTE METODO QUE SE VA A DEFINIR 
    
    @staticmethod
    def getDB():
        user = os.environ['USER']
        password = os.environ['PASSWDORD']
        cluster = os.environ['CLUSTER']
        query_string = "retryWrites=true&w=majority"

        ## CONNECTION STRING
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
        user 
        , password
        , cluster 
        , query_string
        )

        client = pymongo.MongoClient(uri)
        print(uri) 
        db = client[os.environ['DB']]
        
        #SU FUNCION ES RETORNAR EN LA DB LO CUAL ENVIA AL APP.pY
        return client, db
    
    
    
    
    