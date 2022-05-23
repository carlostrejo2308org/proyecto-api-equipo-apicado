import unittest
import json
from os import path
from appDB import app
from pymongo import MongoClient

class testApi(unittest.TestCase):
    def setUp(self):                    
        self.appDB = app()      # Objeto de tipo app, que nos ayudará a conectarnos a la DB

    # # Verifica atributos del objeto
    def test_appDB(self):
        MONGO_URI = 'mongodb://localhost'
        client = MongoClient(MONGO_URI)
        db = client['JsonApi']
        collection = None

        self.assertEqual(self.appDB.MONGO_URI,MONGO_URI, "Obtenido(%s) deberia ser %s" % (self.appDB.MONGO_URI,MONGO_URI))
        self.assertEqual(self.appDB.client,client, "Obtenido(%s) deberia ser %s" % (self.appDB.client,client))
        self.assertEqual(self.appDB.db,db, "Obtenido(%s) deberia ser %s" % (self.appDB.db,db))
        self.assertEqual(self.appDB.collection,collection, "Obtenido(%s) deberia ser %s" % (self.appDB.collection,collection))

    # Verifica el seteo de colección
    def test_setCollection(self):
        name = 'Game'
        self.appDB.setCollection(name)
        self.assertEqual(self.appDB.collection.name,name, "Obtenido(%s) deberia ser %s" % (self.appDB.collection.name,name))   

    #Se comprueba la funcion eliminar
    def test_eliminar(self):
        self.appDB.setCollection('Game')                  
        self.appDB.eliminar()        

        actualRegistros = self.appDB.collection.count_documents({})

        self.assertEqual(actualRegistros,0, "Obtenido(%s) deberia ser %s" % (self.appDB.collection,0))   

    #Se comprueba la funcion insertar
    def test_insertar(self):
        self.appDB.setCollection('Game')
        content = {
                'id': 3498,
                'name':"Grand Theft Auto V",
                'released' : "2013-09-17"
            }   
        
        self.appDB.insertar(content)

        consulta = self.appDB.collection.find_one({'id' : 3498})        
        consultaDicc = {
                'id': consulta['id'],
                'name': consulta['name'],
                'released' : consulta['released']
            }   
        
        content = {
                'id': 3498,
                'name':"Grand Theft Auto V",
                'released' : "2013-09-17"
            }    
        
        self.assertEqual(consultaDicc, content, "Obtenido(%s) deberia ser %s" % (consultaDicc, content))

        actualRegistros = self.appDB.collection.count_documents({})

        self.assertEqual(actualRegistros,1, "Obtenido(%s) deberia ser %s" % (actualRegistros,1))   

    #Se comprueba la funcion readAndSave
    def test_readAndSave(self):        
        self.appDB.setCollection('Game')

        content = {
                'id': 3498,
                'name':"Grand Theft Auto V",
                'released' : "2013-09-17"
            }  

        self.appDB.insertar(content)
        self.appDB.readAndSave()

        name = f"ConsultaJson/tests-apiGame.json"   

        self.assertEqual(path.exists(name),True, "Obtenido(%s) deberia ser %s" % (path.exists(name),True))   

        with open("ConsultaJson/tests-apiGame.json", 'r') as file:  
            content1 = json.load(file)       

        content = {
                'id': 3498,
                'name':"Grand Theft Auto V",
                'released' : "2013-09-17"
            }         

        self.assertEqual(content1[0],content, "Obtenido(%s) deberia ser %s" % (content1[0],content))    


if __name__ == '__main__':    
    unittest.main()     #pragma: no cover