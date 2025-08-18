# ==============================
# Clase Producto
# ==============================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


# ==============================
# Clase Inventario
# ==============================
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("⚠️ Error: El ID ya existe en el inventario.")
                return
        self.productos.append(producto)
        print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("✅ Producto eliminado correctamente.")
                return
        print("⚠️ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("✅ Producto actualizado correctamente.")
                return
        print("⚠️ Producto no encontrado.")

    def buscar_por_nombre(self, nombre_buscar):
        resultados = [p for p in self.productos if nombre_buscar.lower() in p.get_nombre().lower()]
        if resultados:
            print("🔎 Resultados de la búsqueda:")
            for p in resultados:
                print(p)
        else:
            print("⚠️ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("\n📋 Inventario completo:")
            for p in self.productos:
                print(p)


# ==============================
# Menú Interactivo con Datos Iniciales
# ==============================
def menu():
    inventario = Inventario()

    # --- Datos precargados ---
    inventario.agregar_producto(Producto("P001", "Arroz 1kg", 50, 1.20))
    inventario.agregar_producto(Producto("P002", "Azúcar 1kg", 40, 1.10))
    inventario.agregar_producto(Producto("P003", "Aceite 1L", 30, 2.50))
    inventario.agregar_producto(Producto("P004", "Leche 1L", 60, 0.95))
    inventario.agregar_producto(Producto("P005", "Pan", 100, 0.15))

    while True:
        print("\n==== MENÚ DE GESTIÓN DE INVENTARIO ====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_prod = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_prod, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_prod = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == "3":
            id_prod = input("Ingrese ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (dejar vacío si no desea cambiar): ")
            nuevo_precio = input("Nuevo precio (dejar vacío si no desea cambiar): ")

            inventario.actualizar_producto(
                id_prod,
                int(nueva_cantidad) if nueva_cantidad else None,
                float(nuevo_precio) if nuevo_precio else None
            )

        elif opcion == "4":
            nombre = input("Ingrese el nombre o parte del nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")


# ==============================
# Ejecución del programa
# ==============================
if __name__ == "__main__":
    menu()
