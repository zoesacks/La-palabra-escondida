import os, random, sys, math

import pygame
from pygame.locals import *


boton_reintentar = pygame.image.load("imagenes/reintentar.png")
boton_abandonar = pygame.image.load("imagenes/abandonar.png")
boton_siguiente = pygame.image.load("imagenes/siguiente.png")
boton_comenzar = pygame.image.load("imagenes/comenzar.png")


fondo1 = pygame.image.load("imagenes/fondo1.png")
fondo2 = pygame.image.load("imagenes/fondo2.png")
fondo3 = pygame.image.load("imagenes/fondo3.png")
fondo4 = pygame.image.load("imagenes/fondo4.png")

carteltiempo = pygame.image.load("imagenes/cartelTiempo.png")
cartelpuntos = pygame.image.load("imagenes/cartelPuntos.png")

carteltiempoChico = pygame.transform.scale(carteltiempo, [120, 70])
cartelpuntosChico = pygame.transform.scale(cartelpuntos, [120, 70])

aleatorio = pygame.image.load("imagenes/aleatorio.png")
dificultad = pygame.image.load("imagenes/dificultad.png")

mas = pygame.image.load("imagenes/mas.png")
menos = pygame.image.load("imagenes/menos.png")

cartelper = pygame.image.load("imagenes/cartelPerdio.png")
cartelgan = pygame.image.load("imagenes/cartelgano.png")