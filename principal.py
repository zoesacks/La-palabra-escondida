#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from button import*
from imagenes import*
from funcionesVACIAS import*
from letras import*



os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.display.set_caption("La escondida...")
screen = pygame.display.set_mode((ANCHO, ALTO))


defaultFontGrande= pygame.font.Font("fuente.ttf", TAMANNO_LETRA_GRANDE)
defaultFont= pygame.font.Font( "fuente.ttf", TAMANNO_LETRA)



#esta es la primer pantalla que ve el usuario
def mainInicio():
    while True:
        #si presiona enter vuelve al programa principal donde se habilitan las banderas del menú
        screen.blit(fondo1,(0,0))
        screen.blit(defaultFontGrande.render("Presiona enter para comenzar...", 1, COLOR_VERDE_CLARO), (170, 530))
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_RETURN:
                    return
            if e.type == QUIT:
                    pygame.quit()
        pygame.display.update()



#aca el jugador puede elegir si va a jugar por el largo de palabra o largo aleatorio
def menuprincipal():
    while True:

        aleatorio1 = Button(image=aleatorio,
                            pos=(550, 375),
                            base_color=COLOR_LETRAS,
                            hovering_color=COLOR_LETRAS)

        dificultad1 = Button(image=dificultad,
                            pos=(550, 500),
                            base_color=COLOR_LETRAS,
                            hovering_color=COLOR_LETRAS)

        screen.blit(fondo1,(0,0))
        aleatorio1.update(screen)
        dificultad1.update(screen)

        for e in pygame.event.get():
            if e.type == QUIT:
                    pygame.quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if aleatorio1.checkForInput(pygame.mouse.get_pos()):#el boton de aleatorio te da un largo y despues lo envia al main
                    return True
                if dificultad1.checkForInput(pygame.mouse.get_pos()):#el de dificutad envia a elegirlargo
                    return False

        pygame.display.update()



#aca tiene los botones de mas y menos que van sumando/restando al largo de la palabra
def elegirlargo(largo):
    while True:
        boton_mas = Button(image=mas,
                            pos=(800, 330),
                            base_color=COLOR_LETRAS,
                            hovering_color=COLOR_LETRAS)

        boton_menos = Button(image=menos,
                            pos=(300, 330),
                            base_color=COLOR_LETRAS,
                            hovering_color=COLOR_LETRAS)

        boton_jugar      = Button(image=boton_comenzar,
                            pos=(550, 500),
                            base_color=COLOR_LETRAS,
                            hovering_color=COLOR_LETRAS)

        screen.blit(fondo2,(0,0))
        boton_mas.update(screen)
        boton_menos.update(screen)
        boton_jugar.update(screen)

        screen.blit(defaultFontGrande.render(str(largo), 1, COLOR_NARANJA_CLARO), (525, 290))

        for e in pygame.event.get():
            if e.type == QUIT:
                    pygame.quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if boton_mas.checkForInput(pygame.mouse.get_pos()): #esta restringido para que el maximo sea 20
                    if largo < 20:
                        largo += 1
                if boton_menos.checkForInput(pygame.mouse.get_pos()): #esta restringido para que el minimo sea 2
                    if largo > 2:
                        largo -= 1
                if boton_jugar.checkForInput(pygame.mouse.get_pos()):
                    return largo

        pygame.display.update()




#este es el cartel de que perdio, donde se ve la palabra correcta y si quiere reintentar o abandonar.
def mainPerdio(datos):
    while True:
        reintentar = Button(image=boton_reintentar,
                            pos=(725, 500),
                            base_color=COLOR_LETRAS,
                            hovering_color=COLOR_LETRAS)

        abandonar = Button(image=boton_abandonar,
                            pos=(395, 500),
                            base_color=COLOR_LETRAS,
                            hovering_color=COLOR_LETRAS)

        #fondo y cartel


        screen.blit(fondo3,(0,0))
        screen.blit(cartelper,(180,40))
        #botones
        reintentar.update(screen)
        abandonar.update(screen)
        #texto
        if datos[0] == 0 and datos[1] > 0 : #si no acerto ninguna palabra, se quedo sin tiempo pero con intentos
            screen.blit(defaultFont.render("Te quedaste sin tiempo. La palabra era:" , 1, COLOR_LILA), (210, 300))
            screen.blit(defaultFontGrande.render(datos[2] , 1, COLOR_LILA), (420, 360))
        if datos[0] == 0 and datos[1] == 0 : #si no acerto ninguna palabra, le quedo tiempo pero no intentos
            screen.blit(defaultFont.render("Te quedaste sin intentos. La palabra era:", 1, COLOR_LILA), (210, 300))
            screen.blit(defaultFontGrande.render(datos[2] , 1, COLOR_LILA), (420, 360))
        if datos[0] > 0 : # Si acerto otras palabras antes
            screen.blit(defaultFont.render("Ganaste! La ultima palabra era:" , 1, COLOR_LILA), (275, 300))
            screen.blit(defaultFontGrande.render(datos[2] , 1, COLOR_LILA), (420, 360))
        #puntos
        screen.blit(cartelpuntosChico, (490,220))
        screen.blit(defaultFont.render(str(datos[0]), 1, COLOR_NARANJA_CLARO), (540, 235))

        for e in pygame.event.get():
            if e.type == QUIT:
                    pygame.quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if reintentar.checkForInput(pygame.mouse.get_pos()):
                    return
                if abandonar.checkForInput(pygame.mouse.get_pos()):
                    pygame.quit()

        pygame.display.update()


