from mascota.Mascota import Mascota

class Perro(Mascota):
    def __init__(self, name, tipo, golosinas, tamaño):
        super().__init__(name,tipo,golosinas)
        self.tamaño=tamaño
        self.juguetes=[]
    
    #Sobre-escritura de sonido()
    def sonido(self):
        # super().sonido()-> en caso se quisiera imprimir "está haciendo ruido antes de está maullando"
        print(f"{self.name} está  ladrando")
        return self

    #Sobre-escritura de información
    def informacion(self):
        super().informacion()
        print(f"Además este perro es de tamaño: {self.tamaño}")