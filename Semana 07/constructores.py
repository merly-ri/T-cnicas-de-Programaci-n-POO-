# archivo.py

class Archivo:
    """
    Clase que representa la apertura y cierre de un archivo de texto.
    Demuestra el uso de __init__ (constructor) y __del__ (destructor).
    """

    def __init__(self, nombre_archivo):
        """
        Constructor que se ejecuta cuando se crea una instancia de la clase.
        Abre el archivo en modo escritura.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, 'w')
        print(f"Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir(self, texto):
        """
        Método para escribir texto en el archivo.
        """
        self.archivo.write(texto + '\n')
        print(f"Se escribió en el archivo: {texto}")

    def __del__(self):
        """
        Destructor que se ejecuta cuando la instancia se elimina.
        Cierra el archivo abierto.
        """
        self.archivo.close()
        print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")


# Programa principal
if __name__ == "__main__":
    # Crear una instancia de la clase Archivo
    mi_archivo = Archivo('ejemplo.txt')

    # Escribir líneas en el archivo
    mi_archivo.escribir('Hola, este es un ejemplo de constructor y destructor.')
    mi_archivo.escribir('Esta línea se añadirá al archivo.')

    # El destructor se invoca automáticamente al finalizar el programa
    # o cuando la instancia es eliminada.
    del mi_archivo  # Forzamos la eliminación para ver el mensaje de cierre
