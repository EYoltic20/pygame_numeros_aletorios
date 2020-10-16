import sys
import pygame
import os
import random
import time
def Instrucciones():
    blak=(0,0,0)
    screen2=pygame.display.set_mode((800,600))
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_ESCAPE):
                    screen2=pygame.display.set_mode((800,600))
                    running=False
        text1=CreatingText('Baloo Bhai',50,"Instrucciones: ",False,(255,255,255))
        text2=CreatingText('Comic Sans MS',50,"Sumar dos numeros aleatorios",False,(0,0,255))
        text3=CreatingText('Comic Sans MS',50,"Facil: numeros aleatorios de 0-100",False,(0,255,0))
        text4=CreatingText('Comic Sans MS',50,"Medio: numeros aleatorios de 0-500",False,(255,0,0))
        text5=CreatingText('Comic Sans MS',50,"Loco: numeros aleatorios de 0-1000",False,(163, 73, 164))
        screen2.fill(blak)
        screen2.blit(text1.textsurface,(150,100))
        screen2.blit(text2.textsurface,(150,200))
        screen2.blit(text3.textsurface,(150,300))
        screen2.blit(text4.textsurface,(150,400))
        screen2.blit(text5.textsurface,(150,500))
        pygame.display.update()
def preguntar():
    unido=''
    teclado=[]
    size=(800,600)
    screend=pygame.display.set_mode(size)
    while True:
        for event in pygame.event.get():
            if(event.type==pygame.KEYDOWN):
                if(event.unicode=='1'or event.unicode=='2'or event.unicode=='3'or event.unicode=='4'or event.unicode=='5'or event.unicode=='6' or event.unicode=='7'or event.unicode=='9'or event.unicode=='8' or event.unicode=='0'):
                    teclado.append(event.unicode)
                    unido=''.join(teclado)
                elif(event.unicode=='\r'):
                    return unido
                    break
        screend.fill((0,0,0))
        entry=pygame.draw.rect(screend,(44, 255, 252),(250,400,250,50))
        te=CreatingText('Comic Sans MS',60,'Cuantas sumas haras?',True,(163, 73, 164))
        texto=CreatingText('Comic Sans MS',50,str(unido),True,(0,0,0))
        screend.blit(texto.textsurface,(250,400))
        screend.blit(te.textsurface,(100,100))
        pygame.display.update()

def nivel_dificil():
    l=preguntar()
    k=int(l)
    tp=''
    size=(800,600)
    screen3=pygame.display.set_mode(size)
    n=(0,0,0)
    verde=(0,0,255)
    score=0
    Vidas=3
    numer1=random.randrange(1000)
    number2=random.randrange(1000)
    runnig=True
    tecleado=[]
    d=0
    h=0
    #Contar tiempo
    #Hacer el entry
    #Validar,sumar score y restar vidas
    while runnig:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif(event.type==pygame.KEYDOWN):
                if(event.unicode=='1'or event.unicode=='2'or event.unicode=='3'or event.unicode=='4'or event.unicode=='5'or event.unicode=='6' or event.unicode=='7'or event.unicode=='9'or event.unicode=='8' or event.unicode=='0'):
                    tecleado.append(event.unicode)
                    tp=''.join(tecleado)
                elif(event.unicode=='\r'):
                    k-=1
                    suma=numer1+number2
                    if(str(suma)==tp):
                        score+=1
                        tecleado=[]
                        tp=''
                        numer1=random.randrange(1000)
                        number2=random.randrange(1000)
                    else:
                        tecleado=[]
                        tp=''
                        Vidas-=1
                        numer1=random.randrange(1000)
                        number2=random.randrange(1000)
        if(k==0):
            Nueva_pestana("Juego concluido Score: {} Vidas: {} ".format(score,Vidas),(800,600))
            runnig=False
        elif(Vidas==0):
            Nueva_pestana('Uy creo que se te acabaron las vidas, tu puntacion fue de {} '.format(score),(1200,600))
            runnig=False
        numero1=CreatingText('Comic Sans MS',50,'{}'.format(str(numer1)),True,verde)
        numero2=CreatingText('Comic Sans MS',50,'{}'.format(str(number2)),True,verde)
        texto=CreatingText('Comic Sans MS',50,'Score: {}'.format(str(score)),True,verde)
        vidas=CreatingText('Comic Sans MS',50,'Vidas: {} '.format(str(Vidas)),True,verde)
        texto_delo_tecleado=CreatingText('Comic Sans MS',50,tp,True,verde)
        screen3.fill((0,0,0))
        screen3.blit(texto.textsurface,(0,0))
        screen3.blit(vidas.textsurface,(600,0))
        screen3.blit(numero1.textsurface,(300,300))
        screen3.blit(numero2.textsurface,(400,300))
        entry=pygame.draw.rect(screen3,(44, 255, 252),(250,400,250,50))
        screen3.blit(texto_delo_tecleado.textsurface,(250,400))
        pygame.display.update()

