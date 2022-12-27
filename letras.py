import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from button import*
from imagenes import*
from funcionesVACIAS import*

def get_font(size): #Utilizamos una fuente externa al SO
    return pygame.font.Font("font.ttf", size)

def vacia(pos, aba, cant, screen):
    vac = pygame.image.load("imagenes/0.png")
    vac = pygame.transform.scale(vac, [50, 50])
    for x in range(cant):
        screen.blit(vac,[pos, aba])
        pos += 60

def letraNeutraChica(let, pos, aba, screen):
    if let == "a":
        a = pygame.image.load("imagenes/1A.png")
        a = pygame.transform.scale(a, [40, 40])
        screen.blit(a,[pos, aba])
    if let == "b":
        b = pygame.image.load("imagenes/1B.png")
        b = pygame.transform.scale(b, [40, 40])
        screen.blit(b,[pos, aba])
    if let == "c":
        c = pygame.image.load("imagenes/1C.png")
        c = pygame.transform.scale(c, [40, 40])
        screen.blit(c,[pos, aba])
    if let == "d":
        d = pygame.image.load("imagenes/1D.png")
        d = pygame.transform.scale(d, [40, 40])
        screen.blit(d,[pos, aba])
    if let == "e":
        e = pygame.image.load("imagenes/1E.png")
        e = pygame.transform.scale(e, [40, 40])
        screen.blit(e,[pos, aba])
    if let == "f":
        f = pygame.image.load("imagenes/1F.png")
        f = pygame.transform.scale(f, [40, 40])
        screen.blit(f,[pos, aba])
    if let == "g":
        g = pygame.image.load("imagenes/1G.png")
        g = pygame.transform.scale(g, [40, 40])
        screen.blit(g,[pos, aba])
    if let == "h":
        h = pygame.image.load("imagenes/1H.png")
        h = pygame.transform.scale(h, [40, 40])
        screen.blit(h,[pos, aba])
    if let == "i":
        i = pygame.image.load("imagenes/1I.png")
        i = pygame.transform.scale(i, [40, 40])
        screen.blit(i,[pos, aba])
    if let == "j":
        j = pygame.image.load("imagenes/1J.png")
        j = pygame.transform.scale(j, [40, 40])
        screen.blit(j,[pos, aba])
    if let == "k":
        k = pygame.image.load("imagenes/1K.png")
        k = pygame.transform.scale(k, [40, 40])
        screen.blit(k,[pos, aba])
    if let == "l":
        l = pygame.image.load("imagenes/1L.png")
        l = pygame.transform.scale(l, [40, 40])
        screen.blit(l,[pos, aba])
    if let == "m":
        m = pygame.image.load("imagenes/1M.png")
        m = pygame.transform.scale(m, [40, 40])
        screen.blit(m,[pos, aba])
    if let == "n":
        n = pygame.image.load("imagenes/1N.png")
        n = pygame.transform.scale(n, [40, 40])
        screen.blit(n,[pos, aba])
    if let == "ñ":
        ñ = pygame.image.load("imagenes/1Ñ.png")
        ñ = pygame.transform.scale(ñ, [40, 40])
        screen.blit(ñ,[pos, aba])
    if let == "o":
        o = pygame.image.load("imagenes/1O.png")
        o = pygame.transform.scale(o, [40, 40])
        screen.blit(o,[pos, aba])
    if let == "p":
        p = pygame.image.load("imagenes/1P.png")
        p = pygame.transform.scale(p, [40, 40])
        screen.blit(p,[pos, aba])
    if let == "q":
        q = pygame.image.load("imagenes/1Q.png")
        q = pygame.transform.scale(q, [40, 40])
        screen.blit(q,[pos, aba])
    if let == "r":
        r = pygame.image.load("imagenes/1R.png")
        r = pygame.transform.scale(r, [40, 40])
        screen.blit(r,[pos, aba])
    if let == "s":
        s = pygame.image.load("imagenes/1S.png")
        s = pygame.transform.scale(s, [40, 40])
        screen.blit(s,[pos, aba])
    if let == "t":
        t = pygame.image.load("imagenes/1T.png")
        t = pygame.transform.scale(t, [40, 40])
        screen.blit(t,[pos, aba])
    if let == "u":
        u = pygame.image.load("imagenes/1U.png")
        u = pygame.transform.scale(u, [40, 40])
        screen.blit(u,[pos, aba])
    if let == "v":
        v = pygame.image.load("imagenes/1V.png")
        v = pygame.transform.scale(v, [40, 40])
        screen.blit(v,[pos, aba])
    if let == "w":
        w = pygame.image.load("imagenes/1W.png")
        w = pygame.transform.scale(w, [40, 40])
        screen.blit(w,[pos, aba])
    if let == "x":
        x = pygame.image.load("imagenes/1X.png")
        x = pygame.transform.scale(x, [40, 40])
        screen.blit(x,[pos, aba])
    if let == "y":
        y = pygame.image.load("imagenes/1Y.png")
        y = pygame.transform.scale(y, [40, 40])
        screen.blit(y,[pos, aba])
    if let == "z":
        z = pygame.image.load("imagenes/1Z.png")
        z = pygame.transform.scale(z, [40, 40])
        screen.blit(z,[pos, aba])

