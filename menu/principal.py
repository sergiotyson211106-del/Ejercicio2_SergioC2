from ejercicios.ejercicio1 import ejercicio_1
from ejercicios.ejercicio2 import ejercicio_2
from ejercicios.ejercicio3 import ejercicio_3
from ejercicios.ejercicio4 import ejercicio_4
# Refereciar la clase 
from poo.clases.ejer1poo import Ejercicio1
from poo.clases.ejer2poo import Ejercicio2
from poo.clases.ejer3poo import Ejercicio3
from poo.clases.ejer4poo import Ejercicio4
#  carpeta carpeta carpeta      clase

def menuPrincipal():
    while True:
        print("\n :: Menu ::")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Salir")
        
        op = int(input("Ingrese la opcion deseada: "))
        match(op):
            case 1:
                #Lamada a la funcion 
                #Ejercicio_1()
                
                #Crea el objeto de la clase 
                e1 = Ejercicio1()
                #Llamada a los metodos 
                e1.leerDatos()
                e1.calcularAprox()
                e1.mostrarResultado()
                
            case 2:
                 e2 = Ejercicio2()
                 e2.leerDatos()
                 e2.verificarPassword()
                 e2.mostrarResultado()
                 
            case 3:
                e3 = Ejercicio3()
                e3.leerDatos()
                e3.procesarPalabra()
                e3.mostrarResultado()
                
            case 4:
                e4 = Ejercicio4()
                e4.leerDatos()
                e4.calcularTiempo()
                e4.mostrarResultado()
                
            case 5:
                print("Hasta pronto")
                break
            case _:
                print("Ingrese un dato valido")