def nivel_medio():
    l=preguntar()
    k=int(l)
    tp=''
    size=(800,600)
    screen3=pygame.display.set_mode(size)
    n=(0,0,0)
    verde=(0,0,255)
    score=0
    Vidas=3
    numer1=random.randrange(200)
    number2=random.randrange(200)
    runnig=True
    tecleado=[]
    d=0
    h=0
    #Contar tiempo
    #Hacer el entry
    #Validar,sumar score y restar vidas
    while runnig:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif(event.type==pygame.KEYDOWN):
                if(event.unicode=='1'or event.unicode=='2'or event.unicode=='3'or event.unicode=='4'or event.unicode=='5'or event.unicode=='6' or event.unicode=='7'or event.unicode=='9'or event.unicode=='8' or event.unicode=='0'):
                    tecleado.append(event.unicode)
                    tp=''.join(tecleado)
                elif(event.unicode=='\r'):
                    k-=1
                    suma=numer1+number2
                    if(str(suma)==tp):
                        score+=1
                        tecleado=[]
                        tp=''
                        numer1=random.randrange(200)
                        number2=random.randrange(200)
                    else:
                        tecleado=[]
                        tp=''
                        Vidas-=1
                        numer1=random.randrange(100)
                        number2=random.randrange(100)
        if(k==0):
            Nueva_pestana("Juego concluido Score: {} Vidas: {} ".format(score,Vidas),(800,600))
            runnig=False
        elif(Vidas==0):
            Nueva_pestana('Uy creo que se te acabaron las vidas, tu puntacion fue de {} '.format(score),(1200,600))
            runnig=False
        numero1=CreatingText('Comic Sans MS',50,'{}'.format(str(numer1)),True,verde)
        numero2=CreatingText('Comic Sans MS',50,'{}'.format(str(number2)),True,verde)
        texto=CreatingText('Comic Sans MS',50,'Score: {}'.format(str(score)),True,verde)
        vidas=CreatingText('Comic Sans MS',50,'Vidas: {} '.format(str(Vidas)),True,verde)
        texto_delo_tecleado=CreatingText('Comic Sans MS',50,tp,True,verde)
        screen3.fill(n)
        screen3.blit(texto.textsurface,(0,0))
        screen3.blit(vidas.textsurface,(600,0))
        screen3.blit(numero1.textsurface,(300,300))
        screen3.blit(numero2.textsurface,(400,300))
        entry=pygame.draw.rect(screen3,(44, 255, 252),(250,400,250,50))
        screen3.blit(texto_delo_tecleado.textsurface,(250,400))
        pygame.display.update()

def Nivel_Facil():
    l=preguntar()
    k=int(l)
    tp=''
    size=(800,600)
    screen3=pygame.display.set_mode(size)
    n=(0,0,0)
    verde=(0,0,255)
    score=0
    Vidas=3
    numer1=random.randrange(100)
    number2=random.randrange(100)
    runnig=True
    tecleado=[]
    d=0
    h=0
    #Contar tiempo
    #Hacer el entry
    #Validar,sumar score y restar vidas
    while runnig:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif(event.type==pygame.KEYDOWN):
                if(event.unicode=='1'or event.unicode=='2'or event.unicode=='3'or event.unicode=='4'or event.unicode=='5'or event.unicode=='6' or event.unicode=='7'or event.unicode=='9'or event.unicode=='8' or event.unicode=='0'):
                    tecleado.append(event.unicode)
                    tp=''.join(tecleado)
                elif(event.unicode=='\r'):
                    k-=1
                    suma=numer1+number2
                    if(str(suma)==tp):
                        score+=1
                        tecleado=[]
                        tp=''
                        numer1=random.randrange(100)
                        number2=random.randrange(100)
                    else:
                        tecleado=[]
                        tp=''
                        Vidas-=1
                        numer1=random.randrange(100)
                        number2=random.randrange(100)
        if(k==0):
            Nueva_pestana("Juego concluido Score: {} Vidas: {} ".format(score,Vidas),(800,600))
            runnig=False
        elif(Vidas==0):
            Nueva_pestana('Uy creo que se te acabaron las vidas, tu puntacion fue de {} '.format(score),(1200,600))
            runnig=False
        numero1=CreatingText('Comic Sans MS',50,'{}'.format(str(numer1)),True,verde)
        numero2=CreatingText('Comic Sans MS',50,'{}'.format(str(number2)),True,verde)
        texto=CreatingText('Comic Sans MS',50,'Score: {}'.format(str(score)),True,verde)
        vidas=CreatingText('Comic Sans MS',50,'Vidas: {} '.format(str(Vidas)),True,verde)
        texto_delo_tecleado=CreatingText('Comic Sans MS',50,tp,True,verde)
        screen3.fill(n)
        screen3.blit(texto.textsurface,(0,0))
        screen3.blit(vidas.textsurface,(600,0))
        screen3.blit(numero1.textsurface,(300,300))
        screen3.blit(numero2.textsurface,(400,300))
        entry=pygame.draw.rect(screen3,(44, 255, 252),(250,400,250,50))
        screen3.blit(texto_delo_tecleado.textsurface,(250,400))
        pygame.display.update()

