from pygame import *
mixer.init()
mixer.music.load("Elevator Music - So Chill.mp3")
bedroomPic=image.load("bedroom.jpg")
plantPic=image.load("plant.jpg")
font.init()
WIDTH, HEIGHT = 1200, 900
size=(WIDTH, HEIGHT)
screen = display.set_mode(size)
arialS = font.SysFont('Arial', 30)

running = True
def bedroom():
    hi=False
    wakeupRect=Rect(300,600,700,100)
    plantRect=Rect(900,200,250,100)
    gotobathRect=Rect(900,350,250,100)
    step1=False
    step2=False
    step3=False
    step4=False
    while True:
        for evt in event.get():
            if evt.type == QUIT:
                running = False

        if step1==False:
            arial = font.SysFont('Arial', 100)
            wakeupText= arial.render(str("Wake up"), True, (0, 0, 0))
            draw.rect(screen,(100,100,100),wakeupRect)
            screen.blit(wakeupText, (510, 585))
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        keys=key.get_pressed()
        arial = font.SysFont('Arial', 30)
        if wakeupRect.collidepoint(mx,my) and step1==False:
            draw.rect(screen,(0,200,250),wakeupRect)
            screen.blit(wakeupText, (510, 585))
        if wakeupRect.collidepoint(mx,my) and mb[0]:
            screen.blit(bedroomPic,(0,0))
            step1=True
        if step1==True:
            screen.blit(bedroomPic,(0,0))
            draw.rect(screen,(100,100,100),plantRect)
            draw.rect(screen,(100,100,100),gotobathRect)
            if(plantRect.collidepoint(mx,my)):
                draw.rect(screen,(0,200,250),plantRect)
            elif gotobathRect.collidepoint(mx,my):
                draw.rect(screen, (0, 200, 250),gotobathRect)
            if plantRect.collidepoint(mx,my) and evt.type==MOUSEBUTTONUP:
                step2=True
                step1=False
        if step2:
            waterRect = Rect(900, 200, 250, 100)
            talkRect = Rect(900, 350, 250, 100)
            gobackRect = Rect(900, 500, 250, 100)
            arial = font.SysFont('Arial', 30)
            screen.fill((0, 0, 0))
            screen.blit(plantPic, (0, 0))
            talkText = arial.render(str("Water plant"), True, (0, 0, 0))
            talkText2 = arial.render(str("Talk to plant"), True, (0, 0, 0))
            talkText3 = arial.render(str("back to bed"), True, (0, 0, 0))
            draw.rect(screen, (100, 100, 100), waterRect)
            draw.rect(screen, (100, 100, 100), talkRect)
            draw.rect(screen, (100, 100, 100), gobackRect)
            screen.blit(talkText, (600, 200))
            screen.blit(talkText2, (600, 350))
            screen.blit(talkText3, (600, 500))
            display.update()
            if waterRect.collidepoint(mx, my):
                draw.rect(screen, (0, 200, 250), waterRect)
            elif talkRect.collidepoint(mx, my):
                draw.rect(screen, (0, 200, 250), talkRect)
            elif gobackRect.collidepoint(mx, my):
                draw.rect(screen, (0, 200, 250), gobackRect)
            if waterRect.collidepoint(mx, my) and evt.type == MOUSEBUTTONDOWN:
                step3 = True
                step2=False
            elif talkRect.collidepoint(mx, my) and evt.type == MOUSEBUTTONDOWN:
                step4 = True
                step2=False
        if step3:
            print("hi222")
            arial = font.SysFont('Arial', 30)
            waterRect = Rect(900, 200, 250, 100)
            screen.blit(plantPic, (0, 0))
            talkText = arial.render(str("Drink up. You’ve gotta grow strong."), True, (0, 0, 0))
            screen.fill((255, 255, 255))
            screen.blit(plantPic, (0, 0))
            screen.blit(talkText, (600, 200))
            display.update()
            time.wait(2000)
            step3=False
            step1=True
        elif step4:
            talkText = arial.render(str("Good morning"), True, (0, 0, 0))
            lis = [".....", "How have you been?", ".....", "Need more water?", "ok, goodbye", "....",
                   "Say something", "Say something", "It’s like you’re not even alive...", "ok goodbye"]
            screen.fill((255, 255, 255))
            screen.blit(plantPic, (0, 0))
            screen.blit(talkText, (700, 200))
            display.update()
            time.wait(1000)
            screen.fill((255, 255, 255))
            screen.blit(plantPic,(0,0))
            talkText= arial.render(str("....."),True,(0,0,0))
            screen.blit(talkText, (700, 200))
            display.update()
            time.wait(1000)
            screen.fill((255, 255, 255))
            screen.blit(plantPic, (0, 0))
            talkText = arial.render(str("Need more water?"), True, (0, 0, 0))
            screen.fill((255, 255, 255))
            screen.blit(plantPic, (0, 0))
            screen.blit(talkText, (700, 200))
            display.update()
            time.wait(1000)
            screen.fill((255, 255, 255))
            screen.blit(plantPic, (0, 0))
            talkText = arial.render(str("ok, goodbye"), True, (0, 0, 0))
            screen.blit(talkText, (700, 200))
            display.update()
            time.wait(1000)
            screen.fill((255, 255, 255))
            screen.blit(plantPic, (0, 0))
            talkText = arial.render(str("Say something"), True, (0, 0, 0))
            screen.blit(talkText, (700, 200))
            display.update()
            time.wait(1000)
            screen.fill((255, 255, 255))
            screen.blit(plantPic, (0, 0))
            talkText = arial.render(str("It’s like you’re not even....alive"), True, (0, 0, 0))
            screen.blit(talkText, (700, 200))
            display.update()
            time.wait(1000)
            screen.blit(plantPic, (0, 0))
            step4=False
            step1=True
        elif gotobathRect.collidepoint(mx,my) and mb[0]:
            break
        display.update()
