from pygame import *
mixer.init()
mixer.music.load("Elevator Music - So Chill.mp3")
font.init()
arial = font.SysFont('Arial',60)
while running:
    for evt in event.get():  
        if evt.type == QUIT: 
            running = False
   
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()


    display.update()
quit()
        
       
        
  

        
