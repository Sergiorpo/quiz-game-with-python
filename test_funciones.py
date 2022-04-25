############ Ejemplo juego de preguntas ##################

print("Ejemplo de juego de preguntas creado con Python.")

############ Variables ############
puntuacion = 0
nombre_jugador = input("¿Cual es tu nombre?\n" )
######### FUNCIONES #######
def funcionA():
    global puntuacion
    if pregunta == "A" and "a":
        puntuacion += 1
    else:
        puntuacion += 0

def funcionB():
    global puntuacion
    if pregunta == "B" and "b":
        puntuacion += 1
    else:
        puntuacion += 0

def funcionC():
    global puntuacion
    if pregunta == "C" and "c":
        puntuacion += 1
    else:
        puntuacion += 0


print("Que empiece el juego. Elige la respuesta correcta y gana el maximo de puntos")
###### Primera Pregunta #######
print("¿De que color es el cielo?\n"
      "A: Verde\n"
      "B: Azul\n"
      "C: Marron\n")
pregunta = None
while pregunta != "A" and pregunta != "B" and pregunta != "C" and pregunta != "a" and pregunta != "b" and pregunta != "c":
    pregunta = input("Elige A,B o C \n")

funcionB()

###### Segunda Pregunta #######
print("¿De que colores es la bandera de Mexico?\n"
      "A: amarillo, blanco y rojo\n"
      "B: verde, blanco y azul\n"
      "C: verde, blanco y rojo\n")
pregunta = None
while pregunta != "A" and pregunta != "B" and pregunta != "C" and pregunta != "a" and pregunta != "b" and pregunta != "c":
    pregunta = input("Elige A,B o C \n")

funcionC()

###### Tercera Pregunta #######
print("¿Cuando acabo la II Guerra Mundial?\n"
      "A: 1945\n"
      "B: 1942\n"
      "C: 1946\n")
pregunta = None
while pregunta != "A" and pregunta != "B" and pregunta != "C" and pregunta != "a" and pregunta != "b" and pregunta != "c":
    pregunta = input("Elige A,B o C \n")

funcionA()

print("La puntuacion de {} es de {}".format(nombre_jugador,puntuacion))