def bathroom():
    bathroomPic=image.load("Bathroom.png")

    bathtubRect=Rect(1100,200,250,100)
    sinkRect=Rect(1100,350,250,100)
    livingRect=Rect(1100,500,250,100)

    bathtubText = arialS.render(str("Bathtub"), True, (0, 0, 0))
    sinkText = arialS.render(str("Sink"), True, (0, 0, 0))
    livingText = arialS.render(str("Living Room"), True, (0, 0, 0))

    while True:
        for evt in event.get():
            if evt.type == QUIT:
                running = False
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        if bathtubRect.collidepoint(mx,my) and mb[0]:
            bathTub()
        elif sinkRect.collidepoint(mx,my) and mb[0]:
            sink()
        screen.blit(bathroomPic, (0,0))

        draw.rect(screen, (100, 100, 100), bathtubRect)
        draw.rect(screen, (100, 100, 100), sinkRect)
        draw.rect(screen, (100, 100, 100), livingRect)

        screen.blit(bathtubText, (1100, 200))
        screen.blit(sinkText, (1100, 350))
        screen.blit(livingText, (1100, 500))

        display.update()

def bathTub():
    bathtubPic = image.load("bathtubPic.png")

    nvmRect = Rect(1100, 250, 250, 100)

    screen.fill((255,255,255))

    bathtubText1 = arialS.render(str("A nice hot shower would be nice right now..."), True, (0, 0, 0))
    bathtubText2 = arialS.render(str("I shouldn't do that"), True, (0, 0, 0))

    while True:
        for evt in event.get():
            if evt.type == QUIT:
                running = False
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        screen.blit(bathtubPic, (0,0))

        draw.rect(screen, (100, 100, 100), nvmRect)

        screen.blit(bathtubText1, (700,0))

        display.update()
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
        
       
        
  

        
