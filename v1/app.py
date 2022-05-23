from urllib import request
from venv import create
import requests
import random

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
    def createJson(content):
        file = open("apigames.json", 'wb')
        file.write(content)
        file.close()
        print('Archivo apigames.json actualizado')

    #Muestra una lista de ciertos juegos y muestra la respuesta en el json apigames
    def listGames(self,params):
        response = requests.get(self.url + params + self.key)
        content = response.content      
        #ver respuesta en json
        api.createJson(content)
        

    #Tomamos el id(params) y obtiene los detalles del juego
    def idGame(self, params): 
        response = requests.get(self.url +'games/'+params + self.key)

        if  200  <= response.status_code <= 299:
            content = response.content 
            api.createJson(content)
        elif  400  <= response.status_code <= 499:
            print("ID incorrecto")
    
    #plataformas disponibles y 5 juegos por default
    def availablePlatforms(self):
        response = requests.get(self.url + 'platforms/' + self.key)
        content = response.content      
        #ver respuesta en json
        api.createJson(content)        

    def genres(self):
        response = requests.get(self.url + 'genres/' + self.key)
        content = response.content      
        #ver respuesta en json
        api.createJson(content)  
        
#MAIN 
if __name__ == '__main__':
    # 'games/{id}/movies'
    api_key = '?key=9a1c16878d8c4ad39ce142b6fcff8340&1'
    api_game = (f'https://api.rawg.io/api/')
    
    #objeto de la api
    newApi = api(api_game, api_key)
     
    #respuesta de la api
    response = newApi.urlStatus()

    #lista de juegos, 100 respuestas aprox
    # newApi.listGames('games')
    # # newApi.idGame('3498')
    # newApi.availablePlatforms()
    # newApi.genres()