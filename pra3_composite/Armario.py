from Contenedor import Contenedor 

class Armario (Contenedor):
    
    #entra en el armario
    def entrar(self):
        print ("Estás en el armario")

    #verifica si es armario
    def es_armario(self):
        return True