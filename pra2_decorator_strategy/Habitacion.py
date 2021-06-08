from ElementoMapa import ElementoMapa

class Habitacion (ElementoMapa):

    #construye el objeto habitacion
    def __init__(self):        
        #orientaciones
        self.__norte = None
        self.__sur = None 
        self.__este = None 
        self.__oeste = None 

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

    #entra en la habitacion
    def entrar(self, num):
        print ("Estás en la habitacion",num)

    #pone un elem_mapa en una orientacion de la habitacion
    def poner (self, elem_mapa, orientacion):
        orientacion.poner(elem_mapa, self)
        
    # verifica si es Habitación
    def es_habitacion(self):
        return True
    
