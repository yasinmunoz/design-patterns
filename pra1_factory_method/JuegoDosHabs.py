from Juego import Juego

########## JUEGO LABERINTO DOS HABITACIONES CON BOMBAS ##########
print( "---- Laberinto con dos habitaciones con bombas ----")
print("-------------------------------------------------")
juego = Juego()
juego.fabricar_lab_2hab_bombs()

# Entramos al laberinto...
#... y por defecto entramos a la hab1 ...
habitacion = juego.laberinto.entrar()

# ... nos movemos al norte de la hab1 ...
habitacion.get_norte().entrar()

# ... entramos en la hab2 ...
habitacion = habitacion.get_sur().get_lado2()
habitacion.entrar(juego.laberinto.numero_habitacion(habitacion))

# ... una vez dentro, cerramos la puerta ...
habitacion.get_norte().cerrar()

# ... nos movemos al sur de la hab1.
habitacion.get_sur().entrar()