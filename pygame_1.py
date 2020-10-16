import pygame
import sys
import os
pygame.init()
size=(800,600)
screen=pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        print(event)#conocer el tipode evento
        if event.type == pygame.QUIT:# Esta funcion nos dice que si el evento que pasa es de salir se sale
            sys.exit()
