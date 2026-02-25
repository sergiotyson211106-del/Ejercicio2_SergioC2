import math
def asignarDatos():
  password = "lunes"
  intentos = 0
  palabra = ""
  return password,intentos,palabra

def mostrarMensaje(password,intentos,palabra):
  while palabra != password:
    palabra = input("Contraseña:")
    intentos += 1
    if intentos == 5:
      print("Excediste las oportunidades")
      break

def ejercicio_2():
    password,intentos,palabra = asignarDatos()
    mostrarMensaje(password,intentos,palabra)