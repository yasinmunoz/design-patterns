from Orientacion import Orientacion

class Este (Orientacion):
    
    #pone un elem_mapa en el este de habitacion
    def poner(self, elem_mapa, habitacion):
        habitacion.set_este(elem_mapa)