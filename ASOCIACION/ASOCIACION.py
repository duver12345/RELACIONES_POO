class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

    def escribir_libro(self, titulo):
        return Libro(titulo, self)

class Libro:
    def __init__(self, titulo, autor=None):
        self.titulo = titulo
        self.autor = autor

# Uso
autor = Autor("Gabriel García Márquez")
libro = autor.escribir_libro("Cien años de soledad")
print(f"{libro.titulo} fue escrito por {libro.autor.nombre}")