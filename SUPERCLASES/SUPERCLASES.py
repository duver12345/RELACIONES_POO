class Electrodomestico:  # Superclase
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        print(f"{self.marca} está encendido.")

class Lavadora(Electrodomestico):  # Subclase
    def lavar(self):
        print(f"{self.marca} está lavando la ropa.")

class Microondas(Electrodomestico):  # Subclase
    def calentar(self):
        print(f"{self.marca} está calentando la comida.")