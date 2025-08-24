import pygame as tm
import random
W = 900
H = 600

tm.init() # we have initialized game engine
tm.display.set_caption("Its Temujin's Baloon ")
screen=tm.display.set_mode((W,H))

SKY = (150,200,255)
BLOON_COLORS = [
    (0,0,255),# blue
    (255,0,0),#red
    (0,255,0),#green
    (0,255,255),# sky type
    (255,255,0), # yellow
    
]
def draw_baloon(surf,x,y,r,col):
    tm.draw.circle(surf,col,(x,y),r)
    tm.draw.line(surf,(90,90,90),(x,y+r),(x,y+r+20),2) # line so we wrote starting and endino
    tm.draw.polygon(surf,col,[(x-6, y+r-3), (x+6, y+r-3), (x, y+r+6)]) # polygon or triangle kind of hting so 3 point


arc_pts= []
start_x = 500
start_y = 200
gap_x = 60
gap_y = 60
for row in range(4):
    for col in range(6):
        x = start_x + col *gap_x
        y = start_y + row * gap_y
        arc_pts.append((x,y))



running = True
while True:
    for e in tm.event.get():
        if e.type == tm.QUIT:
            running = False



    screen.fill(SKY)
    for i,(x,y) in enumerate(arc_pts):
        draw_baloon(screen,x,y,18,BLOON_COLORS[i%len(BLOON_COLORS)])

    tm.display.flip()


tm.quit()