def letraNeutra(let, pos, aba, screen):
    if let == "a":
        a = pygame.image.load("imagenes/1A.png")
        a = pygame.transform.scale(a, [50, 50])
        screen.blit(a,[pos, aba])
    if let == "b":
        b = pygame.image.load("imagenes/1B.png")
        b = pygame.transform.scale(b, [50, 50])
        screen.blit(b,[pos, aba])
    if let == "c":
        c = pygame.image.load("imagenes/1C.png")
        c = pygame.transform.scale(c, [50, 50])
        screen.blit(c,[pos, aba])
    if let == "d":
        d = pygame.image.load("imagenes/1D.png")
        d = pygame.transform.scale(d, [50, 50])
        screen.blit(d,[pos, aba])
    if let == "e":
        e = pygame.image.load("imagenes/1E.png")
        e = pygame.transform.scale(e, [50, 50])
        screen.blit(e,[pos, aba])
    if let == "f":
        f = pygame.image.load("imagenes/1F.png")
        f = pygame.transform.scale(f, [50, 50])
        screen.blit(f,[pos, aba])
    if let == "g":
        g = pygame.image.load("imagenes/1G.png")
        g = pygame.transform.scale(g, [50, 50])
        screen.blit(g,[pos, aba])
    if let == "h":
        h = pygame.image.load("imagenes/1H.png")
        h = pygame.transform.scale(h, [50, 50])
        screen.blit(h,[pos, aba])
    if let == "i":
        i = pygame.image.load("imagenes/1I.png")
        i = pygame.transform.scale(i, [50, 50])
        screen.blit(i,[pos, aba])
    if let == "j":
        j = pygame.image.load("imagenes/1J.png")
        j = pygame.transform.scale(j, [50, 50])
        screen.blit(j,[pos, aba])
    if let == "k":
        k = pygame.image.load("imagenes/1K.png")
        k = pygame.transform.scale(k, [50, 50])
        screen.blit(k,[pos, aba])
    if let == "l":
        l = pygame.image.load("imagenes/1L.png")
        l = pygame.transform.scale(l, [50, 50])
        screen.blit(l,[pos, aba])
    if let == "m":
        m = pygame.image.load("imagenes/1M.png")
        m = pygame.transform.scale(m, [50, 50])
        screen.blit(m,[pos, aba])
    if let == "n":
        n = pygame.image.load("imagenes/1N.png")
        n = pygame.transform.scale(n, [50, 50])
        screen.blit(n,[pos, aba])
    if let == "ñ":
        ñ = pygame.image.load("imagenes/1Ñ.png")
        ñ = pygame.transform.scale(ñ, [50, 50])
        screen.blit(ñ,[pos, aba])
    if let == "o":
        o = pygame.image.load("imagenes/1O.png")
        o = pygame.transform.scale(o, [50, 50])
        screen.blit(o,[pos, aba])
    if let == "p":
        p = pygame.image.load("imagenes/1P.png")
        p = pygame.transform.scale(p, [50, 50])
        screen.blit(p,[pos, aba])
    if let == "q":
        q = pygame.image.load("imagenes/1Q.png")
        q = pygame.transform.scale(q, [50, 50])
        screen.blit(q,[pos, aba])
    if let == "r":
        r = pygame.image.load("imagenes/1R.png")
        r = pygame.transform.scale(r, [50, 50])
        screen.blit(r,[pos, aba])
    if let == "s":
        s = pygame.image.load("imagenes/1S.png")
        s = pygame.transform.scale(s, [50, 50])
        screen.blit(s,[pos, aba])
    if let == "t":
        t = pygame.image.load("imagenes/1T.png")
        t = pygame.transform.scale(t, [50, 50])
        screen.blit(t,[pos, aba])
    if let == "u":
        u = pygame.image.load("imagenes/1U.png")
        u = pygame.transform.scale(u, [50, 50])
        screen.blit(u,[pos, aba])
    if let == "v":
        v = pygame.image.load("imagenes/1V.png")
        v = pygame.transform.scale(v, [50, 50])
        screen.blit(v,[pos, aba])
    if let == "w":
        w = pygame.image.load("imagenes/1W.png")
        w = pygame.transform.scale(w, [50, 50])
        screen.blit(w,[pos, aba])
    if let == "x":
        x = pygame.image.load("imagenes/1X.png")
        x = pygame.transform.scale(x, [50, 50])
        screen.blit(x,[pos, aba])
    if let == "y":
        y = pygame.image.load("imagenes/1Y.png")
        y = pygame.transform.scale(y, [50, 50])
        screen.blit(y,[pos, aba])
    if let == "z":
        z = pygame.image.load("imagenes/1Z.png")
        z = pygame.transform.scale(z, [50, 50])
        screen.blit(z,[pos, aba])

