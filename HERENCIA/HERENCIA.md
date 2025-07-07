# **HERENCIA PROGRAMACION ORIENTADA OBJETOS (POO)**

## ¿Qué es?

La herencia es un concepto clave en la Programación Orientada a Objetos que permite construir nuevas clases a partir de clases ya existentes. Gracias a esto, no es necesario volver a escribir el mismo código, ya que las clases hijas (también llamadas subclases) pueden heredar los atributos y métodos de una clase padre (o superclase).

## ¿Qué puede hacer una clase hija?

Reutilizar código de la clase padre.
-Agregar sus propios atributos y métodos, específicos de su función.
-Modificar el comportamiento de métodos heredados, a través de un proceso llamado sobrescritura (override).

## Ventajas de la herencia:

-Permite organizar el código de forma jerárquica, de lo general a lo particular.
-Mejora la claridad y estructura del programa.
-Facilita la mantenibilidad y escalabilidad del software.
-Favorece la reutilización de componentes existentes.

## **Ejemplo**
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        print(f"El vehículo {self.marca} está encendido.")

class Moto(Vehiculo):
    def hacer_ruido(self):
        print(f"La moto {self.marca} hace: ¡Brrrrr!")