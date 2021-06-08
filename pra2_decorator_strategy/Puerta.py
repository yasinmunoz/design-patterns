from ElementoMapa import ElementoMapa
from Habitacion import Habitacion


class Puerta (ElementoMapa):

    #Construye la puerta
    def __init__ (self):
        #Los lados de la puerta comunican con habitaciones
        self.__lado1 = Habitacion()
        self.__lado2 = Habitacion()
        
        #La puerta esta abierta (por defecto)
        self.__abierta = True 

    #getters y setters de los lados 
    def get_lado1 (self):
        return self.__lado1
    def set_lado1 (self, habitacion):
        self.__lado1 = habitacion 

    def get_lado2 (self):
        return self.lado2 
    def set_lado2 (self, habitacion):
        self.lado2 = habitacion

    #Abre la puerta 
    def abrir (self):
        self.__abierta = True 
        print ("La puerta está abierta")

    #Cierra la puerta 
    def cerrar (self):
        self.__abierta = False 
        print ("La puerta está cerrada")

    #Verifica si el elem_mapa es puerta
    def es_puerta (self):
        return True        
    

