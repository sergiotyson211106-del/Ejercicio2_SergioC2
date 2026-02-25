import math
def leerValores():
  n=int(input("Profundidad del pozo(pulg)="))
  u=int(input("Energía(pulg/min)="))
  return n,u

def calcularTiempo(n,u):
  d = 1
  ascenso=0
  tiempo  = 0
  while True:
    ascenso += u #desplazamiento hacia arriba
    tiempo += 1  #Tiempo de ascenso
    if ascenso >= n:  #Si llegó a la cima sale del ciclo
      break;
    ascenso -= d #Desplazamiento hacia abajo
    tiempo += 1  #Tiempo de descanso
  return tiempo

def mostrarResultado(tiempo):
  print("Tiempo en salir:",tiempo)

def ejercicio_4(): 
    n,u = leerValores()
    tiempo = calcularTiempo(n,u)
    mostrarResultado(tiempo)