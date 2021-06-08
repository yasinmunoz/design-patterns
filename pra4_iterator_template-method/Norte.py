from Orientacion import Orientacion

class Norte (Orientacion):
    
    #pone un elem_mapa en el norte de habitacion
    def poner(self, elem_mapa, habitacion):
        habitacion.set_norte(elem_mapa)