from inspect import classify_class_attrs
from mascota.Mascota import Mascota

class Ninja:

    lista_ninjas=[]

    def __init__(self,nombre,apellido,mascota):

        self.nombre=nombre
        self.apellido=apellido
        self.mascotas={}
        self.mascotas[mascota.tipo]=mascota
        Ninja.lista_ninjas.append(self)

# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
    def caminar(self,mascota):
        print(f"{self.nombre} está caminando con {mascota.name}")
        mascota.jugar()
        return self

# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
    def alimentar(self,mascota):
        print(f"{self.nombre} está alimentando a {mascota.name}")
        mascota.comer()
        return self

# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
    def bañar(self,boby):
        boby.sonido()
        return self

#agregando una mascota a ninja
    def nuevaMascota(self,nuevaMascota):
        self.mascotas[nuevaMascota.tipo]=nuevaMascota
        print(f"{self.nombre} adoptó a {nuevaMascota.name}")

# mostrando datos de un ninja
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} , Apellido: {self.apellido}")
        print(f"Sus mascotas son: ")
        for mascota in self.mascotas:
            print(f"{self.mascotas[mascota].name} de tipo {self.mascotas[mascota].tipo}" )

#mostrar la lista de ninjas
    @classmethod
    def mostrar_lista_ninjas(cls):
        print("Los ninjas registrados son: ")
        for ninja in cls.lista_ninjas:
            Ninja.mostrar_datos(ninja)

