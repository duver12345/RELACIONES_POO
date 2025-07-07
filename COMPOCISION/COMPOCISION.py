class Item:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Orden:
    def __init__(self, id_orden):
        self.id = id_orden
        self.items = []

    def agregar_item(self, nombre, precio):
        self.items.append(Item(nombre, precio))

# Uso
orden = Orden(101)
orden.agregar_item("Cuaderno", 5.0)
orden.agregar_item("Lápiz", 1.0)
for item in orden.items:
    print(f"{item.nombre}: ${item.precio}")
