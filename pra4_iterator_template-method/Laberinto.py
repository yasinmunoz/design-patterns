class Laberinto:
    
    #Construye el laberinto con una lista de habitaciones
    def __init__ (self):
        self.__habitaciones = [] 

    #getter y setter de habitaciones
    def get_habitaciones (self):
        return self.__habitaciones

    def set_habitaciones (self, habitaciones):
        self.__habitaciones = habitaciones

    #agrega una habitacion a habitaciones
    def agregar_habitacion (self, habitacion):
        self.__habitaciones.append(habitacion)

    #obtiene una habitacion
    def obtener_habitacion (self, num_hab):
        return self.__habitaciones[num_hab]

    #retorna numero de habitacion
    def numero_habitacion (self, habitacion):
        return self.__habitaciones.index(habitacion) + 1

    #entrar en la primera habitacion del laberinto (por defecto)
    def entrar (self):
        print("Estoy en el laberinto")
        habitacion = self.__habitaciones[0]
        #entra en la habitacion
        habitacion.entrar(self.numero_habitacion(habitacion)) 
        return habitacion

    #recorre el laberinto con un iterador
    def recorrer(self, un_bloque):
        for i in self.get_habitaciones():
            i.recorrer(un_bloque)