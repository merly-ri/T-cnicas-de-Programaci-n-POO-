import tkinter as tk
import subprocess
import os

# Ruta base del proyecto (ajusta si es necesario)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Función para ejecutar un archivo Python
def ejecutar_ruta(rel_path):
    ruta_completa = os.path.join(BASE_DIR, rel_path)
    subprocess.run(["python", ruta_completa], shell=True)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Dashboard POO - Michelle Rivera")
ventana.geometry("500x600")
ventana.config(bg="lightblue")

# Título principal
tk.Label(ventana, text="Dashboard de Proyectos de POO", font=("Arial", 16), bg="lightblue").pack(pady=10)

# === Semana 1 ===
tk.Label(ventana, text="TRABAJO 1", font=("Arial", 14, "bold"), bg="lightblue").pack()
tk.Button(ventana, text="CLIMA FUNCIONAL.py", command=lambda: ejecutar_ruta(
    "TRABAJO 4/TRABAJO 1/CLIMA FUNCIONAL.py")).pack(pady=2)
tk.Button(ventana, text="CLIMA POO.py", command=lambda: ejecutar_ruta("TRABAJO 4/TRABAJO 1/CLIMA POO.py")).pack(pady=2)

# === Ejemplos del mundo real ===
tk.Label(ventana, text="TRABAJO 2", font=("Arial", 14, "bold"), bg="lightblue").pack(pady=10)
tk.Button(ventana, text="Tienda Onlinee.py", command=lambda: ejecutar_ruta(
    "TRABAJO 4/TRABAJO 2/Tienda Onlinee.py")).pack(pady=2)

# === Tipos de datos e identificadores ===
tk.Label(ventana, text="TRABAJO 3", font=("Arial", 14, "bold"), bg="lightblue").pack(pady=10)
tk.Button(ventana, text="Área de un círculo.py", command=lambda: ejecutar_ruta(
    "TRABAJO 4/TRABAJO 3/Area_de_un_circulo.py")).pack(pady=2)

# === Aplicación de conceptos de POO ===
tk.Label(ventana, text="TRABAJO 4", font=("Arial", 14, "bold"), bg="lightblue").pack(pady=10)
tk.Button(ventana, text="Encapsulacion.py", command=lambda: ejecutar_ruta(
    "TRABAJO 4/Trabajo 7/Encapsulacion.py")).pack(pady=2)
tk.Button(ventana, text="Herencia.py", command=lambda: ejecutar_ruta("TRABAJO 4/Trabajo 7/Herencia.py")).pack(pady=2)
tk.Button(ventana, text="Polimorfismo.py", command=lambda: ejecutar_ruta(
    "TRABAJO 4/Trabajo 7/Polimorfsino.py")).pack(pady=2)

# === Semana 7 ===
tk.Label(ventana, text="TRABAJO 5", font=("Arial", 14, "bold"), bg="lightblue").pack(pady=10)
tk.Button(ventana, text="Constructores y Destructores.py", command=lambda: ejecutar_ruta(
    "TRABAJO 4/TRABAJO 7/CONSTRUCTORES Y DESTRUCTORES.py")).pack(pady=2)

# Iniciar ventana
ventana.mainloop()
