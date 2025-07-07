# Clase base de encapsulacion

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre   # Atributo privado
        self.__edad = edad       # Atributo privado

    # Getter
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Setter
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad no válida")

if __name__ == "__main__":
    persona = Persona("Merly", 18)
    print(f"Nombre: {persona.get_nombre()}")
    print(f"Edad: {persona.get_edad()}")

    persona.set_edad(23)
    print(f"Nueva Edad: {persona.get_edad()}")

    persona.set_edad(-5)  # Intento inválido