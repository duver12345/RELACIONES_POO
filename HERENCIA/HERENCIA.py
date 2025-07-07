class Vehiculo:
    def __init__(self, marca):
        self.marca = marca  

    def encender(self):
        print(f"El vehículo {self.marca} está encendido.")

# Clase derivada o subclase: Moto
class Moto(Vehiculo):
    def hacer_ruido(self):
        print(f"La moto {self.marca} hace: ¡Brrrrr!")

# Clase derivada o subclase: Carro
class Carro(Vehiculo):
    def tocar_claxon(self):
        print(f"El carro {self.marca} toca el claxon: ¡Piiii!")