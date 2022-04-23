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

while respuesta != "A" and respuesta != "a" and respuesta != "B" and respuesta != "b" and respuesta != "C" and respuesta != "c":
    respuesta = input("Elige A,B o C")

if respuesta == "A" or "a":
    puntuacion += 0

elif respuesta == "B" or "b":
    puntuacion += 1

elif respuesta == "C" or "c":
    puntuacion += 0

#########Segunda pregunta

print("¿De qué colores es la bandera de México?\n"
      "A: amarillo, blanco y rojo\n"
      "B: verde, blanco y azul\n"
      "C: verde, blanco y rojo\n")

while respuesta != "A" and respuesta != "a" and respuesta != "B" and respuesta != "b" and respuesta != "C" and respuesta != "c":
    respuesta = input("Elige A,B o C")

if respuesta == "A" or "a":
    puntuacion += 0

elif respuesta == "B" or "b":
    puntuacion += 0

elif respuesta == "C" or "c":
    puntuacion += 1

#########Tercera pregunta

print("¿Cuándo acabó la II Guerra Mundial?\n"
      "A: 1945\n"
      "B: 1942\n"
      "C: 1946\n")

while respuesta != "A" and respuesta != "a" and respuesta != "B" and respuesta != "b" and respuesta != "C" and respuesta != "c":
    respuesta = input("Elige A,B o C")

if respuesta == "A" or "a":
    puntuacion += 1

elif respuesta == "B" or "b":
    puntuacion += 0

elif respuesta == "C" or "c":
    puntuacion += 0

print("La puntuacion de {} es de {}".format(nombre_jugador,puntuacion))