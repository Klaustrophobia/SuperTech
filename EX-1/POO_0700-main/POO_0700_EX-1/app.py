import pymongo
from Classes import DbMongo, Categoria
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()
    
    
    client.close()

    
if __name__ == '__main__':
    load_dotenv()
    main()

    