def letraCorrectaChica(let, pos, aba, screen):
    if let == "a":
        a = pygame.image.load("imagenes/2A.png")
        a = pygame.transform.scale(a, [40, 40])
        screen.blit(a,[pos, aba])
    if let == "b":
        b = pygame.image.load("imagenes/2B.png")
        b = pygame.transform.scale(b, [40, 40])
        screen.blit(b,[pos, aba])
    if let == "c":
        c = pygame.image.load("imagenes/2C.png")
        c = pygame.transform.scale(c, [40, 40])
        screen.blit(c,[pos, aba])
    if let == "d":
        d = pygame.image.load("imagenes/2D.png")
        d = pygame.transform.scale(d, [40, 40])
        screen.blit(d,[pos, aba])
    if let == "e":
        e = pygame.image.load("imagenes/2E.png")
        e = pygame.transform.scale(e, [40, 40])
        screen.blit(e,[pos, aba])
    if let == "f":
        f = pygame.image.load("imagenes/2F.png")
        f = pygame.transform.scale(f, [40, 40])
        screen.blit(f,[pos, aba])
    if let == "g":
        g = pygame.image.load("imagenes/2G.png")
        g = pygame.transform.scale(g, [40, 40])
        screen.blit(g,[pos, aba])
    if let == "h":
        h = pygame.image.load("imagenes/2H.png")
        h = pygame.transform.scale(h, [40, 40])
        screen.blit(h,[pos, aba])
    if let == "i":
        i = pygame.image.load("imagenes/2I.png")
        i = pygame.transform.scale(i, [40, 40])
        screen.blit(i,[pos, aba])
    if let == "j":
        j = pygame.image.load("imagenes/2J.png")
        j = pygame.transform.scale(j, [40, 40])
        screen.blit(j,[pos, aba])
    if let == "k":
        k = pygame.image.load("imagenes/2K.png")
        k = pygame.transform.scale(k, [40, 40])
        screen.blit(k,[pos, aba])
    if let == "l":
        l = pygame.image.load("imagenes/2L.png")
        l = pygame.transform.scale(l, [40, 40])
        screen.blit(l,[pos, aba])
    if let == "m":
        m = pygame.image.load("imagenes/2M.png")
        m = pygame.transform.scale(m, [40, 40])
        screen.blit(m,[pos, aba])
    if let == "n":
        n = pygame.image.load("imagenes/2N.png")
        n = pygame.transform.scale(n, [40, 40])
        screen.blit(n,[pos, aba])
    if let == "ñ":
        ñ = pygame.image.load("imagenes/2Ñ.png")
        ñ = pygame.transform.scale(ñ, [40, 40])
        screen.blit(ñ,[pos, aba])
    if let == "o":
        o = pygame.image.load("imagenes/2O.png")
        o = pygame.transform.scale(o, [40, 40])
        screen.blit(o,[pos, aba])
    if let == "p":
        p = pygame.image.load("imagenes/2P.png")
        p = pygame.transform.scale(p, [40, 40])
        screen.blit(p,[pos, aba])
    if let == "q":
        q = pygame.image.load("imagenes/2Q.png")
        q = pygame.transform.scale(q, [40, 40])
        screen.blit(q,[pos, aba])
    if let == "r":
        r = pygame.image.load("imagenes/2R.png")
        r = pygame.transform.scale(r, [40, 40])
        screen.blit(r,[pos, aba])
    if let == "s":
        s = pygame.image.load("imagenes/2S.png")
        s = pygame.transform.scale(s, [40, 40])
        screen.blit(s,[pos, aba])
    if let == "t":
        t = pygame.image.load("imagenes/2T.png")
        t = pygame.transform.scale(t, [40, 40])
        screen.blit(t,[pos, aba])
    if let == "u":
        u = pygame.image.load("imagenes/2U.png")
        u = pygame.transform.scale(u, [40, 40])
        screen.blit(u,[pos, aba])
    if let == "v":
        v = pygame.image.load("imagenes/2V.png")
        v = pygame.transform.scale(v, [40, 40])
        screen.blit(v,[pos, aba])
    if let == "w":
        w = pygame.image.load("imagenes/2W.png")
        w = pygame.transform.scale(w, [40, 40])
        screen.blit(w,[pos, aba])
    if let == "x":
        x = pygame.image.load("imagenes/2X.png")
        x = pygame.transform.scale(x, [40, 40])
        screen.blit(x,[pos, aba])
    if let == "y":
        y = pygame.image.load("imagenes/2Y.png")
        y = pygame.transform.scale(y, [40, 40])
        screen.blit(y,[pos, aba])
    if let == "z":
        z = pygame.image.load("imagenes/2Z.png")
        z = pygame.transform.scale(z, [40, 40])
        screen.blit(z,[pos, aba])

