from Habitacion import Habitacion
from Laberinto import Laberinto
from Pared import Pared
from Puerta import Puerta
from Bomba import Bomba
from Bicho import Bicho 
from Agresivo import Agresivo
from Perezoso import Perezoso 

class Juego:       

    #construye el juego con un laberinto
    def __init__ (self):
        #bichos del juego
        self.__bichos = [] 

        #laberinto del juego
        self.laberinto = Laberinto()
        print("¡COMIENZA EL JUEGO!")
    
    #get y set de bichos
    def get_bichos (self):
        return self.__bichos
    def set_bichos (self, bichos):
        self.__bichos = bichos

    #fabrica un laberinto
    def crear_laberinto (self):
        return Laberinto()

    #fabrica una habitacion
    def crear_habitacion (self):                        
        return Habitacion()

    #fabrica una pared 
    def crear_pared (self):
        return Pared() 

    #fabrica una puerta
    def crear_puerta (self, hab1, hab2):
        puerta = Puerta()
        puerta.set_lado1(hab1)
        puerta.set_lado2(hab2)
        return puerta
        
    #fabrica una bomba
    def crear_bomba (self):
        bomba = Bomba ()
        return bomba     

    #decorar un elem_mapa con bomba
    def decorar_con_bomba (self, elem_mapa):
        bomba = self.crear_bomba()
        bomba.set_elem_mapa(elem_mapa)
        return bomba 

    #crea un bicho
    def crear_bicho (self, modo):
        bicho = Bicho()
        bicho.set_modo(modo)
        return bicho

    #crea un bicho agresivo
    def crear_bicho_agresivo (self):
        return Agresivo() 

    def crear_bicho_perezoso(self):
        return Perezoso()

    #agrega un bicho a bichos
    def agregar_bicho (self, bicho):
        self.__bichos.append(bicho)

    # FABRICA UN LABERINTO CON 4 HABITACIONES Y BOMBAS
    def fabricar_lab_4hab (self):

        # se crea el laberinto...
        laberinto = self.crear_laberinto()

        #... con cuatro habitaciones ...
        hab1 = self.crear_habitacion()
        hab2 = self.crear_habitacion()
        hab3 = self.crear_habitacion()
        hab4 = self.crear_habitacion()

        #... con un bicho agresivo en la hab1 ...
        bicho_agresivo = self.crear_bicho(self.crear_bicho_agresivo())        
        bicho_agresivo.set_localizacion (hab1)

        #... con un bicho perezoso en la hab2 ...
        bicho_perezoso = self.crear_bicho(self.crear_bicho_perezoso())
        bicho_perezoso.set_localizacion (hab2)

        # ... una puerta que comunica hab1 con hab2 ...
        puerta1 = self.crear_puerta(hab1, hab2)

        # ... otra puerta que comunica hab2 con hab3 ...
        puerta2 = self.crear_puerta(hab2, hab3)

        # ... otra puerta que cominica hab3 con hab4 ...
        puerta3 = self.crear_puerta(hab3, hab4)

        # ... se define hab1 ...
        hab1.set_norte(self.crear_pared())
        hab1.set_sur(puerta1)
        hab1.set_este(self.crear_pared())
        hab1.set_oeste(self.crear_pared())

        # ... se define hab2 ...
        hab2.set_norte(puerta1)
        hab2.set_sur(self.decorar_con_bomba(self.crear_pared))
        hab2.set_este(puerta2)
        hab2.set_oeste(self.decorar_con_bomba(self.crear_pared)) 

        # ... se define hab3 ...
        hab3.set_norte(self.crear_pared())
        hab3.set_sur(puerta3)
        hab3.set_este(self.crear_pared())
        hab3.set_oeste(puerta2)

        # ... se define hab4 ...
        hab4.set_norte(puerta3)
        hab4.set_sur(self.crear_pared())
        hab4.set_este(self.crear_pared())
        hab4.set_oeste(self.crear_pared())

        # ... se añade hab1, hab2, hab3 y hab4 a la lista de habitaciones ...
        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        laberinto.agregar_habitacion(hab3)
        laberinto.agregar_habitacion(hab4)

        # ... se agregan los bichos al juego ... 
        self.agregar_bicho (bicho_agresivo)
        self.agregar_bicho (bicho_perezoso)

        #... y se setea el laberinto con el del juego.
        self.laberinto = laberinto