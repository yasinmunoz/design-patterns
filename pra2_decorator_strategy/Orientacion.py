import abc
from ElementoMapa import ElementoMapa

class Orientacion (ElementoMapa):
   
    #pone un elem_mapa en una orientacion de la habitacion
    @abc.abstractmethod
    def poner(self, elem_mapa, habitacion):
        pass