import json
import requests
from appDB import app
class api:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.response = None
        self.appDB = app()      # Objeto de tipo app, que nos ayudará a conectarnos a la DB
        
    #verificar la respuesta http
    def checkStatusCode(self):
        if  self.response == None:
            self.response = requests.get(self.url)            
        
        if  200  <= self.response.status_code <= 299:
            return True
        elif  400  <= self.response.status_code <= 499:
            return False
        return False            

    # Hace la petición
    def getResponse(self, url):
        self.response = requests.get(url)

    #Muestra una lista de ciertos juegos y muestra la respuesta en el json apigames
    def listGames(self,param):        
        self.getResponse(self.url + param + self.key)       
        
        if self.checkStatusCode():
            r = json.loads(self.response.content)
            
            self.appDB.setCollection('ListGames')   # Se setea el nombre de la coleeción
            self.appDB.eliminar()       # Se eliminan los registros dentro de la colección
            for element in r['results']:
                content = {
                    'id' : element['id'],
                    'name': element["name"],
                    'released' : element["released"]
                }
                #Resultados en consola
                #print(content)
            
                self.appDB.insertar(content)    # Ahora se inserta el contenido de la consulta, dentro de la DB
            print(f"Registros agregados a la colección : ListGames")
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

            self.appDB.setCollection('Game')
            self.appDB.eliminar()

            #Obtenemos los datos
            content = {
                'id':r["id"],
                'name':r["name"],
                'released' : r["released"]
            }            

            self.appDB.insertar(content)
            
            print(f"Registro agregado a la colección : Game")
        else:
            print("ID incorrecto")
    
    #plataformas disponibles y 5 juegos por default
    def availablePlatforms(self):        
        self.getResponse(self.url + 'platforms' + self.key)

        if self.checkStatusCode():
            r = json.loads(self.response.content)        

            self.appDB.setCollection('Platforms')
            self.appDB.eliminar()
            
            for element in r['results']:
                content = {
                    'id' : element['id'],
                    'name': element["name"],
                    'games_count' : element["games_count"]
                }

                #Resultados en consola
                #print(content)            
                self.appDB.insertar(content)
            print(f"Registros agregados a la colección : Platforms")
                

    def genres(self):        
        self.getResponse(self.url + 'genres' + self.key)

        if self.checkStatusCode():
            r = json.loads(self.response.content)
            self.appDB.setCollection('Genres')
            self.appDB.eliminar()
            for element in r['results']:
                content = {
                    'name': element["name"],
                    'games_count' : element["games_count"]
                }                
                            
                self.appDB.insertar(content)
            print(f"Registros agregados a la colección : Genres")
                
        
#MAIN 
if __name__ == '__main__':
    # 'games/{id}/movies'
    api_key = '?key=9a1c16878d8c4ad39ce142b6fcff8340&1'    
    api_game = ('https://api.rawg.io/api/')
    
    #objeto de la api
    newApi = api(api_game, api_key)

    # newApi.listGames('games')
    # newApi.idGame('3498')
    # newApi.availablePlatforms()
    # newApi.genres()