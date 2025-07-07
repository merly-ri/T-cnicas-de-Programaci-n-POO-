# Clase base de herencia
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        print(f"Vehículo: {self.marca} {self.modelo}")

# Clase derivada

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        # Llamada al constructor de la clase base
        super().__init__(marca, modelo)
        self.puertas = puertas

    def descripcion(self):
        # Sobrescribimos el método descripción
        print(f"Coche: {self.marca} {self.modelo} con {self.puertas} puertas.")

    def tocar_claxon(self):
        print(f"¡{self.marca} dice: Beep beep!")

# Programa principal
if __name__ == "__main__":
    vehiculo1 = Vehiculo("Toyota", "Hilux")
    vehiculo1.descripcion()


    coche1 = Coche("Ford", "Mustang", 2)
    coche1.descripcion()
    coche1.tocar_claxon()