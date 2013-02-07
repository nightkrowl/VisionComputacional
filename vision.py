#!/usr/bin/env python

import pygame  # interfaz
from pygame.locals import *  # para funcion de botones y raton
from pygame import * 
from PIL import Image # Para cargar imagen
import numpy as ny  #Libreria para arreglos
import sys    # 	

umbraln = 122 # Umbral para color negro en funcion umbral
umbralb = 130 # Umbral para color blanco en funcion umbral

image = str(raw_input('Dame el nombre de la imagen con extencion: ')) # Pedimos imagen

img = Image.open(image) # Abrimos imagen con PIL
width, height = img.size    #Obtencion de medidas de la imagen


def window():
    screen = pygame.display.set_mode((width + 100, height)) # cargar ventana con medidas
    pygame.display.set_caption("window vision") # Mostrar ventana
    background = pygame.image.load(image) # carga de imagen
    #button = pygame.Surface((100, 25))
    screen.blit(background, (100,0)) #posicion de imagen en la ventana
    pygame.display.flip()   #Refrescar pantalla

    bgris = pygame.image.load("gris.png") #boton
    screen.blit(bgris, (0,30)) # Posicion del boton

    bumbral = pygame.image.load("umbral.png") #boton
    screen.blit(bumbral, (0,60)) # Posicion del boton

    bfiltro = pygame.image.load("filtro.png")
    screen.blit(bfiltro, (0,90))

    breset = pygame.image.load("reset.png")
    screen.blit(breset, (0,120))
    pygame.display.flip() # Refrescar pantalla
    
    
    while True:  #ciclo para cerrar ventana
        for event in pygame.event.get(): # Para eventos en de pygame
            if event.type == QUIT: #Cerrar ventana
                sys.exit(0)
	    """
	    if event.type == pygame.MOUSEBUTTONDOWN: #evento click
		mouse_x, mouse_y  = pygame.mouse.get_pos() #coordenadas del mouse
		if 0 < mouse_x < 100 and 0 < mouse_y < 30: #coordenadas de boton 
		    escalagrises(img) # Funcion 
		    background = pygame.image.load("greyim.png") # carga de imagen
	 	    screen.blit(background, (100,0)) #posicion de ventana en pantalla
	   	    pygame.display.flip() # se muestran cambios
		if 0 < mouse_x < 100 and 30 < mouse_y < 60:
		    umbrales(img)
		    background = pygame.image.load("umb.png") # carga de imagen
	 	    screen.blit(background, (100,0)) #posicion de ventana en pantalla
	   	    pygame.display.flip() # se muestran cambios 
		if 0 < mouse_x < 100 and 60 < mouse_y < 90:
		    filtro()
		    background = pygame.image.load("imfil.png") # carga de imagen
	 	    screen.blit(background, (100,0)) #posicion de ventana en pantalla
	   	    pygame.display.flip() # se muestran cambios
		if 0 < mouse_x < 100 and 90 < mouse_y < 120:
  		    background = pygame.image.load(image) # carga de imagen
		    screen.blit(background, (0,0))
    		    pygame.display.flip() # se muestran cambios	
	    """
	    if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
		    escalagrises()
		    background = pygame.image.load("grayim.png") # carga de imagen
	 	    screen.blit(background, (100,0)) #posicion de imagen en ventana
		    pygame.display.flip()
	    if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
		    umbrales()
		    background = pygame.image.load("umb.png") # carga de imagen
	 	    screen.blit(background, (100,0)) #posicion de imagen en ventana
		    pygame.display.flip()
	    if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_UP:
		    filtro()
		    background = pygame.image.load("imfil.png") # carga de imagen
	 	    screen.blit(background, (100,0)) #posicion de imagen en ventana
		    pygame.display.flip()

    return 0

def escalagrises(): # Funcion para hacer a escala de grises
    img = Image.open(image) # Abrimos imagen con PIL
    pixel = img.load()  #Carga de matriz de pixeles
    width, height = img.size    #Obtencion de medidas de la imagen

    for i in range(width):  #Contar pixeles a lo ancho
        for j in range(height):  # Contar pixeles a lo largo
            (r, g, b) = pixel[i,j]
            gs = int((r + g + b) / 3)
            pixel [i, j] = (gs, gs, gs)
    return img.save("grayim.png")
        
def umbrales():  # Funcion para los umbrales
    img = Image.open(image) # Abrimos imagen con PIL
    pixel = img.load()  #Carga de matriz de pixeles
    width, height = img.size    #Obtencion de medidas de la imagen

    for i in range(width):
        for j in range(height):
	    (r, g, b) = pixel[i,j]
            prom = int((r + g + b) / 3)
            if prom < umbraln:
	        pixel[i,j] = (0, 0, 0)
	    elif prom > umbralb:
	        pixel[i,j] = (255, 255, 255)
            else:   
                pixel[i,j] = (prom, prom, prom)  
    return img.save("umb.png")	       

def filtro():  # Funcion Filtro
    img = Image.open(image) # Abrimos imagen con PIL
    pixel = img.load()  #Carga de matriz de pixeles
    width, height = img.size    #Obtencion de medidas de la imagen

    for i in range(width):
        for j in range(height):
	    img_filtro = []
            img_filtro.append(list(pixel[i, j]))
            
            if i > 0:
                img_filtro.append(list(pixel[i-1, j]))
            if j > 0:
                img_filtro.append(list(pixel[i, j-1]))
            if i < width-1:
                img_filtro.append(list(pixel[i+1, j]))
            if j < height-1:
                img_filtro.append(list(pixel[i, j+1]))
            
            filtro = [sum(a) for a in zip(*img_filtro)]
            pixel[i,j] = filtro[0]/3, filtro[1]/3, filtro[2]/3
    return img.save("imfil.png")

"""
def convolucion(f, h):
    F = (x, y)
    h = ny.array ([0, 0.2, 0],[0.2, 0.2, 0.2],[0, 0.2, 0])
	for x in xrange(width):
	    for y in xrange(height):
		suma = 0.0
	    for i in xrange (k1):
		for j in xrange(k2):
		try:
		    suma += f(x + i, y + j) * h(i, j)
		except:
		    pass
	    F(x, y) = int(from(suma))
	return F
"""   
      
def main():
    pygame.init()
    window()
    escalagrises()
    umbrales()
    filtro()
    #convolucion()
main()
