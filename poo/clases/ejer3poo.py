import math
class Ejercicio3:
    def __init__(self):
        self.palabra = ""

    def leerDatos(self):
        pass

    def procesarPalabra(self):
        while True:
            self.palabra = input("Palabra: ")
            if self.palabra == "salir":
                break
            else:
                print(self.palabra)

    def mostrarResultado(self):
        print("Programa finalizado")