print("Ejemplo de juego de preguntas creado con Python.")
nombre_jugador = input("¿Cual es tu nombre?\n" )

print("Que empiece el juego. Elige la respuesta correcta y gana el maximo de puntos")

puntuacion = 0
respuesta = None
##########Primera pregunta.
print("¿De que color es el cielo?\n"
      "A: Verde\n"
      "B: Azul\n"
      "C: Marron\n")

while respuesta != "A" and respuesta != "a" and  respuesta != "B" and respuesta != "b" and respuesta != "C" and respuesta != "c":
    respuesta = input("Elige A,B o C\n")

if respuesta == "A" or "a":
    puntuacion += 0

if respuesta == "B" or "b":
    puntuacion += 1

if respuesta == "C" or "c":
    puntuacion += 0

#########Segunda pregunta
respuesta = None
print("¿De que colores es la bandera de Mexico?\n"
      "A: amarillo, blanco y rojo\n"
      "B: verde, blanco y azul\n"
      "C: verde, blanco y rojo\n")

while respuesta != "A" and respuesta != "a" and respuesta != "B" and respuesta != "b" and respuesta != "C" and respuesta != "c":
    respuesta = input("Elige A,B o C\n")

if respuesta == "A" or "a":
    puntuacion += 0

if respuesta == "B" or "b":
    puntuacion += 0

if respuesta == "C" or "c":
    puntuacion += 1

#########Tercera pregunta
respuesta = None
print("¿Cuando acabo la II Guerra Mundial?\n"
      "A: 1945\n"
      "B: 1942\n"
      "C: 1946\n")

while respuesta != "A" and respuesta != "a" and respuesta != "B" and respuesta != "b" and respuesta != "C" and respuesta != "c":
    respuesta = input("Elige A,B o C\n")

if respuesta == "A" or "a":
    puntuacion += 1

if respuesta == "B" or "b":
    puntuacion += 0

if respuesta == "C" or "c":
    puntuacion += 0

#########Cuarta pregunta
respuesta = None
print("¿Como se denomina el resultado de la multiplicacion?\n"
      "A: Parciales\n"
      "B: Multiplicador\n"
      "C: producto\n")

while respuesta != "A" and respuesta != "a" and respuesta != "B" and respuesta != "b" and respuesta != "C" and respuesta != "c":
    respuesta = input("Elige A,B o C\n")

if respuesta == "A" or "a":
    puntuacion += 0

if respuesta == "B" or "b":
    puntuacion += 0

if respuesta == "C" or "c":
    puntuacion += 1
print("Ya queda poco.")


#########Quinta pregunta
respuesta = None
print("¿Que año llego Cristobal Colon a America?\n"
      "A: 1492\n"
      "B: 1590\n"
      "C: 1495\n")

while respuesta != "A" and respuesta != "a" and respuesta != "B" and respuesta != "b" and respuesta != "C" and respuesta != "c":
    respuesta = input("Elige A,B o C\n")

if respuesta == "A" or "a":
    puntuacion += 1

if respuesta == "B" or "b":
    puntuacion += 0

if respuesta == "C" or "c":
    puntuacion += 0

#########Sexta pregunta
respuesta = None
print("¿Cual es el color que representa la esperanza?\n"
      "A: Verde\n"
      "B: Blanco\n"
      "C: Azul\n")

while respuesta != "A" and respuesta != "a" and respuesta != "B" and respuesta != "b" and respuesta != "C" and respuesta != "c":
    respuesta = input("Elige A,B o C\n")

if respuesta == "A" or "a":
    puntuacion += 1

if respuesta == "B" or "b":
    puntuacion += 0

if respuesta == "C" or "c":
    puntuacion += 0

print("La puntuacion de {} es de {}".format(nombre_jugador,puntuacion))