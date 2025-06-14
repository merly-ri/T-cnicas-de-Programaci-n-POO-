# clima_oop.py

class ClimaDia:
    """
    Clase que representa la temperatura de un solo día.
    """
    def __init__(self, dia, temperatura):
        self.__dia = dia
        self.__temperatura = temperatura  # Encapsulado

    def get_temperatura(self):
        return self.__temperatura

    def __str__(self):
        return f"Día {self.__dia}: {self.__temperatura}°C"


class SemanaClimatica:
    """
    Clase que contiene los datos de una semana de clima.
    """
    def __init__(self):
        self.dias = []

    def ingresar_datos(self):
        print("Ingrese la temperatura para cada día (7 días):")
        for i in range(7):
            temp = float(input(f"Temperatura del día {i + 1}: "))
            dia_clima = ClimaDia(i + 1, temp)
            self.dias.append(dia_clima)

    def calcular_promedio(self):
        total
