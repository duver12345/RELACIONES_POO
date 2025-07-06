class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print(f"Hola, soy {self.nombre}")

class SalonDeClases:
    def __init__(self, numero):
        self.numero = numero
        self.estudiantes = []  # Relación de agregación

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        print(f"Estudiantes del salón {self.numero}:")
        for est in self.estudiantes:
            est.presentarse()

# Uso
Anuel = Estudiante("Anuel")
Sara = Estudiante("Sara")

salon101 = SalonDeClases(101)
salon101.agregar_estudiante(Anuel)
salon101.agregar_estudiante(Sara)

salon101.mostrar_estudiantes()
