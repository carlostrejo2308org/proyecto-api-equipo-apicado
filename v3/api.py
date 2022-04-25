import json
from textwrap import indent
from unittest import result
from urllib import request
from venv import create
import requests


class api:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        
    #verificar la respuesta http
    def urlStatus(self):
        response = requests.get(self.url)
        
        if  200  <= response.status_code <= 299:   
            print("Respuesta satisfactoria, status " + str(response.status_code))
        elif 400  <= response.status_code <= 499:
            print("Error del cliente, status " + str(response.status_code))
        
        #Response contiene el status (status_code)
        return response

    #Creador de los json de las respuestas    
    def createJson(content, name):
        file = open(f"tests/api{name}.json", 'w')
        file.write(content)
        file.close()
        print(f'Archivo api{name}.json actualizado')

    #Muestra una lista de ciertos juegos y muestra la respuesta en el json apigames
    def listGames(self,param):
        response = requests.get(self.url + param + self.key)
        r = json.loads(response.content)        
        if  200  <= response.status_code <= 299:
            arr = []
            for element in r['results']:
                content = {
                    'id' : element['id'],
                    'name': element["name"],
                    'released' : element["released"]
                }
                arr.append(content)
            #Resultados en consola
            # print(content)
            api.createJson(json.dumps(arr, indent = 2),'ListGames')
        elif  400  <= response.status_code <= 499:
            print("ID incorrecto")

    #Tomamos la identificación (parama) y obtenemos los detalles del juego.
    def idGame(self, param): 
        #Hacemos la peticion
        response = requests.get(self.url +'games/'+param + self.key)
        
        #Guardamos el contenido de la petición en una variable, para pasarlo a un diccionario y obtener solo algunos datos del json.
        r = json.loads(response.content)

        #Verificamos la respuesta para ver si encontró la dirección
        if  200  <= response.status_code <= 299:
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
        elif  400  <= response.status_code <= 499:
            print("ID incorrecto")
    
    #plataformas disponibles y 5 juegos por default
    def availablePlatforms(self):
        response = requests.get(self.url + 'platforms' + self.key)
        r = json.loads(response.content)        
        if  200  <= response.status_code <= 299:
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
        response = requests.get(self.url + 'genres' + self.key)
        r = json.loads(response.content)
        if  200  <= response.status_code <= 299:
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
    response = newApi.urlStatus()

    #lista de juegos, 100 respuestas aprox
    #newApi.listGames('games')
    # newApi.idGame('3498')
    # newApi.availablePlatforms()
    newApi.genres()