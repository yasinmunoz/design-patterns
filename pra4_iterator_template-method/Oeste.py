from Orientacion import Orientacion

class Oeste (Orientacion):
    
    #pone un elem_mapa en el oeste de habitacion
    def poner(self, elem_mapa, habitacion):
        habitacion.set_oeste(elem_mapa)