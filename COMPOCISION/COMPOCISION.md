# 📁 COMPOSICIÓN
## ¿Qué es?
La composición es una relación fuerte. Una clase contiene a otra y si desaparece, la otra también lo hace. Es una relación de dependencia total.

## 🧠 Ejemplo:
Una Casa tiene Habitaciones. Si la casa se destruye, las habitaciones también.

## 🧪 Código:

class Habitacion:
    def __init__(self, nombre):
        self.nombre = nombre

class Casa:
    def __init__(self):
        self.habitaciones = [Habitacion("Sala"), Habitacion("Cuarto")]

c = Casa()
print(c.habitaciones[0].nombre)
