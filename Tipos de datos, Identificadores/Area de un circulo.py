#Calcular el area de un circulo
import math

# Solicitar al usuario el radio del círculo
radio_str = input("Ingresa el radio del círculo en centímetros: ")  # tipo de dato string
radio = float(radio_str)  # convertir a float

# Calcular el área del círculo
area_circulo = math.pi * radio ** 2  # float

# Definir un límite para comparar (por ejemplo, 100 cm²)
limite_area = 100  # integer

# Verificar si el área es mayor que el límite
es_mayor = area_circulo > limite_area  # boolean

# Mostrar resultados
print("El área del círculo es:", area_circulo, "cm²")
print("¿El área es mayor que", limite_area, "? :", es_mayor)
