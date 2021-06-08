from ElementoMapa import ElementoMapa
import abc 

class Decorator(ElementoMapa):
    
    #construye el juego con un laberinto
    def __init__ (self):
        # componente al que agrega
        __elem_mapa = None
    
    # get y set de elem_mapa
    def get_elem_mapa(self):
        return self.__elem_mapa
    def set_elem_mapa(self, elem_mapa):
        self.__elem_mapa = elem_mapa

    #accede al componenete
    @abc.abstractmethod
    def entrar(self):
        pass
        