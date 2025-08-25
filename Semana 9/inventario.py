import json
from pathlib import Path

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = Path(archivo)
        self.productos = {}
        self.cargar()

    def cargar(self):
        if not self.archivo.exists():
            return
        try:
            with self.archivo.open("r", encoding="utf-8") as f:
                data = json.load(f)
                self.productos = {int(k): v for k, v in data.items()}
        except (json.JSONDecodeError, PermissionError):
            print("[ERROR] No se pudo cargar el archivo. Inventario vacío.")

    def guardar(self):
        try:
            with self.archivo.open("w", encoding="utf-8") as f:
                json.dump(self.productos, f, indent=2)
        except PermissionError:
            print("[ERROR] No se pudo guardar el inventario.")

    def agregar(self, id, nombre, precio, cantidad):
        if id in self.productos:
            print("Producto ya existe.")
            return
        self.productos[id] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        self.guardar()
        print("Producto agregado.")

    def actualizar(self, id, nombre=None, precio=None, cantidad=None):
        if id not in self.productos:
            print("Producto no encontrado.")
            return
        if nombre: self.productos[id]["nombre"] = nombre
        if precio: self.productos[id]["precio"] = precio
        if cantidad: self.productos[id]["cantidad"] = cantidad
        self.guardar()
        print("Producto actualizado.")

    def eliminar(self, id):
        if id in self.productos:
            self.productos.pop(id)
            self.guardar()
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def listar(self):
        for id, p in self.productos.items():
            print(f"ID:{id} | Nombre:{p['nombre']} | Precio:{p['precio']} | Cantidad:{p['cantidad']}")

# Ejemplo rápido de uso
inv = Inventario()
inv.agregar(1, "Laptop", 1200.0, 5)
inv.actualizar(1, cantidad=3)
inv.listar()
inv.eliminar(1)
