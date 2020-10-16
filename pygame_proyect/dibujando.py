import pygame
import sys
pygame.init()
black=( 0, 0, 0)
white=( 255, 255, 255)
green=( 0, 255, 0)
red=( 255, 0, 0)
blue=( 0, 0, 255)
size=(800,600)
screen=pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    screen.fill(black)
    pygame.draw.line(screen,green,[0,100],[200,100],20)#x,y,tamano
    pygame.draw.rect(screen,blue,(100,100,80,80))#los primeros dos valores son donde comienza , El tercero es el ancho y el 4 la altura
    pygame.draw.circle(screen,red,(20,20),200)#su centro y el tamano de su radio
    pygame.display.flip()
