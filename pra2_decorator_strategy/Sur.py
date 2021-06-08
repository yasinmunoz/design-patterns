from Orientacion import Orientacion

class Sur (Orientacion):
    
    #pone un elem_mapa en el sur de habitacion
    def poner(self, elem_mapa, habitacion):
        habitacion.set_sur(elem_mapa)