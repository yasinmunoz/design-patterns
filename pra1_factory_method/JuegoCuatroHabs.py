from Juego import Juego

########## JUEGO LABERINTO CUATRO HABITACIONES CON BOMBAS  ##########
print( "---- Laberinto con cuatro habitaciones con bombas ----")
print("-------------------------------------------------")
juego = Juego()
juego.fabricar_lab_4hab_bombs()

# Entramos al laberinto...
#... y por defecto entramos a la hab1 ...
habitacion = juego.laberinto.entrar()

# ... nos movemos al norte de la hab1 para activar la bomba ...
habitacion.get_norte().entrar()

# ... nos movemos al oeste de la hab1 para chocarnos ...
habitacion.get_oeste().entrar()

# ... nos movemos al este de la hab1 para abrir la puerta ...
habitacion.get_este().abrir()

# ... entramos en la hab2 ...
habitacion = habitacion.get_este().get_lado2()
habitacion.entrar(juego.laberinto.numero_habitacion(habitacion))

# ... una vez dentro, cerramos la puerta ...
habitacion.get_oeste().cerrar()

# ... entramos en la hab3 ...
habitacion = habitacion.get_sur().get_lado2()
habitacion.entrar(juego.laberinto.numero_habitacion(habitacion))

# ... entramos en la hab4 ...
habitacion = habitacion.get_oeste().get_lado2()
habitacion.entrar(juego.laberinto.numero_habitacion(habitacion))

# ... nos movemos al sur de la hab4 para activar la bomba.
habitacion.get_sur().entrar()