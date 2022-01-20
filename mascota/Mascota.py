from posixpath import supports_unicode_filenames

class Mascota:

    lista_mascotas=[]

    def __init__(self,name="N/A",tipo="N/A",golosinas="N/A"):
        self.name=name
        self.tipo=tipo
        self.golosinas=golosinas
        self.salud=0
        self.energia=0
        self.juguetes=[]
        Mascota.lista_mascotas.append(self)

    def dormir(self):
        self.energia+=25
        print(f"Dormir: energía de {self.name} incrementó en 25, total: {self.energia}")
        return self

    def comer(self):
        self.energia+=5
        self.salud+=10
        print(f"Comer: Ahora {self.name} tiene energía total: {self.energia} y salud total: {self.salud}")
        return self

    def jugar(self):
        self.salud+=5
        print(f"Jugar: Ahora la salud de {self.name} incrementó en 5, total: {self.salud}")
        return self

    def sonido(self):
        print(f"{self.name} está haciendo ruido")
        return self

    def agregar_juguete(self,jugueteNuevo):
        self.juguetes.append(jugueteNuevo)
        print(f"Se agregó el juguete: {jugueteNuevo} a los juguetes de {self.name}")

    def informacion(self):
        print(f"{self.name} es de tipo: {self.tipo} y le gusta las golosinas: {self.golosinas}")

    @classmethod
    def mostrar_lista_mascotas(cls):
        print("Lista de mascotas: ")
        for mascota in cls.lista_mascotas:
            mascota.informacion()
