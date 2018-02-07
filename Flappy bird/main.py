import pygame
import random
import time

pygame.init()
pygame.font.init()
# 23 24   52 623
dw=400
dh=600
flag=0
xe=0
score =0
highscore=0
ye=0
display=pygame.display.set_mode((dw,dh))
thistime=-1
color={'white':(255,255,255),'black':(0,0,0),'yellow':(255,255,0),'cyan':(0,255,255),'red':(125,0,0),'green':(0,125,0),'darkgreen':(0,255,0),'darkred':(255,0,0)}

pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()

bgimg=pygame.image.load('bg.png')
img=pygame.image.load('bird.png')
eimg=pygame.image.load('enemy.png')

def enemycome():
    global thistime
    xe=405
    ye=random.randrange(-610,-210)

    return [xe,ye]

def message_display(text):
    texta =  pygame.font.Font('freesansbold.ttf',50)
    surf,rect = text_objects(text,texta)
    rect.center=((dw/2),(dh/2))
    display.blit(surf,rect)
    pygame.display.update()
    time.sleep(3)
    gameloop()        

def text_objects(text, font):
    textSurface = font.render(text, True, color['black'])
    return textSurface, textSurface.get_rect()

def diedfunc():
    global highscore
    global score
    if(score>highscore):
        file=open("DO-NOT-EDIT.txt",'w')
        file.write(str(score))
        file.close()
    message_display("DIED")
    

def imgfunc(x,y):
    display.blit(img,(x,y))

def enemyfunc(x,y):
    display.blit(eimg,(x,y))

def crash(x,y,x1,y1,y2):
    if((x+23+18)>x1 and (x+18<=x1+52) and ((y+10<=y1+623) or ((y+24+10)>=y2))):
        return True
    return False

def score_display(text):
    texta =  pygame.font.Font('freesansbold.ttf',20)
    surf,rect = text_objects(text,texta)
    rect.center=(70,20)
    display.blit(surf,rect)
    pygame.display.update()

def hscore_display(text):
    texta =  pygame.font.Font('freesansbold.ttf',20)
    surf,rect = text_objects(text,texta)
    rect.center=(70,50)
    display.blit(surf,rect)
    pygame.display.update()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(display, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(display, ic,(x,y,w,h))
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    display.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.fill(color['yellow'])
        texta = pygame.font.SysFont("comicsansms",50)
        surf,rect = text_objects("FLAPPY",texta)
        rect.center = ((dw/2),100)
        display.blit(surf,rect)
        surf,rect = text_objects("BIRD",texta)
        rect.center = ((dw/2),200)
        display.blit(surf,rect)
        surf,rect = text_objects("CLONE",texta)
        rect.center = ((dw/2),300)
        display.blit(surf,rect)

        button("PLAY",50,450,100,50,color['green'],color['darkgreen'],gameloop)
        button("QUIT",250,450,100,50,color['red'],color['darkred'],pygame.quit)

        pygame.display.update()
        clock.tick(15)

def jump(x,y):
    global thistime
    global flag
    global xe
    global ye
    global score
    y1=8
    y2=6
    y3=4
    arr=[[0,0],[2,y1],[2,y1],[2,y1],[2,y1],[2,y1],[2,y1],[2,y1],[2,y1],[2,y1],[3,y2],[3,y2],[3,y2],[3,y3],[3,y3],[3,y3],[3,y3],[3,y3],[3,2],[3,2],[3,2],[3,2],[3,2],[3,1],[3,1],[3,1],[3,1],[3,1],[3,0],[3,0],[3,0],[3,0],[3,-2],[3,-2],[3,-2],[3,-2],[3,-2],[3,-2],[3,-2],[3,-2],[3,-2],[3,-5],[3,-5],[3,-5],[3,-5],[3,-5],[3,-5],[3,-5],[3,-5],[3,-5],[3,-5],[3,-5],[3,-5],[3,-5],[3,-5]]
    for i in arr:
        thistime+=1
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                y=jump(x,y)
                return y
        if flag==0:
            xyz=enemycome()
            thistime+=1
            xe=xyz[0]
            ye=xyz[1]
            flag=1
        if xe<-50:
            flag=0
        y-=i[1]
        if xe ==90:
            score+=1
        if flag==-1:
            if thistime>=100:
                flag=0
        #display.fill(color['cyan'])
        
        display.blit(bgimg,(0,0))
        score_display("Score: "+str(score))
        hscore_display("High Score: "+str(highscore))
        if flag==1:
            xe-=5
            enemyfunc(xe,ye)
            enemyfunc(xe,ye+800)
        if xe<-50:
            flag=0
            enemyfunc(xe,ye)
            enemyfunc(xe,ye+800)
        imgfunc(x,y)
        if crash(x,y,xe,ye,ye+800):
            diedfunc()
        pygame.display.update()
        clock.tick(60)
    return y
def gameloop():
    global thistime
    global xe
    global ye
    died=False
    y=dh*0.5
    x=dw*0.3
    global flag
    he=200
    we=50
    global highscore
    file=open("DO-NOT-EDIT.txt",'r')
    string=file.read()
    file.close()
    highscore=int(string)
    flag=-1
    timea=0
    xe=dw-100
    ye=0
    thistime=0
    global score
    score=0
    change=2
    while not died:
        thistime+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamedied = True
                break
            if event.type == pygame.KEYDOWN:
                y=jump(x,y)
                change=10
        if (y>(dh-15)):
            diedfunc()
        y+=change
        if flag==-1:
            if thistime>=100:
                flag=0
        if flag==0:
            xyz=enemycome()
            thistime+=1
            xe=xyz[0]
            ye=xyz[1]
            flag=1
        if xe<-50:
            flag=0
            enemyfunc(xe,ye+800)
            enemyfunc(xe,ye)
        if x>dw:
            x=0
        if xe ==90:
            score+=1
        #display.fill(color['cyan'])
        display.blit(bgimg,(0,0))
        score_display("Score: "+str(score))
        hscore_display("High Score: "+str(highscore))
        imgfunc(x,y)
        if flag==1:
            xe-=5
            enemyfunc(xe,ye)
            enemyfunc(xe,ye+800)
        if crash(x,y,xe,ye,ye+800):
            diedfunc()
        pygame.display.update()
        clock.tick(60)
game_intro()
gameloop()
pygame.quit()
quit()
