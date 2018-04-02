import pygame
import time
import random

pygame.init()

dw=800
dh=600
displayScreen = pygame.display.set_mode((dw,dh))#sets width and height

color={'red':(200,0,0),'white':(255,255,255),'black':(0,0,0),'seacolor':(0,125,125),'cyan':(0,255,255),'green':(0,200,0),'darkgreen':(0,255,0),'darkred':(255,0,0)}

pygame.display.set_caption('Save the Fish')#sets title

clock = pygame.time.Clock()

playerImg=pygame.image.load('fish.png')
villainImg=pygame.image.load('shark.png')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(displayScreen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(displayScreen, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    displayScreen.blit(textSurf, textRect)

def fishfunc(x,y):
    displayScreen.blit(playerImg,(x,y))#position playerImg on screen

def villainfunc(xa,ya):
    displayScreen.blit(villainImg,(xa,ya))#position villainImg on screen

def message_display(text):
    texta =  pygame.font.Font('freesansbold.ttf',50)
    surf,rect = text_objects(text,texta)
    rect.center=((dw/2),(dh/2))
    displayScreen.blit(surf,rect)
    pygame.display.update()
    time.sleep(3)
    gameloop()

def score_display(text):
    texta =  pygame.font.Font('freesansbold.ttf',20)
    surf,rect = text_objects(text,texta)
    rect.center=(70,20)
    displayScreen.blit(surf,rect)
    pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, color['black'])
    return textSurface, textSurface.get_rect()

def diedfunc():
    message_display("You couldn't save the fish")

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        displayScreen.fill(color['cyan'])
        texta = pygame.font.SysFont("comicsansms",100)
        surf,rect = text_objects("SAVE THE FISH",texta)
        rect.center = ((dw/2),(dh/2))
        displayScreen.blit(surf,rect)

        button("PLAY",150,450,100,50,color['green'],color['darkgreen'],gameloop)
        button("QUIT",550,450,100,50,color['red'],color['darkred'],pygame.quit)

        pygame.display.update()
        clock.tick(15)

def gameloop():
    gamedied = False #False means game is not going to exit

    x=dw*0.45
    y=dh*0.8
    ya =0
    num=140
    xa=0
    changex=0
    timea=-1
    while not gamedied:
        timea+=1
        #print(timea)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamedied = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    changex=-5
                elif event.key == pygame.K_RIGHT:
                    changex=5
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        changex = 0
        x+=changex
        displayScreen.fill(color['seacolor'])
        fishfunc(x,y)
        if timea%num==0:
            ya=0
            xa=random.randrange(0,dw)
            #xa=300
            villainfunc(xa,0)
        else:
            ya=ya+(timea/200)+5
            num=140-((int)((timea/200))*5)
            #print('num is' +str(num))
            villainfunc(xa,ya)
        if x>dw-25:
            x=0-25
        if x<0-25:
            x=dw-50
        if (ya+70)>=y and (xa+50)>=x and (ya)<=(y+25) and xa<=(x+25):
            diedfunc()
        score_display("Score: "+str(timea))
        pygame.display.update()
        clock.tick(60)#fps

game_intro()
gameloop()
pygame.quit()
quit()