##La variable largo es el largo de la palabra, y datos es una lista vacía en la que al final se cargará puntos, intentos y palabra correcta para usarlas en la pantalla de perdió.
def main(largo, datos):

        t1 = pygame.time.get_ticks()
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial
        palabraUsuario =""
        listaPalabrasDiccionario=[]
        correctas = []
        incorrectas = []
        casi = []
        puntos = 0

        #lemarios y lectura
        nuevoLemario= "nuevoLemario.txt"
        lemario = "lemario.txt"
        lectura(lemario, listaPalabrasDiccionario, largo)
        gano = False
        intentos = 5
        ListaDePalabrasUsuario=[]
        palabraCorrecta= nuevaPalabra(listaPalabrasDiccionario).lower()#encontre palabras del lemario con mayusculas asi que para asegurarme las converti todas a minisculas
        print(palabraCorrecta)


        while segundos > fps/1000 and intentos > 0 and not gano:

            gameClock.tick(fps)
            totaltime += gameClock.get_time()
            if True:
                fps = 3

            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return()

                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)

                    if (len(palabraUsuario) < largo): #no dejo que ingrese palabras de un largo mayor
                        palabraUsuario = palabraUsuario + letra

                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]

                    if e.key == K_RETURN:

                        if (palabraUsuario in listaPalabrasDiccionario) and (not coinciden(palabraUsuario, ListaDePalabrasUsuario)) and (len(palabraUsuario)==largo):#Reviso que este la palabra en el lemario, que no la halla ingeresado antes y que el largo no se menor al que debe
                            #se revisa si gano, se agrega a lista de palabra de usuario, se borra la palabra de la variable palabra de usuario y se resta un intento
                            gano = revision(palabraCorrecta,palabraUsuario,correctas,incorrectas,casi)
                            ListaDePalabrasUsuario.append(palabraUsuario)
                            palabraUsuario = ""
                            intentos -= 1

                        else: #si no se cumple alguna de las condiciones la palabra que el usuario intento ingresar se borra
                            palabraUsuario = ""




            segundos = TIEMPO_MAX - (pygame.time.get_ticks() - t1)/1000

            screen.blit(fondo4,(0,0))
            ##Estas funciones estan en extras
            escribiendo(screen, palabraUsuario, largo, intentos) #Muestra lo que el jugador va tipiando
            dibujar(screen, puntos, segundos) #Muestra el tiempo y los puntos
            abecedario(screen, ListaDePalabrasUsuario, palabraCorrecta ) #muestra el teclado con los colores correspondientes de las palabras que se arriesgo
            resultado(screen, ListaDePalabrasUsuario, palabraCorrecta, palabraUsuario, gano) #Muestra las palabras que se arriesgo con sus respectivos colores

            pygame.display.flip()

        if gano:
            puntos = puntaje(puntos, intentos)
            datos.append(puntos)
            datos.append(intentos)
            datos.append(palabraCorrecta)
            #si se queda sin tiempo va a la pantalla de perdio
            return datos

        if segundos < 0 or intentos == 0:
            datos.append(puntos)
            datos.append(intentos)
            datos.append(palabraCorrecta)
            #si se queda sin tiempo va a la pantalla de perdio
            return datos

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
        nuevoLemario.close()


pantalla_inicio = True
pantalla_menu = False
pantalla_main = False
pantalla_dificultad = False
pantalla_perdio = False
largo = 2
datos = []


##Desde el programa principal se manejan las distintas pantallas por medio de banderas que se habilitan y deshabilitan dependiendo en cual haya entrado
if __name__ == "__main__":

    if pantalla_inicio == True: #primer pantalla que inicia el juego
        mainInicio()
        pantalla_menu = True
        pantalla_inicio = False

        while True: #las pantallas están en un ciclo ya que si pierde tiene la opción de  volver al menú y volver a jugar entonces esto se vuelve a repetir todo hasta que el jugador salga.


            if pantalla_menu == True: #elige si jugar con un largo aleatorio o eleegirlo

                if menuprincipal() == False: #se habilta la pantalla de elegir el largo
                    pantalla_dificultad = True
                    pantalla_menu = False

                if menuprincipal() == True:
                    largo = random.randint(4, 6) #se da un largo aleatorio, estos valores se pueden cambiar a un minimo de tres y maximo de 20
                    pantalla_main = True
                    pantalla_menu = False

            if pantalla_dificultad == True: #pantalla de elegir largo
                largo = elegirlargo(largo)
                pantalla_main = True
                pantalla_dificultad = False

            if pantalla_main == True: #esta es la pantalla principal del juego
                main(largo, datos)
                pantalla_main = False
                pantalla_perdio = True


            if pantalla_perdio == True: #a esta pantalla va si pierde o gana
                mainPerdio(datos)
                pantalla_menu = True
                pantalla_perdio = False