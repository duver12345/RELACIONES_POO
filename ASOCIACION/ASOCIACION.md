# 📁 ASOCIACIÓN 
## ¿Qué es?
La asociación es cualquier relación entre dos clases, pero sin dependencia. Las clases se conocen, pero no se contienen entre sí.

## 🧠 Ejemplo:
Un Profesor puede dar clases en una Escuela, pero no la "posee".

## 🧪 Código:

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

class Escuela:
    def __init__(self, nombre):
        self.nombre = nombre

p = Profesor("Sara")
e = Escuela("Escuela 123")
# No hay relación fuerte, solo conocimiento
print(f"{p.nombre} enseña en {e.nombre}")