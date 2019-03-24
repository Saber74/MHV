from pygame import *
mixer.init()
mixer.music.load("Elevator Music - So Chill.mp3")
bedroomPic=image.load("bedroom.jpg")
font.init()
arial = font.SysFont('Arial',100)
WIDTH, HEIGHT = 1400, 900
size=(WIDTH, HEIGHT)
screen = display.set_mode(size)
running = True
def plant():
    waterRect=Rect(1100,350,250,100)
    talkRect=Rect(1100,350,250,100)
    while True:
        for evt in event.get():
            if evt.type == QUIT:
                running = False
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        display.update()
    quit()
def bedroom():
    wakeupRect=Rect(300,600,700,100)
    plantRect=Rect(1100,200,250,100)
    gotobathRect=Rect(1100,350,250,100)
    step1=False
    while True:
        for evt in event.get():
            if evt.type == QUIT:
                running = False
        if step1==False:
            wakeupText= arial.render(str("Wake up"), True, (0, 0, 0))
            draw.rect(screen,(100,100,100),wakeupRect)
            screen.blit(wakeupText, (510, 585))
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        if wakeupRect.collidepoint(mx,my) and step1==False:
            draw.rect(screen,(0,200,250),wakeupRect)
            screen.blit(wakeupText, (510, 585))
        if wakeupRect.collidepoint(mx,my) and mb[0]:
            screen.blit(bedroomPic,(0,0))
            step1=True
        if step1==True:
            draw.rect(screen,(100,100,100),plantRect)
            draw.rect(screen,(100,100,100),gotobathRect)
            if plantRect.collidepoint(mx,my) and mb[0]:
                plant()
            # elif gotobathRect.collidepoint(mx,my) and mb[0]:
            #     break
        display.update()
    quit()
while running:
    screen.fill((200,200,200))
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    bedroom()

    display.update()
quit()
        
       
        
  

        
