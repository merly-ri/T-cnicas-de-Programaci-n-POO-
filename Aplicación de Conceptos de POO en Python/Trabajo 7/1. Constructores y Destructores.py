# class

class ConexionBD:
    """
    Clase que simula una conexión a una base de datos.
    Demuestra el uso de __init__ (constructor) y __del__ (destructor).
    """

    def __init__(self, nombre_bd):
        """
        Constructor que se ejecuta al crear la instancia.
        Simula abrir una conexión a una base de datos.
        """
        self.nombre_bd = nombre_bd
        self.conectado = True
        print(f"Conexión a la base de datos '{self.nombre_bd}' establecida.")

    def ejecutar_consulta(self, consulta):
        """
        Método que simula ejecutar una consulta SQL.
        """
        if self.conectado:
            print(f"Ejecutando consulta en '{self.nombre_bd}': {consulta}")
        else:
            print("No se puede ejecutar la consulta. Conexión cerrada.")

    def __del__(self):
        """
        Destructor que se ejecuta cuando la instancia se destruye.
        Simula cerrar la conexión.
        """
        self.conectado = False
        print(f"Conexión a la base de datos '{self.nombre_bd}' cerrada.")


# Programa principal
if __name__ == "__main__":
    # Crear una conexión simulada
    conexion = ConexionBD("MiBaseDeDatos")

    # Ejecutar algunas consultas
    conexion.ejecutar_consulta("SELECT * FROM usuarios;")
    conexion.ejecutar_consulta("INSERT INTO usuarios VALUES ('Ana', 25);")

    # Forzar la destrucción de la instancia para ver el destructor en acción
    del conexion

    # Nota: Si no usas 'del', el destructor se llama al finalizar el programa.
