from os import remove
import json
from pymongo import MongoClient

class app:
        
    def __init__(self) -> None:
        self.MONGO_URI = 'mongodb://localhost'
        self.client = MongoClient(self.MONGO_URI)
        self.db = self.client['JsonApi']
        self.collection = None
        
    def setCollection(self,name):
        self.collection = self.db[name]

    def insertar(self, content):                           
        self.collection.insert_one(content)

    def eliminar(self):
        self.collection.delete_many({})

    def createJson(self, content):
        name = f"ConsultaJson/tests-api{self.collection.name}.json"
        remove(name)
        file = open(name, 'w')
        file.write(content)
        file.close()        

    def readAndSave(self):
        results = self.collection.find({})
        arr = []

        if self.collection == self.db["Genres"]:
            content = {"name" : "" , "games_count" : ""}
        elif self.collection == self.db["Platforms"]:
            content = {"id" : "", "name" : "" , "games_count" : ""}
        else:
            content = {"id" : "", "name" : "" , "released" : ""}

        for result in results:   
            for k in content:
                content[k] = result[k]
            #print("content",content)                  
            arr.append(content)                       

        self.createJson(json.dumps(arr, indent=2))                  



                   