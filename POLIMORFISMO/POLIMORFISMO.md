# **POLIMORFISMO PROGRAMACION ORIENTADA OBJETOS (POO)**

## ¿Qué es?

El polimorfismo es una idea de la programación que significa que una misma acción se puede hacer de distintas maneras, dependiendo del tipo de objeto que la use.

La palabra polimorfismo quiere decir “muchas formas”, y esto ayuda a que los programas sean más flexibles y fáciles de cambiar o mejorar. Por ejemplo, puedes tener varios objetos diferentes que usen el mismo método, pero cada uno lo hace a su manera.

# **Ejemplo**

class Notificacion:
    def enviar(self):
        pass

class Email(Notificacion):
    def enviar(self):
        print("Enviando notificación por correo electrónico.")

class SMS(Notificacion):
    def enviar(self):
        print("Enviando notificación por mensaje de texto (SMS).")

# Lista de distintos tipos de notificación
notificaciones = [Email(), SMS()]

# Se llama al mismo método, pero cada clase lo hace a su manera
for n in notificaciones:
    n.enviar()