def letraCorrecta(let, pos, aba, screen):
    if let == "a":
        a = pygame.image.load("imagenes/2A.png")
        screen.blit(a,[pos, aba])
    if let == "b":
        b = pygame.image.load("imagenes/2B.png")
        screen.blit(b,[pos, aba])
    if let == "c":
        c = pygame.image.load("imagenes/2C.png")
        screen.blit(c,[pos, aba])
    if let == "d":
        d = pygame.image.load("imagenes/2D.png")
        screen.blit(d,[pos, aba])
    if let == "e":
        e = pygame.image.load("imagenes/2E.png")
        screen.blit(e,[pos, aba])
    if let == "f":
        f = pygame.image.load("imagenes/2F.png")
        screen.blit(f,[pos, aba])
    if let == "g":
        g = pygame.image.load("imagenes/2G.png")
        screen.blit(g,[pos, aba])
    if let == "h":
        h = pygame.image.load("imagenes/2H.png")
        screen.blit(h,[pos, aba])
    if let == "i":
        i = pygame.image.load("imagenes/2I.png")
        screen.blit(i,[pos, aba])
    if let == "j":
        j = pygame.image.load("imagenes/2J.png")
        screen.blit(j,[pos, aba])
    if let == "k":
        k = pygame.image.load("imagenes/2K.png")
        screen.blit(k,[pos, aba])
    if let == "l":
        l = pygame.image.load("imagenes/2L.png")
        screen.blit(l,[pos, aba])
    if let == "m":
        m = pygame.image.load("imagenes/2M.png")
        screen.blit(m,[pos, aba])
    if let == "n":
        n = pygame.image.load("imagenes/2N.png")
        screen.blit(n,[pos, aba])
    if let == "ñ":
        ñ = pygame.image.load("imagenes/2Ñ.png")
        screen.blit(ñ,[pos, aba])
    if let == "o":
        o = pygame.image.load("imagenes/2O.png")
        screen.blit(o,[pos, aba])
    if let == "p":
        p = pygame.image.load("imagenes/2P.png")
        screen.blit(p,[pos, aba])
    if let == "q":
        q = pygame.image.load("imagenes/2Q.png")
        screen.blit(q,[pos, aba])
    if let == "r":
        r = pygame.image.load("imagenes/2R.png")
        screen.blit(r,[pos, aba])
    if let == "s":
        s = pygame.image.load("imagenes/2S.png")
        screen.blit(s,[pos, aba])
    if let == "t":
        t = pygame.image.load("imagenes/2T.png")
        screen.blit(t,[pos, aba])
    if let == "u":
        u = pygame.image.load("imagenes/2U.png")
        screen.blit(u,[pos, aba])
    if let == "v":
        v = pygame.image.load("imagenes/2V.png")
        screen.blit(v,[pos, aba])
    if let == "w":
        w = pygame.image.load("imagenes/2W.png")
        screen.blit(w,[pos, aba])
    if let == "x":
        x = pygame.image.load("imagenes/2X.png")
        screen.blit(x,[pos, aba])
    if let == "y":
        y = pygame.image.load("imagenes/2Y.png")
        screen.blit(y,[pos, aba])
    if let == "z":
        z = pygame.image.load("imagenes/2Z.png")
        screen.blit(z,[pos, aba])

