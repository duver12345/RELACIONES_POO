class Dispositivo:
    def encender(self):
        pass  

# Subclase: Computadora
class Computadora(Dispositivo):
    def encender(self):
        print("Encendiendo la computadora...")

# Subclase: Televisor
class Televisor(Dispositivo):
    def encender(self):
        print("Encendiendo el televisor...")

# Subclase: Consola de videojuegos
class Consola(Dispositivo):
    def encender(self):
        print("Encendiendo la consola de videojuegos...")

# Lista de dispositivos
dispositivos = [Computadora(), Televisor(), Consola()]

# Se llama al mismo método, y cada uno responde según su clase
for d in dispositivos:
    d.encender()