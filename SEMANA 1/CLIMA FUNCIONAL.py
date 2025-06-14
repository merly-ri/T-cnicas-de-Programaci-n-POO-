# clima_funcional.py

# Función para ingresar temperaturas de 7 días
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese la temperatura de cada día (7 días):")
    for i in range(7):
        temp = float(input(f"Temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

# Función principal que organiza la ejecución
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

# Ejecutar el programa
if __name__ == "__main__":
    main()
