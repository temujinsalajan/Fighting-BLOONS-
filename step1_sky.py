import pygame as tm

W = 900
H = 600

tm.init() # we have initialized game engine
tm.display.set_caption("Its Temujin's Baloon ")
screen=tm.display.set_mode((W,H))

SKY = (150,200,255)

running = True
while True:
    for e in tm.event.get():
        if e.type == tm.QUIT:
            running = False




    screen.fill(SKY)
    tm.display.flip()



tm.quit()