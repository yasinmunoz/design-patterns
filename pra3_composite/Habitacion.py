from Contenedor import Contenedor

class Habitacion (Contenedor):    

    #entra en la habitacion
    def entrar(self, num):
        print ("Estás en la habitacion",num)

    #pone un elem_mapa en una orientacion de la habitacion
    def poner (self, elem_mapa, orientacion):
        orientacion.poner(elem_mapa, self)
        
    # verifica si es Habitación
    def es_habitacion(self):
        return True
    
