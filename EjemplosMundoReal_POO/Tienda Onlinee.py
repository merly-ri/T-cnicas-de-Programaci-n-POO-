# Clase que representa un producto en la tienda
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}")

    def actualizar_stock(self, cantidad):
        self.stock += cantidad


# Clase que representa un cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_al_carrito(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.carrito.append((producto, cantidad))
            producto.actualizar_stock(-cantidad)
            print(f"{cantidad} unidad(es) de {producto.nombre} agregadas al carrito.")
        else:
            print(f"No hay suficiente stock para {producto.nombre}.")

    def ver_carrito(self):
        print(f"\nCarrito de {self.nombre}:")
        total = 0
        for producto, cantidad in self.carrito:
            subtotal = producto.precio * cantidad
            print(f"{producto.nombre} x{cantidad} - ${subtotal:.2f}")
            total += subtotal
        print(f"Total a pagar: ${total:.2f}\n")


# Clase que representa la tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"\nCatálogo de {self.nombre}:")
        for producto in self.productos:
            producto.mostrar_info()


# Simulación del sistema
if __name__ == "__main__":
    # Crear tienda
    tienda = Tienda("Shoplin")

    # Crear productos
    p1 = Producto("Mouse", 14.99, 9)
    p2 = Producto("Teclado", 25.99, 4)
    p3 = Producto("Cargadores", 10.50, 7)



    # Agregar productos a la tienda
    tienda.agregar_producto(p1)
    tienda.agregar_producto(p2)
    tienda.agregar_producto(p3)

    # Mostrar productos disponibles
    tienda.mostrar_productos()

    # Crear cliente
    cliente1 = Cliente("Merly")

    # Cliente agrega productos al carrito
    cliente1.agregar_al_carrito(p1, 7)
    cliente1.agregar_al_carrito(p3, 5)
    cliente1.agregar_al_carrito(p2, 2)  # Este debería fallar por stock insuficiente

    # Ver carrito
    cliente1.ver_carrito()

    # Mostrar stock actualizado
    tienda.mostrar_productos()

