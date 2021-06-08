from Forma import Forma
from ElementoMapa import ElementoMapa

class Contenedor (ElementoMapa):

    #construye el objeto contenedor ...
    def __init__(self):        
        # ... con unas orientaciones ...
        self.__norte = None
        self.__sur = None
        self.__este = None
        self.__oeste = None

        # ... y con una forma ...
        self.forma = Forma()

    #getters y setters de los lados 
    def get_norte (self):
        return self.__norte
    def set_norte (self, elem_mapa):
        self.__norte = elem_mapa

    def get_sur (self):
        return self.__sur     
    def set_sur (self,elem_mapa):
        self.__sur = elem_mapa

    def get_este (self):
        return self.__este 
    def set_este (self, elem_mapa):
        self.__este = elem_mapa

    def get_oeste (self):
        return self.__oeste 
    def set_oeste (self, elem_mapa):
        self.__oeste = elem_mapa