import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from letras import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SLASH:
        return("-")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")



def dibujar(screen, puntos, segundos):
    defaultFontGrande= pygame.font.Font("fuente.ttf", TAMANNO_LETRA_GRANDE)
    defaultFont= pygame.font.Font( "fuente.ttf", TAMANNO_LETRA)

    screen.blit(carteltiempo,(20,20))
    screen.blit(cartelpuntos,(930,20))

    screen.blit(defaultFont.render( str(puntos), 1, COLOR_NARANJA_CLARO), (990, 40))
    screen.blit(defaultFontGrande.render(str(int(segundos)), 1, COLOR_LILA), (55, 35))



def abecedario(screen, listaDePalabrasUsuario, palabraCorrecta):
    correctas = []
    incorrectas = []
    casi = []
    linea1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
    linea2 = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ñ"]
    linea3 = ["z", "x", "c", "v", "b", "n", "m"]
    abecdario = [linea1, linea2, linea3]
    pos = 0
    aba = 420
    for pal in listaDePalabrasUsuario:
        revisionLetra(palabraCorrecta, pal, correctas, incorrectas, casi)
    for linea in abecdario:
        aba += 50
        pos = ANCHO//2-len(linea)*25
        for letra in linea:
            if coinciden(letra, correctas):
                letraCorrectaChica(letra, pos, aba, screen)
                pos += 50
            if coinciden(letra, incorrectas) and (not coinciden(letra, correctas)) and (not coinciden(letra, casi)):
                letraIncorrectaChica(letra, pos, aba, screen)
                pos += 50
            if (coinciden(letra, casi)) and (not coinciden(letra, correctas)):
                letraCasiChica(letra, pos, aba, screen)
                pos += 50
            if (not coinciden(letra, correctas)) and (not coinciden(letra, incorrectas)) and (not coinciden(letra, casi)):
                letraNeutraChica(letra, pos, aba, screen)
                pos += 50


def resultado(screen, listaDePalabrasUsuario, palabraCorrecta, palabra, gano):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)
    pos = 200
    aba = 170
    cont = 4
    cant = 0
    for pal in listaDePalabrasUsuario:
        correctas = []
        incorrectas = []
        casi = []
        revision(palabraCorrecta,pal,correctas,incorrectas,casi)
        pos = ANCHO//2-len(palabraCorrecta)*30
        aba -= 60
        for y in range(len(pal)):
            if coinciden(y, correctas):
                letraCorrecta(pal[y], pos, aba, screen)
                pos += 60
            elif coinciden(y, casi):
                letraCasi(pal[y], pos, aba, screen)
                pos += 60
            else:
                letraIncorrecta(pal[y], pos, aba, screen)
                pos += 60
        cont -= 1
        aba += 120
        
    while cont > 0:
        pos = ANCHO//2-len(palabraCorrecta)*30
        cant = len(palabraCorrecta)
        vacia(pos, aba, cant, screen)
        cont -= 1
        aba += 60


def escribiendo(screen, palabraUsuario, largo, intentos):
    aba = 110 + (5 - intentos)*60
    pos = ANCHO//2-largo*30
    cont = largo
    for let in palabraUsuario:
        letraNeutra(let, pos, aba, screen)
        pos+=60
        cont -= 1
    while cont > 0:
        vacia(pos, aba, cont, screen)
        pos += 60
        cont -= 1