def letraCasiChica(let, pos, aba, screen):
    if let == "a":
        a = pygame.image.load("imagenes/3A.png")
        a = pygame.transform.scale(a, [40, 40])
        screen.blit(a,[pos, aba])
    if let == "b":
        b = pygame.image.load("imagenes/3B.png")
        b = pygame.transform.scale(b, [40, 40])
        screen.blit(b,[pos, aba])
    if let == "c":
        c = pygame.image.load("imagenes/3C.png")
        c = pygame.transform.scale(c, [40, 40])
        screen.blit(c,[pos, aba])
    if let == "d":
        d = pygame.image.load("imagenes/3D.png")
        d = pygame.transform.scale(d, [40, 40])
        screen.blit(d,[pos, aba])
    if let == "e":
        e = pygame.image.load("imagenes/3E.png")
        e = pygame.transform.scale(e, [40, 40])
        screen.blit(e,[pos, aba])
    if let == "f":
        f = pygame.image.load("imagenes/3F.png")
        f = pygame.transform.scale(f, [40, 40])
        screen.blit(f,[pos, aba])
    if let == "g":
        g = pygame.image.load("imagenes/3G.png")
        g = pygame.transform.scale(g, [40, 40])
        screen.blit(g,[pos, aba])
    if let == "h":
        h = pygame.image.load("imagenes/3H.png")
        h = pygame.transform.scale(h, [40, 40])
        screen.blit(h,[pos, aba])
    if let == "i":
        i = pygame.image.load("imagenes/3I.png")
        i = pygame.transform.scale(i, [40, 40])
        screen.blit(i,[pos, aba])
    if let == "j":
        j = pygame.image.load("imagenes/3J.png")
        j = pygame.transform.scale(j, [40, 40])
        screen.blit(j,[pos, aba])
    if let == "k":
        k = pygame.image.load("imagenes/3K.png")
        k = pygame.transform.scale(k, [40, 40])
        screen.blit(k,[pos, aba])
    if let == "l":
        l = pygame.image.load("imagenes/3L.png")
        l = pygame.transform.scale(l, [40, 40])
        screen.blit(l,[pos, aba])
    if let == "m":
        m = pygame.image.load("imagenes/3M.png")
        m = pygame.transform.scale(m, [40, 40])
        screen.blit(m,[pos, aba])
    if let == "n":
        n = pygame.image.load("imagenes/3N.png")
        n = pygame.transform.scale(n, [40, 40])
        screen.blit(n,[pos, aba])
    if let == "ñ":
        ñ = pygame.image.load("imagenes/3Ñ.png")
        ñ = pygame.transform.scale(ñ, [40, 40])
        screen.blit(ñ,[pos, aba])
    if let == "o":
        o = pygame.image.load("imagenes/3O.png")
        o = pygame.transform.scale(o, [40, 40])
        screen.blit(o,[pos, aba])
    if let == "p":
        p = pygame.image.load("imagenes/3P.png")
        p = pygame.transform.scale(p, [40, 40])
        screen.blit(p,[pos, aba])
    if let == "q":
        q = pygame.image.load("imagenes/3Q.png")
        q = pygame.transform.scale(q, [40, 40])
        screen.blit(q,[pos, aba])
    if let == "r":
        r = pygame.image.load("imagenes/3R.png")
        r = pygame.transform.scale(r, [40, 40])
        screen.blit(r,[pos, aba])
    if let == "s":
        s = pygame.image.load("imagenes/3S.png")
        s = pygame.transform.scale(s, [40, 40])
        screen.blit(s,[pos, aba])
    if let == "t":
        t = pygame.image.load("imagenes/3T.png")
        t = pygame.transform.scale(t, [40, 40])
        screen.blit(t,[pos, aba])
    if let == "u":
        u = pygame.image.load("imagenes/3U.png")
        u = pygame.transform.scale(u, [40, 40])
        screen.blit(u,[pos, aba])
    if let == "v":
        v = pygame.image.load("imagenes/3V.png")
        v = pygame.transform.scale(v, [40, 40])
        screen.blit(v,[pos, aba])
    if let == "w":
        w = pygame.image.load("imagenes/3W.png")
        w = pygame.transform.scale(w, [40, 40])
        screen.blit(w,[pos, aba])
    if let == "x":
        x = pygame.image.load("imagenes/3X.png")
        x = pygame.transform.scale(x, [40, 40])
        screen.blit(x,[pos, aba])
    if let == "y":
        y = pygame.image.load("imagenes/3Y.png")
        y = pygame.transform.scale(y, [40, 40])
        screen.blit(y,[pos, aba])
    if let == "z":
        z = pygame.image.load("imagenes/3Z.png")
        z = pygame.transform.scale(z, [40, 40])
        screen.blit(z,[pos, aba])

