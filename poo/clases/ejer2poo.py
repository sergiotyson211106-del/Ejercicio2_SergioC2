import math
class Ejercicio2():
    def __init__(self):
        self.password = "lunes"
        self.intentos = 0
        self.palabra = ""

    def leerDatos(self):
        pass

    def verificarPassword(self):
        while self.palabra != self.password:
            self.palabra = input("Contraseña: ")
            self.intentos += 1

            if self.intentos == 5 and self.palabra != self.password:
                print("Excediste las oportunidades")
                break

    def mostrarResultado(self):
        if self.palabra == self.password:
            print("Acceso concedido")
        else:
            print("Acceso denegado")
