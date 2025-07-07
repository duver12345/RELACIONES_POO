**SuperClases PROGRAMACION ORIENTADA OBJETOS (POO)**

¿Qué es?

Una superclase es una clase más general o principal, de la que otras clases más específicas toman sus características y comportamientos.
Funciona como un modelo base que permite organizar el código de forma ordenada y reducir la repetición, ya que lo común se define una sola vez.

**Ejemplo**

class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar(self):
        print(f"El {self.nombre} está sonando.")

class Guitarra(Instrumento):
    def rasguear(self):
        print("Rasgueando las cuerdas de la guitarra.")

class Piano(Instrumento):
    def presionar_teclas(self):
        print("Presionando las teclas del piano.")

