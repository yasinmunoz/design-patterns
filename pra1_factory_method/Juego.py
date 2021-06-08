from Habitacion import Habitacion
from Laberinto import Laberinto
from Pared import Pared
from Puerta import Puerta
from Bomba import Bomba

class Juego:       

    #construye el juego con un laberinto
    def __init__ (self):
        #laberinto del juego
        self.laberinto = Laberinto()
        print("¡COMIENZA EL JUEGO!")
    
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
        
    # fabrica una bomba
    def crear_bomba(self):
        bomba = Bomba ()
        return bomba 

    # FABRICA UN LABERINTO CON 2 HABITACIONES Y BOMBAS
    def fabricar_lab_2hab_bombs(self):
        # se crea el laberinto...
        laberinto = self.crear_laberinto()

        # ... con dos habitaciones ...
        hab1 = self.crear_habitacion()
        hab2 = self.crear_habitacion()

        # ... una puerta que comunica con hab1 y hab2 ...
        puerta = self.crear_puerta (hab1, hab2)

        # ... se define hab1 con una pared, una puerta y dos bombas ...
        hab1.set_norte(self.crear_pared())
        hab1.set_sur(puerta)
        hab1.set_este(self.crear_bomba())
        hab1.set_oeste(self.crear_bomba())

        # ... se define hab2 con una pared, una puerta y dos bombas ...
        hab2.set_norte(puerta)
        hab2.set_sur(self.crear_pared())
        hab2.set_este(self.crear_bomba())
        hab2.set_oeste(self.crear_bomba())

        #... se añade hab1 y hab2 a la lista de habitaciones ...
        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)

        #... y se setea el laberinto con el del juego.
        self.laberinto = laberinto        

    # FABRICA UN LABERINTO CON 4 HABITACIONES Y BOMBAS
    def fabricar_lab_4hab_bombs(self):

        # se crea el laberinto...
        laberinto = self.crear_laberinto()

        #... con cuatro habitaciones ...
        hab1 = self.crear_habitacion()
        hab2 = self.crear_habitacion()
        hab3 = self.crear_habitacion()
        hab4 = self.crear_habitacion()

        # ... una puerta que comunica hab1 con hab2 ...
        puerta1 = self.crear_puerta(hab1, hab2)

        # ... otra puerta que comunica hab1 con hab3 ...
        puerta2 = self.crear_puerta(hab1, hab4)

        # ... otra puerta que comunica hab2 con hab4 ...
        puerta3 = self.crear_puerta(hab2, hab3)

        # ... otra puerta que cominica hab4 con hab3 ...
        puerta4 = self.crear_puerta(hab3, hab4)

        # ... se define hab1 ...
        hab1.set_norte(self.crear_bomba())
        hab1.set_sur(puerta2)
        hab1.set_este(puerta1)
        hab1.set_oeste(self.crear_pared())

        # ... se define hab2 ...
        hab2.set_norte(self.crear_bomba())
        hab2.set_sur(puerta3)
        hab2.set_este(self.crear_pared())
        hab2.set_oeste(puerta1)

        # ... se define hab3 ...
        hab3.set_norte(puerta3)
        hab3.set_sur(self.crear_bomba())
        hab3.set_este(self.crear_pared())
        hab3.set_oeste(puerta4)

        # ... se define hab4 ...
        hab4.set_norte(puerta2)
        hab4.set_sur(self.crear_bomba())
        hab4.set_este(puerta4)
        hab4.set_oeste(self.crear_pared())

        # ... se añade hab1, hab2, hab3 y hab4 a la lista de habitaciones ...
        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        laberinto.agregar_habitacion(hab3)
        laberinto.agregar_habitacion(hab4)

        #... y se setea el laberinto con el del juego.
        self.laberinto = laberinto