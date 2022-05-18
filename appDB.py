from os import remove, path
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

    def eliminar(self):
        self.collection.delete_many({})

    def insertar(self, content):                                   
        self.collection.insert_one(content)

    def createJson(self, content):
        name = f"ConsultaJson/tests-api{self.collection.name}.json"        
        file = open(name, 'a')
        file.write(content)
        file.close()        

    def readAndSave(self):
        results = self.collection.find({})        

        if self.collection == self.db["Genres"]:
            content = {"name" : "" , "games_count" : ""}
        elif self.collection == self.db["Platforms"]:
            content = {"id" : "", "name" : "" , "games_count" : ""}
        else:
            content = {"id" : "", "name" : "" , "released" : ""}
                
        name = f"ConsultaJson/tests-api{self.collection.name}.json"
        if path.exists(name):
            remove(name)

        file = open(name, 'a')        
        file.write('[\n')
        for result in results:   
            for k in content:                
                content[k] = result[k]       

            file.write(json.dumps(content, indent = 2))            
            file.write(',\n')
        
        file.write(',,')        
        file.close()  

        self.organizarJson(name)


    def organizarJson(self, name):
        f = open(name,"r")
        lineas = f.readlines()
        f.close()
        f = open(name,"w")
        

        for i in range(len(lineas)):            
            if (i+1) < len(lineas):
                if not(lineas[i] == '},\n' and lineas[i+1] == ',,'):
                    f.write(lineas[i])

        f.write('}\n]')            
        f.close()                