def letraCasi(let, pos, aba, screen):
    if let == "a":
        a = pygame.image.load("imagenes/3A.png")
        screen.blit(a,[pos, aba])
    if let == "b":
        b = pygame.image.load("imagenes/3B.png")
        screen.blit(b,[pos, aba])
    if let == "c":
        c = pygame.image.load("imagenes/3C.png")
        screen.blit(c,[pos, aba])
    if let == "d":
        d = pygame.image.load("imagenes/3D.png")
        screen.blit(d,[pos, aba])
    if let == "e":
        e = pygame.image.load("imagenes/3E.png")
        screen.blit(e,[pos, aba])
    if let == "f":
        f = pygame.image.load("imagenes/3F.png")
        screen.blit(f,[pos, aba])
    if let == "g":
        g = pygame.image.load("imagenes/3G.png")
        screen.blit(g,[pos, aba])
    if let == "h":
        h = pygame.image.load("imagenes/3H.png")
        screen.blit(h,[pos, aba])
    if let == "i":
        i = pygame.image.load("imagenes/3I.png")
        screen.blit(i,[pos, aba])
    if let == "j":
        j = pygame.image.load("imagenes/3J.png")
        screen.blit(j,[pos, aba])
    if let == "k":
        k = pygame.image.load("imagenes/3K.png")
        screen.blit(k,[pos, aba])
    if let == "l":
        l = pygame.image.load("imagenes/3L.png")
        screen.blit(l,[pos, aba])
    if let == "m":
        m = pygame.image.load("imagenes/3M.png")
        screen.blit(m,[pos, aba])
    if let == "n":
        n = pygame.image.load("imagenes/3N.png")
        screen.blit(n,[pos, aba])
    if let == "ñ":
        ñ = pygame.image.load("imagenes/3Ñ.png")
        screen.blit(ñ,[pos, aba])
    if let == "o":
        o = pygame.image.load("imagenes/3O.png")
        screen.blit(o,[pos, aba])
    if let == "p":
        p = pygame.image.load("imagenes/3P.png")
        screen.blit(p,[pos, aba])
    if let == "q":
        q = pygame.image.load("imagenes/3Q.png")
        screen.blit(q,[pos, aba])
    if let == "r":
        r = pygame.image.load("imagenes/3R.png")
        screen.blit(r,[pos, aba])
    if let == "s":
        s = pygame.image.load("imagenes/3S.png")
        screen.blit(s,[pos, aba])
    if let == "t":
        t = pygame.image.load("imagenes/3T.png")
        screen.blit(t,[pos, aba])
    if let == "u":
        u = pygame.image.load("imagenes/3U.png")
        screen.blit(u,[pos, aba])
    if let == "v":
        v = pygame.image.load("imagenes/3V.png")
        screen.blit(v,[pos, aba])
    if let == "w":
        w = pygame.image.load("imagenes/3W.png")
        screen.blit(w,[pos, aba])
    if let == "x":
        x = pygame.image.load("imagenes/3X.png")
        screen.blit(x,[pos, aba])
    if let == "y":
        y = pygame.image.load("imagenes/3Y.png")
        screen.blit(y,[pos, aba])
    if let == "z":
        z = pygame.image.load("imagenes/3Z.png")
        screen.blit(z,[pos, aba])

