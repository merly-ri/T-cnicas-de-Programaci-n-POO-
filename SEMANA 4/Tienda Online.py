import random

numero = random.randint(1, 100)
print(f"Número generado: {numero}")

if numero % 2 == 0:
    print("Es un número par.")
else:
    print("Es un número impar.")
