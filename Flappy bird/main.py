import pygame
import random
import time

pygame.init()
# 23 24   52 623
dw=400
dh=600
flag=0
xe=0
score =0
ye=0
display=pygame.display.set_mode((dw,dh))
thistime=-1
color={'white':(255,255,255),'black':(0,0,0),'cyan':(0,125,0)}

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
            print("NOW")
            died=True
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
        imgfunc(x,y)
        if flag==1:
            xe-=5
            enemyfunc(xe,ye)
            enemyfunc(xe,ye+800)
        if crash(x,y,xe,ye,ye+800):
            diedfunc()
        pygame.display.update()
        clock.tick(60)
gameloop()
pygame.quit()
quit()
