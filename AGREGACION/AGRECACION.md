# 📁 AGREGACIÓN 
## ¿Qué es?
La agregación es una relación débil entre clases. Una clase "tiene" otra, pero pueden existir por separado. Por ejemplo, una universidad tiene estudiantes, pero si la universidad desaparece, los estudiantes siguen existiendo.

## 🧠 Ejemplo:
Una Universidad tiene muchos Estudiantes.

## 🧪 Código:

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

u = Universidad("U Central")
e1 = Estudiante("Juan")
u.agregar_estudiante(e1)