def letraIncorrectaChica(let, pos, aba, screen):
    if let == "a":
        a = pygame.image.load("imagenes/4A.png")
        a = pygame.transform.scale(a, [40, 40])
        screen.blit(a,[pos, aba])
    if let == "b":
        b = pygame.image.load("imagenes/4B.png")
        b = pygame.transform.scale(b, [40, 40])
        screen.blit(b,[pos, aba])
    if let == "c":
        c = pygame.image.load("imagenes/4C.png")
        c = pygame.transform.scale(c, [40, 40])
        screen.blit(c,[pos, aba])
    if let == "d":
        d = pygame.image.load("imagenes/4D.png")
        d = pygame.transform.scale(d, [40, 40])
        screen.blit(d,[pos, aba])
    if let == "e":
        e = pygame.image.load("imagenes/4E.png")
        e = pygame.transform.scale(e, [40, 40])
        screen.blit(e,[pos, aba])
    if let == "f":
        f = pygame.image.load("imagenes/4F.png")
        f = pygame.transform.scale(f, [40, 40])
        screen.blit(f,[pos, aba])
    if let == "g":
        g = pygame.image.load("imagenes/4G.png")
        g = pygame.transform.scale(g, [40, 40])
        screen.blit(g,[pos, aba])
    if let == "h":
        h = pygame.image.load("imagenes/4H.png")
        h = pygame.transform.scale(h, [40, 40])
        screen.blit(h,[pos, aba])
    if let == "i":
        i = pygame.image.load("imagenes/4I.png")
        i = pygame.transform.scale(i, [40, 40])
        screen.blit(i,[pos, aba])
    if let == "j":
        j = pygame.image.load("imagenes/4J.png")
        j = pygame.transform.scale(j, [40, 40])
        screen.blit(j,[pos, aba])
    if let == "k":
        k = pygame.image.load("imagenes/4K.png")
        k = pygame.transform.scale(k, [40, 40])
        screen.blit(k,[pos, aba])
    if let == "l":
        l = pygame.image.load("imagenes/4L.png")
        l = pygame.transform.scale(l, [40, 40])
        screen.blit(l,[pos, aba])
    if let == "m":
        m = pygame.image.load("imagenes/4M.png")
        m = pygame.transform.scale(m, [40, 40])
        screen.blit(m,[pos, aba])
    if let == "n":
        n = pygame.image.load("imagenes/4N.png")
        n = pygame.transform.scale(n, [40, 40])
        screen.blit(n,[pos, aba])
    if let == "ñ":
        ñ = pygame.image.load("imagenes/4Ñ.png")
        ñ = pygame.transform.scale(ñ, [40, 40])
        screen.blit(ñ,[pos, aba])
    if let == "o":
        o = pygame.image.load("imagenes/4O.png")
        o = pygame.transform.scale(o, [40, 40])
        screen.blit(o,[pos, aba])
    if let == "p":
        p = pygame.image.load("imagenes/4P.png")
        p = pygame.transform.scale(p, [40, 40])
        screen.blit(p,[pos, aba])
    if let == "q":
        q = pygame.image.load("imagenes/4Q.png")
        q = pygame.transform.scale(q, [40, 40])
        screen.blit(q,[pos, aba])
    if let == "r":
        r = pygame.image.load("imagenes/4R.png")
        r = pygame.transform.scale(r, [40, 40])
        screen.blit(r,[pos, aba])
    if let == "s":
        s = pygame.image.load("imagenes/4S.png")
        s = pygame.transform.scale(s, [40, 40])
        screen.blit(s,[pos, aba])
    if let == "t":
        t = pygame.image.load("imagenes/4T.png")
        t = pygame.transform.scale(t, [40, 40])
        screen.blit(t,[pos, aba])
    if let == "u":
        u = pygame.image.load("imagenes/4U.png")
        u = pygame.transform.scale(u, [40, 40])
        screen.blit(u,[pos, aba])
    if let == "v":
        v = pygame.image.load("imagenes/4V.png")
        v = pygame.transform.scale(v, [40, 40])
        screen.blit(v,[pos, aba])
    if let == "w":
        w = pygame.image.load("imagenes/4W.png")
        w = pygame.transform.scale(w, [40, 40])
        screen.blit(w,[pos, aba])
    if let == "x":
        x = pygame.image.load("imagenes/4X.png")
        x = pygame.transform.scale(x, [40, 40])
        screen.blit(x,[pos, aba])
    if let == "y":
        y = pygame.image.load("imagenes/4Y.png")
        y = pygame.transform.scale(y, [40, 40])
        screen.blit(y,[pos, aba])
    if let == "z":
        z = pygame.image.load("imagenes/4Z.png")
        z = pygame.transform.scale(z, [40, 40])
        screen.blit(z,[pos, aba])

