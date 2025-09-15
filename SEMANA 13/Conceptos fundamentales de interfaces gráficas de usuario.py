import tkinter as tk
from tkinter import messagebox

# ============================
# Aplicación de Ejemplo - Tkinter
# ============================

class Aplicacion:
    def __init__(self, master):
        # Configuración de la ventana principal
        self.master = master
        master.title("Gestor de Información")
        master.geometry("400x300")  # tamaño fijo
        master.resizable(False, False)

        # Etiqueta de título
        self.label_titulo = tk.Label(master, text="Gestor de Datos con Tkinter", font=("Arial", 14, "bold"))
        self.label_titulo.pack(pady=10)

        # Frame para campo de entrada
        frame_input = tk.Frame(master)
        frame_input.pack(pady=5)

        # Etiqueta del campo de texto
        self.label_entrada = tk.Label(frame_input, text="Ingrese información:")
        self.label_entrada.grid(row=0, column=0, padx=5)

        # Campo de texto
        self.entry_dato = tk.Entry(frame_input, width=30)
        self.entry_dato.grid(row=0, column=1, padx=5)

        # Botón "Agregar"
        self.boton_agregar = tk.Button(frame_input, text="Agregar", command=self.agregar_dato)
        self.boton_agregar.grid(row=0, column=2, padx=5)

        # Lista para mostrar datos
        self.lista_datos = tk.Listbox(master, width=50, height=10)
        self.lista_datos.pack(pady=10)

        # Botón "Limpiar"
        self.boton_limpiar = tk.Button(master, text="Limpiar", command=self.limpiar_datos)
        self.boton_limpiar.pack(pady=5)

    # ============================
    # Funciones de la aplicación
    # ============================
    def agregar_dato(self):
        """Agrega el contenido del campo de texto a la lista"""
        dato = self.entry_dato.get().strip()
        if dato:  # valida que no esté vacío
            self.lista_datos.insert(tk.END, dato)
            self.entry_dato.delete(0, tk.END)  # limpia el campo
        else:
            messagebox.showwarning("Entrada vacía", "Por favor ingrese un dato válido.")

    def limpiar_datos(self):
        """Limpia el campo de texto y elimina la selección en la lista"""
        seleccion = self.lista_datos.curselection()
        if seleccion:
            # Si hay un elemento seleccionado, se elimina
            for index in reversed(seleccion):
                self.lista_datos.delete(index)
        else:
            # Si no hay selección, solo limpia el campo de texto
            self.entry_dato.delete(0, tk.END)

# ============================
# Ejecución de la aplicación
# ============================
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
