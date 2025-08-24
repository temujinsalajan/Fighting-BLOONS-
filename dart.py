import pygame as pg

class Dart:
    def __init__(self, pos, vel, radius=5, color=(20, 20, 20)):
        self.pos = pg.Vector2(pos)
        self.vel = pg.Vector2(vel)
        self.radius = radius
        self.color = color
        self.alive = True

    def update(self, width, height):
        self.pos += self.vel
        if not (0 <= self.pos.x <= width and 0 <= self.pos.y <= height):
            self.alive = False

    def draw(self, surf):
        pg.draw.circle(surf, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)


# ----------------------------------------------------------
# TEST MODE — press SPACE to fire darts
# ----------------------------------------------------------
if __name__ == "__main__":
    pg.init()
    W, H = 600, 400
    screen = pg.display.set_mode((W, H))
    pg.display.set_caption("Test Dart — Press SPACE to Fire")
    clock = pg.time.Clock()

    darts = []  # <-- store multiple darts
    start_pos = (100, 200)  # where darts are fired from
    dart_speed = pg.Vector2(6, 0)  # horizontal speed

    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

            # Fire a new dart on SPACE press
            if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                darts.append(Dart(pos=start_pos, vel=dart_speed))

        screen.fill((200, 230, 255))

        # Update and draw all darts
        for d in darts[:]:
            d.update(W, H)
            d.draw(screen)
            if not d.alive:
                darts.remove(d)

        pg.display.flip()
        clock.tick(60)

    pg.quit()


