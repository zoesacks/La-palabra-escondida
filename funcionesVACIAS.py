
from configuracion import *
import random
import math

#recibe una lista de palabras y devuelve una de ellas elegida al azar
def nuevaPalabra(lista):
    palabraCorrecta = random.choice(lista)
    return(palabraCorrecta)

#toma el archivo y lo guarda en entrada
def lectura(archivo,salida,largo):
    with open(archivo,"r") as entrada: 
        for linea in entrada:
            if len(linea)==largo+1:
                salida.append(linea[:-1])


def coinciden(x,lista):
    for i in lista:
        if i == x:
            return True
    return False


def revision(palabraCorrecta,palabra, correcta, incorrecta, casi): #esta revision funciona con indices y la otra directamente con la letra
    if palabraCorrecta == palabra:
        return True
    else:
        for i in range(len(palabra)):
            if coinciden(palabra[i],palabraCorrecta):
                if palabra[i] == palabraCorrecta[i]:
                    correcta.append(i)
                else:
                    casi.append(i)
            else:
                incorrecta.append(i)
    return False

def revisionLetra(palabraCorrecta, palabra, correcta, incorrecta, casi ):
    for i in range(len(palabra)):
        if coinciden(palabra[i], palabraCorrecta):
            if palabra[i] == palabraCorrecta[i]:
                correcta.append(palabra[i])
            else:
                casi.append(palabra[i])
        else:
            incorrecta.append(palabra[i])

def puntaje(puntos, intentos):
    puntos += ((intentos)*10)
    return puntos



