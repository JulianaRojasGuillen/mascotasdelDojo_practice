from mascota.Mascota import Mascota

class Gato(Mascota):
    def __init__(self, name, tipo, golosinas, color_arenero):
        super().__init__(name,tipo,golosinas)
        self.color_arenero=color_arenero
    
    #Sobre-escritura de sonido()
    def sonido(self):
        # super().sonido()-> en caso se quisiera imprimir "está haciendo ruido antes de está maullando"
        print(f"{self.name} está  maullando")
        return self

    #Sobre-escritura de información
    def informacion(self):
        super().informacion()
        print(f"Además su arenero es de color: {self.color_arenero}")