def letraIncorrecta(let, pos, aba, screen):
    if let == "a":
        a = pygame.image.load("imagenes/4A.png")
        screen.blit(a,[pos, aba])
    if let == "b":
        b = pygame.image.load("imagenes/4B.png")
        screen.blit(b,[pos, aba])
    if let == "c":
        c = pygame.image.load("imagenes/4C.png")
        screen.blit(c,[pos, aba])
    if let == "d":
        d = pygame.image.load("imagenes/4D.png")
        screen.blit(d,[pos, aba])
    if let == "e":
        e = pygame.image.load("imagenes/4E.png")
        screen.blit(e,[pos, aba])
    if let == "f":
        f = pygame.image.load("imagenes/4F.png")
        screen.blit(f,[pos, aba])
    if let == "g":
        g = pygame.image.load("imagenes/4G.png")
        screen.blit(g,[pos, aba])
    if let == "h":
        h = pygame.image.load("imagenes/4H.png")
        screen.blit(h,[pos, aba])
    if let == "i":
        i = pygame.image.load("imagenes/4I.png")
        screen.blit(i,[pos, aba])
    if let == "j":
        j = pygame.image.load("imagenes/4J.png")
        screen.blit(j,[pos, aba])
    if let == "k":
        k = pygame.image.load("imagenes/4K.png")
        screen.blit(k,[pos, aba])
    if let == "l":
        l = pygame.image.load("imagenes/4L.png")
        screen.blit(l,[pos, aba])
    if let == "m":
        m = pygame.image.load("imagenes/4M.png")
        screen.blit(m,[pos, aba])
    if let == "n":
        n = pygame.image.load("imagenes/4N.png")
        screen.blit(n,[pos, aba])
    if let == "ñ":
        ñ = pygame.image.load("imagenes/4Ñ.png")
        screen.blit(ñ,[pos, aba])
    if let == "o":
        o = pygame.image.load("imagenes/4O.png")
        screen.blit(o,[pos, aba])
    if let == "p":
        p = pygame.image.load("imagenes/4P.png")
        screen.blit(p,[pos, aba])
    if let == "q":
        q = pygame.image.load("imagenes/4Q.png")
        screen.blit(q,[pos, aba])
    if let == "r":
        r = pygame.image.load("imagenes/4R.png")
        screen.blit(r,[pos, aba])
    if let == "s":
        s = pygame.image.load("imagenes/4S.png")
        screen.blit(s,[pos, aba])
    if let == "t":
        t = pygame.image.load("imagenes/4T.png")
        screen.blit(t,[pos, aba])
    if let == "u":
        u = pygame.image.load("imagenes/4U.png")
        screen.blit(u,[pos, aba])
    if let == "v":
        v = pygame.image.load("imagenes/4V.png")
        screen.blit(v,[pos, aba])
    if let == "w":
        w = pygame.image.load("imagenes/4W.png")
        screen.blit(w,[pos, aba])
    if let == "x":
        x = pygame.image.load("imagenes/4X.png")
        screen.blit(x,[pos, aba])
    if let == "y":
        y = pygame.image.load("imagenes/4Y.png")
        screen.blit(y,[pos, aba])
    if let == "z":
        z = pygame.image.load("imagenes/4Z.png")
        screen.blit(z,[pos, aba])
