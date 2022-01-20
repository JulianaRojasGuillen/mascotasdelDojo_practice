from mascota.Mascota import Mascota
from ninja.Ninja import Ninja
from mascota.subclases_mascota.Gato import Gato
from mascota.subclases_mascota.Perro import Perro

#creando un perro y un gato
boby = Perro("Boby","snauzer","galletas","mediano")
amon = Gato("Amon","siames","atun cookie","rojo")

#creando dos ninjas
juliana = Ninja("Juliana","Rojas",boby)
maria = Ninja("Maria", "Guillen",amon)

#Boby come, juega y duerme:
boby.comer().jugar().dormir()

#Juliana sale a caminar con Boby (por lo que Boby juega) y lo alimenta
juliana.caminar(boby).alimentar(boby)

# Amon come
amon.comer()

#Juliana baña a Amon
juliana.bañar(amon)

#juliana adoptó una nueva mascota
pepito=Perro("Pepito", "chihuahua","carnecitas","pequeño")
juliana.nuevaMascota(pepito)

#Mostrando la lista de mascotas:
Mascota.mostrar_lista_mascotas()

#Mostrando la lista de ninjas:
Ninja.mostrar_lista_ninjas()
