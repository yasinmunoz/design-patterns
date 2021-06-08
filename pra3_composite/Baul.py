from Contenedor import Contenedor

class Baul (Contenedor):
    
    #entra en el baúl
    def entrar(self):
        print ("Estás en el baúl")

    #verifica si es baul
    def es_baul(self):
        return True