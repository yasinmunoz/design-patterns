from Juego import Juego

########## JUEGO LABERINTO CUATRO HABITACIONES ##########
print( "---- Laberinto con cuatro habitaciones ----")
print("-------------------------------------------------")
juego = Juego()
juego.fabricar_lab_4hab()

#... activamos el bicho de la hab1 ...
agresivo = juego.get_bichos()[0]
agresivo.get_modo().es_agresivo()

# ... movemos el bicho agresivo de habitacion  ... 
agresivo.get_modo().mover()

# ... bicho agresivo duerme ...
agresivo.get_modo().dormir()

# ... bicho agresivo se despierta ... 
agresivo.get_modo().despertar()

# ... bicho agresivo ataca ...
agresivo.get_modo().atacar()

#... activamos el bicho de la hab2 ...
perezoso = juego.get_bichos()[1]
perezoso.get_modo().es_perezoso()

# ... movemos el bicho perezoso de habitacion  ... 
perezoso.get_modo().mover()

# ... bicho perezoso duerme ...
perezoso.get_modo().dormir()

# ... bicho perezoso se despierta ... 
perezoso.get_modo().despertar()

# ... bicho perezoso ataca ... 
perezoso.get_modo().atacar()

# Entramos al laberinto...
#... y por defecto entramos a la hab1 ...
habitacion = juego.laberinto.entrar()

#... cerramos la puerta de la hab1 ...
habitacion.get_sur().cerrar()

#... abrimos la puerta de la hab1 ...
habitacion.get_sur().abrir()

# ... entramos en la hab2 ...
habitacion = habitacion.get_sur().get_lado2()
habitacion.entrar(juego.laberinto.numero_habitacion(habitacion))

# ... nos movemos al sur de la hab2 para chocarnos ...
habitacion.get_sur().entrar()

# ... nos movemos al oeste para explotar la bomba ...
habitacion.get_oeste().activar()

# ... vamos a comprobar si el oeste de la hab2 es una bomba ...
print ("¿Es el oeste de la habitación 2 una bomba?")
print (habitacion.get_oeste().es_bomba())

# ... vamos a comprobar si dicha bomba está activada ...
print ("¿Está activada?")
print (habitacion.get_oeste().get_activada())

# ... vamos a comprobar si el sur de la hab2 es una bomba ...
print ("¿Es el sur de la habitación 2 una bomba?")
print (habitacion.get_sur().es_bomba())

# ... vamos a comprobar si dicha bomba está activada ...
print ("¿Está activada?")
print (habitacion.get_sur().get_activada())

# ... vamos a comprobar si el bicho 1 es perezoso ... 
print ("¿Es el bicho 1 perezoso?")
print (juego.get_bichos()[0].get_modo().es_perezoso())

# ... vamos a comprobar si el bicho 2 es perezoso ... 
print ("¿Es el bicho 1 perezoso?")
print (juego.get_bichos()[1].get_modo().es_perezoso())