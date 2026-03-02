import math
class Ejercicio4:
    def __init__(self):
        self.n = 0          
        self.u = 0         
        self.d = 1          
        self.ascenso = 0
        self.tiempo = 0

    def leerDatos(self):
        self.n = int(input("Profundidad del pozo (pulg): "))
        self.u = int(input("Energía (pulg/min): "))

    def calcularTiempo(self):
        self.ascenso = 0
        self.tiempo = 0

        while True:
            self.ascenso += self.u   
            self.tiempo += 1         

            if self.ascenso >= self.n:
                break

            self.ascenso -= self.d   
            self.tiempo += 1         

    def mostrarResultado(self):
        print("Tiempo en salir:", self.tiempo)