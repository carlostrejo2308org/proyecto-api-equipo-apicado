import json
import requests
'''
from textwrap import indent
from unittest import result
from urllib import request
from venv import create
'''

class api:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.response = None
        
    #verificar la respuesta http
    def checkStatusCode(self):
        if  self.response == None:
            self.response = requests.get(self.url)            
        
        if  200  <= self.response.status_code <= 299:
            return True
        elif  400  <= self.response.status_code <= 499:
            return False
        return False            

    #Creador de los json de las respuestas    
    def createJson(content, name):
        file = open(f"tests-api{name}.json", 'w')
        file.write(content)
        file.close()
        print(f'Archivo api{name}.json actualizado')

    # Hace la petición
    def getResponse(self, url):
        self.response = requests.get(url)

    #Muestra una lista de ciertos juegos y muestra la respuesta en el json apigames
    def listGames(self,param):        
        self.getResponse(self.url + param + self.key)       
        
        if self.checkStatusCode():
            r = json.loads(self.response.content)
            arr = []

            for element in r['results']:
                content = {
                    'id' : element['id'],
                    'name': element["name"],
                    'released' : element["released"]
                }
                arr.append(content)
                #Resultados en consola
                #print(content)
            api.createJson(json.dumps(arr, indent = 2),'ListGames')
        else:
            print("ID incorrecto")

    #Tomamos la identificación (parama) y obtenemos los detalles del juego.
    def idGame(self, param): 
        #Hacemos la peticion                
        self.getResponse(self.url +'games/'+param + self.key)

        #Verificamos la respuesta para ver si encontró la dirección
        if self.checkStatusCode():

            #Guardamos el contenido de la petición en una variable, para pasarlo a un diccionario y obtener solo algunos datos del json.
            r = json.loads(self.response.content)

            #Obtenemos los datos
            content = {
                'id':r["id"],
                'name':r["name"],
                'released' : r["released"]
            }
            #Resultados en consola
            # print(content)

            #Regresamos el diccionario a un string
            api.createJson(json.dumps(content, indent = 2),'Game')
        else:
            print("ID incorrecto")
    
    #plataformas disponibles y 5 juegos por default
    def availablePlatforms(self):        
        self.getResponse(self.url + 'platforms' + self.key)

        if self.checkStatusCode():
            r = json.loads(self.response.content)        
            arr = []
            for element in r['results']:
                content = {
                    'id' : element['id'],
                    'name': element["name"],
                    'games_count' : element["games_count"]
                }
                arr.append(content)
                #Resultados en consola
                #print(content)
            api.createJson(json.dumps(arr, indent = 2),'Platforms')      

    def genres(self):        
        self.getResponse(self.url + 'genres' + self.key)

        if self.checkStatusCode():
            r = json.loads(self.response.content)
            arr = []
            for element in r['results']:
                content = {
                    'name': element["name"],
                    'games_count' : element["games_count"]
                }
                arr.append(content)     
            #ver respuesta en json
            api.createJson(json.dumps(arr, indent = 2),'Genres')  
        
#MAIN 
if __name__ == '__main__':
    # 'games/{id}/movies'
    api_key = '?key=9a1c16878d8c4ad39ce142b6fcff8340&1'    
    api_game = ('https://api.rawg.io/api/')
    
    #objeto de la api
    newApi = api(api_game, api_key)
     
    #respuesta de la api    
    if newApi.checkStatusCode():        
        print("Respuesta satisfactoria, status " + str(newApi.response.status_code))
    else:
        print("Error del cliente, status " + str(newApi.response.status_code))


    #lista de juegos, 100 respuestas aprox
    # newApi.listGames('games')
    # newApi.idGame('3498')
    # newApi.availablePlatforms()
    # newApi.genres()