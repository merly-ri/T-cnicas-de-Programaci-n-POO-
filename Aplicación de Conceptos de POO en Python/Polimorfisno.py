# Clase base de polimorfisno

class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido genérico")

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra: ¡Guau guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato maúlla: ¡Miau miau!")

def reproducir_sonido(animal):
    # Ejemplo de polimorfismo: diferentes comportamientos
    animal.hacer_sonido()

if __name__ == "__main__":
    animal = Animal()
    perro = Perro()
    gato = Gato()

    reproducir_sonido(animal)
    reproducir_sonido(perro)
    reproducir_sonido(gato)
