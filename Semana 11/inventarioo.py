import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = self.cargar()

    def agregar(self, producto):
        self.productos[producto.id] = producto
        self.guardar()

    def eliminar(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar()

    def actualizar(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            self.guardar()

    def buscar(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def mostrar(self):
        return [f"{p.id}: {p.nombre} - Cantidad: {p.cantidad}, Precio: ${p.precio}" for p in self.productos.values()]

    def guardar(self):
        with open(self.archivo, "w") as f:
            json.dump({id: p.to_dict() for id, p in self.productos.items()}, f)

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                return {id: Producto(**p) for id, p in data.items()}
        except FileNotFoundError:
            return {}

def menu():
    inv = Inventario()
    while True:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inv.agregar(Producto(id, nombre, cantidad, precio))
            print("Producto agregado correctamente.")

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inv.eliminar(id)
            print("Producto eliminado.")

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja vacío para no cambiar): ")
            precio = input("Nuevo precio (deja vacío para no cambiar): ")
            inv.actualizar(id, int(cantidad) if cantidad else None, float(precio) if precio else None)
            print("Producto actualizado.")

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inv.buscar(nombre)
            if resultados:
                for p in resultados:
                    print(f"{p.id}: {p.nombre} - Cantidad: {p.cantidad}, Precio: ${p.precio}")
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            for item in inv.mostrar():
                print(item)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
