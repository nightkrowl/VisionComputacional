#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys, pygame
from pygame.locals import *
 
WIDTH = 340
HEIGHT = 500
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # cargar ventana con medidas
    pygame.display.set_caption("Ventana") # Mostrar ventana

    fondo = pygame.image.load('fondo.png').convert() # carga de imagen
    screen.blit(fondo, (0,0)) #posiciones en ventana
    pygame.display.flip() # se muestran cambios

    while True:  #ciclo para cerrar ventana
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
