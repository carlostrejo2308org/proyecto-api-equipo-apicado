import unittest
import json
from api import api
from unittest import mock

class testApi(unittest.TestCase):
    def setUp(self):        
        api_key = '?key=9a1c16878d8c4ad39ce142b6fcff8340&1'
        api_game = ('https://api.rawg.io/api/')    
        self.newApi = api(api_game, api_key)    # Crea objeto de tipo api

    # Verifica atributos del objeto
    def testNewApi(self):
        api_key = '?key=9a1c16878d8c4ad39ce142b6fcff8340&1'
        api_game = ('https://api.rawg.io/api/')  

        self.assertEqual(self.newApi.key,api_key, "Obtenido(%s) deberia ser %s" % (self.newApi.key,api_key))
        self.assertEqual(self.newApi.url,api_game, "Obtenido(%s) deberia ser %s" % (self.newApi.url,api_game))

    # Verifica el codigo de estatus
    def testStatusCode(self):
        self.assertEqual(self.newApi.checkStatusCode(),True, "Obtenido(%s) deberia ser %s" % (self.newApi.checkStatusCode(),True))

        self.assertEqual(self.newApi.response.status_code,200, "Obtenido(%s) deberia ser %s" % (self.newApi.response.status_code,200))        

        # Se cambia el url para arroje el error deseado
        self.newApi.getResponse('https://api.rawg.io/api/asdf')
        self.assertEqual(self.newApi.checkStatusCode(),False, "Obtenido(%s) deberia ser %s" % (self.newApi.checkStatusCode(),False))

        self.assertEqual(self.newApi.response.status_code,404, "Obtenido(%s) deberia ser %s" % (self.newApi.response.status_code,404))    

    # Se comprueba la funcion listGames
    def testListGames(self):
        param = 'gamess'      # Se le da un parametro incorrecto  
        
        # Checa la salida por pantalla
        with mock.patch('sys.stdout') as fake_stdout:
            self.newApi.listGames(param)
        fake_stdout.assert_has_calls([mock.call.write('ID incorrecto'), 
        mock.call.write('\n')])

        param = 'games'     # Se cambia por el parametro correcto
        with mock.patch('sys.stdout') as fake_stdout:
            self.newApi.listGames(param)
        fake_stdout.assert_has_calls([mock.call.write('Archivo apiListGames.json actualizado'), 
        mock.call.write('\n')])

        # Se lee el contenido de ambos archivos (el que crea la función antes llamada y el ya
        # escrito dentro de la carpeta "testJson")
        with open("tests-apiListGames.json", 'r') as file:  
            content1 = json.load(file)            
        
        with open("testJson/tests-apiListGames.json", 'r') as file:  
            content2 = json.load(file)
    
        # Verifica si el contenido de ambos archivos es identico
        self.assertEqual(content1,content2, "Obtenido(%s) deberia ser %s" % (content1,content2)) 

    # Se comprueba la funcion idGamne
    def testIdGame(self):
        param = '11111111'        # Parametro incorrecto
        
        with mock.patch('sys.stdout') as fake_stdout:
            self.newApi.idGame(param)
        fake_stdout.assert_has_calls([mock.call.write('ID incorrecto'), 
        mock.call.write('\n')])

        param = '3498'      # Parametro correcto
        with mock.patch('sys.stdout') as fake_stdout:
            self.newApi.idGame(param)
        fake_stdout.assert_has_calls([mock.call.write('Archivo apiGame.json actualizado'), 
        mock.call.write('\n')])


        with open("tests-apiGame.json", 'r') as file:  
            content1 = json.load(file)            
        
        with open("testJson/tests-apiGame.json", 'r') as file:  
            content2 = json.load(file)
    
        self.assertEqual(content1,content2, "Obtenido(%s) deberia ser %s" % (content1,content2)) 

    # Verifica la funcion availablePlatforms
    def testAvailablePlatforms(self):        
        with mock.patch('sys.stdout') as fake_stdout:
            self.newApi.availablePlatforms()
        fake_stdout.assert_has_calls([mock.call.write('Archivo apiPlatforms.json actualizado'), 
        mock.call.write('\n')])

        with open("tests-apiPlatforms.json", 'r') as file:  
            content1 = json.load(file)            
        
        with open("testJson/tests-apiPlatforms.json", 'r') as file:  
            content2 = json.load(file)
    
        self.assertEqual(content1,content2, "Obtenido(%s) deberia ser %s" % (content1,content2)) 

    # Verifica la funcion genres
    def testGenres(self):
        with mock.patch('sys.stdout') as fake_stdout:
            self.newApi.genres()
        fake_stdout.assert_has_calls([mock.call.write('Archivo apiGenres.json actualizado'), 
        mock.call.write('\n')])

        with open("tests-apiGenres.json", 'r') as file:  
            content1 = json.load(file)            
        
        with open("testJson/tests-apiGenres.json", 'r') as file:  
            content2 = json.load(file)
    
        self.assertEqual(content1,content2, "Obtenido(%s) deberia ser %s" % (content1,content2)) 


if __name__ == '__main__':    
    unittest.main()