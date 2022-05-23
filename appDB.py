from os import remove, path
import json
from pymongo import MongoClient

class app:
        
    # Se establecen los elementos para realizar una conección con Mongo como atributos de la clase
    # collection se inicializa cono None, debido a que se utilizarán diferentes colecciones
    def __init__(self) -> None:
        self.MONGO_URI = 'mongodb://localhost'
        self.client = MongoClient(self.MONGO_URI)
        self.db = self.client['JsonApi']
        self.collection = None
        
    # Cambia el nombre de la colección        
    def setCollection(self,name):
        self.collection = self.db[name]

    # Elimina todos los registros de una colección
    def eliminar(self):
        self.collection.delete_many({})

    # Inserta un solo registro a la colección
    def insertar(self, content):                                   
        self.collection.insert_one(content)
       
    # Lee los registros de una colección y los guarda en un archivo .json
    def readAndSave(self):
        # Guarda los registros en una variable tipo puntero
        results = self.collection.find({})        

        # Se establece el tipo de formato que se usara para guardar, segpun el  tipo de colección
        # esto de hace debido a que no queremos guardar el "_id"
        if self.collection == self.db["Genres"]:
            content = {"name" : "" , "games_count" : ""}
        elif self.collection == self.db["Platforms"]:
            content = {"id" : "", "name" : "" , "games_count" : ""}
        else:
            content = {"id" : "", "name" : "" , "released" : ""}
           
        # Nombre del archivo a guardar los registros        
        name = f"ConsultaJson/tests-api{self.collection.name}.json"
        
        # Si dicho archivo existe, se elimina
        if path.exists(name):
            remove(name)

        # Abre/crea el archivo
        file = open(name, 'a')        
        file.write('[\n')

        # Se itera en los registros
        for result in results:   
            # Ahora se crea la estructura de los elementos a guardar
            for k in content:                
                content[k] = result[k]       

            file.write(json.dumps(content, indent = 2))     # Una vez que este completo se guarda
            file.write(',\n')
        
        file.write(',,')        
        file.close()        # Se cierra el archivo

        self.organizarJson(name)

    # Hace un cambio al archivo para que la sintaxis sea correcta
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