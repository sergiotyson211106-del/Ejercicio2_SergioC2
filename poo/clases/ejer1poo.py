import math
class Ejercicio1():
    def __init__(self):
        self.x = 0
        self.tolerancia = 0
        self.valorReal = 0
        self.k = 0
        self.aprox = 0
        self.error = 0

    def leerDatos(self):
        self.x = float(input("x="))
        self.tolerancia = float(input("Tolerancia="))
        
        
    def calcularAprox(self):
        self.valorReal = math.sin(self.x)
        self.k = 0
        self.aprox = 0
        while True:
            self.aprox += ((-1)**self.k*self.x**(2*self.k+1))/math.factorial(2*self.k+1)
            self.k += 1
            self.error = math.fabs((self.valorReal - self.aprox)/self.valorReal) * 100
            if self.error < self.tolerancia:
               break

    def mostrarResultado(self):
        print("Valor real = ", self.valorReal)
        print("Aproximación = ", self.aprox)
        print("Error = ", self.error)