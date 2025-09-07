class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos_inmutables = (titulo, autor)  # tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # lista mutable

class Biblioteca:
    def __init__(self):
        self.libros = {}        # diccionario {isbn: libro}
        self.usuarios = {}      # diccionario {id: usuario}
        self.usuarios_ids = set()  # conjunto de ids únicos

    def anadir_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        self.libros.pop(isbn, None)

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios_ids:
            self.usuarios[usuario.user_id] = usuario
            self.usuarios_ids.add(usuario.user_id)

    def baja_usuario(self, user_id):
        self.usuarios.pop(user_id, None)
        self.usuarios_ids.discard(user_id)

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            libro = self.libros.pop(isbn)
            self.usuarios[user_id].libros_prestados.append(libro)

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    break   # para no seguir recorriendo innecesariamente

    def buscar_libro(self, criterio, valor):
        return [
            libro for libro in self.libros.values()
            if (criterio == "titulo" and valor.lower() in libro.datos_inmutables[0].lower()) or
               (criterio == "autor" and valor.lower() in libro.datos_inmutables[1].lower()) or
               (criterio == "categoria" and valor.lower() in libro.categoria.lower())
        ]

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            return [libro.datos_inmutables[0] for libro in self.usuarios[user_id].libros_prestados]
        return []


# ---------- PRUEBA ----------
biblio = Biblioteca()
l1 = Libro("Cien años de soledad", "García Márquez", "Novela", "123")
l2 = Libro("El Principito", "Saint-Exupéry", "Fábula", "456")
biblio.anadir_libro(l1)
biblio.anadir_libro(l2)

u1 = Usuario("Ana", "U1")
biblio.registrar_usuario(u1)

biblio.prestar_libro("U1", "123")
print(biblio.listar_libros_prestados("U1"))  # ['Cien años de soledad']
biblio.devolver_libro("U1", "123")
print(biblio.listar_libros_prestados("U1"))  # []