def Dificultadad(screen):
    butonFacil=pygame.draw.rect(screen,(255,0,0),(270,100,250,50))
    butonIntermedio=pygame.draw.rect(screen,(0,255,0),(270,200,250,50))
    butonDificil=pygame.draw.rect(screen,(0,0,255),(270,300,250,50))
    """mx,my
    mx1,my2
    mx2,my2"""
    texto=CreatingText('Comic Sans MS',50,'Facil',True,(255,255,255))
    texto2=CreatingText('Comic Sans MS',50,'Normal',True,(255,255,255))
    texto3=CreatingText('Comic Sans MS',50,'Loco',True,(255,255,255))
    screen.blit(texto.textsurface,(350,100))
    screen.blit(texto2.textsurface,(350,200))
    screen.blit(texto3.textsurface,(350,300))

class CreatingText:
    def __init__(self,font,sizet,text,tf,color):
        self.myfont=pygame.font.SysFont(font,sizet)
        self.textsurface=self.myfont.render(text,tf,color)


def Nueva_pestana(Texto,size):
    blak=( 0, 0, 0)
    screen2=pygame.display.set_mode(size)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_ESCAPE):
                    screen2=pygame.display.set_mode((800,600))
                    running=False
        text=CreatingText('Comic Sans MS',50,Texto,False,(44, 255, 252))
        screen2.fill(blak)
        screen2.blit(text.textsurface,(100,300))
        pygame.display.update()

class Button:
    def __init__(self,image,position):
        self.image=image
        self.rect=image.get_rect(topleft=position)
    def on_click(self,event):
        d=open('Instruccions.txt','r')
        k=d.read()
        if(event.type==pygame.MOUSEBUTTONDOWN):
            if(event.button==1):
                if(self.rect.collidepoint(event.pos)):
                    Instrucciones()
def main():
    d=0
    pygame.init()
    h=1
    pygame.font.init()
    size=(800,600)
    screen=pygame.display.set_mode(size)
    black=( 0, 0, 0)
    white=( 255, 255, 255)
    green=( 0, 255, 0)
    red=( 255, 0, 0)
    blue=( 0, 0, 255)
    image0=pygame.image.load('signo2.png')
    image0=pygame.transform.scale(image0,(25,25))
    lx=25
    ly=25
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if(event.type==pygame.KEYDOWN):
                    if(event.unicode=='1'):
                        Nivel_Facil()
                    elif(event.unicode=='2'):
                        nivel_medio()
                    elif(event.unicode=='3'):
                        nivel_dificil()
        if(h>0 and h!=101):
            d=0
            h+=10
            print(h)
        elif(h==101):
            d=10
            h=1
        screen.fill(black)
        button=Button(image0,(lx,ly))# creamos un objeto button
        button.on_click(event)# llamamos a la funcion on_click
        screen.blit(button.image,button.rect)# lo proyectamos en la pantalla
        t1=CreatingText('Comic Sans MS',30+d,'facil tecle 1',True,(255,0,0))
        t2=CreatingText('Comic Sans MS',30+d,'Normal  tecle 2',True,(0,255,0))
        t3=CreatingText('Comic Sans MS',30+d,'Loco tecle 3',True,(0,0,255))
        #Dificultad
        Dificultadad(screen)
        #sumando score
        screen.blit(t1.textsurface,(200,500))
        screen.blit(t2.textsurface,(400,500))
        screen.blit(t3.textsurface,(600,500))
        pygame.display.update()

if __name__ == '__main__':
    main()
