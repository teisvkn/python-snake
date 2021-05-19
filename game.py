import pygame

HEIGHT = 600
WIDTH = 1200
BORDER = 20
fgColor = pygame.Color("green")
bgColor = pygame.Color("black")

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect((0, 0), (WIDTH, BORDER)))
pygame.draw.rect(screen, fgColor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
pygame.draw.rect(screen, fgColor, pygame.Rect((0, HEIGHT-BORDER), (WIDTH, BORDER)))

class Pad:
    width = 20
    height = 100
    x = BORDER # initiate away from border
    y = BORDER # initiate away from border
    sx = 0 # directional speed 
    sy = 0 # directional speed

    def draw(self, color): 
        global screen
        pygame.draw.rect(
            screen, 
            color, 
            pygame.Rect(
                self.x,
                self.y,
                self.width,
                self.height
            )
        )

    # erase from current position, 
    # update position and redraw at new position
    def move(self, dx, dy):
        global screen, bgColor, fgColor, BORDER, HEIGHT, WIDTH
        # remove current drawing
        self.draw(bgColor)
        # change coordinates
        self.x = WIDTH - self.width
        self.y = max(BORDER + 1, min(HEIGHT - BORDER - self.height - 1, self.y + dy))
        # draw at new position
        self.draw(fgColor)

    def update(self):
        self.move(self.sx, self.sy)


class Ball:
    radius = 10
    x = BORDER + 10 # initiate away from border
    y = BORDER + 10 # initiate away from border
    sx = 4 # directional speed 
    sy = 2 # directional speed
    pad = None

    def __init__(self, pad) -> None:
        self.pad = pad

    def draw(self, color): 
        global screen
        pygame.draw.circle(
            screen, 
            color, 
            (self.x, self.y),
            self.radius
        )

    # erase from current position, 
    # update position and redraw at new position
    def move(self, dx, dy):
        global screen, bgColor, fgColor, BORDER, HEIGHT, WIDTH
        # remove current drawing
        self.draw(bgColor)
        # change coordinates        
        self.x = max(BORDER + self.radius, min(WIDTH - self.radius, self.x + dx))
        self.y = max(BORDER + self.radius, min(HEIGHT - BORDER - self.radius, self.y + dy))

        self.detectBorderCollision()

        # draw at new position
        self.draw(fgColor)

    def update(self):
        self.move(self.sx, self.sy)

    def detectBorderCollision(self):
        # hits the upper or lower border
        if (self.y + self.radius >= HEIGHT - BORDER or self.y - self.radius <= BORDER):
            self.sy = -self.sy

        # Hits the left most border
        if (self.x <= BORDER + self.radius):
            self.sx = -self.sx

        # detect pad collision
        if ((self.x + self.radius >= WIDTH - BORDER) and (pad.y < self.y < pad.y + pad.height) ):
            self.sx = -self.sx




pad = Pad()
ball = Ball(pad)


def redraw():
    pad.update()
    ball.update()
    pygame.display.flip()


clock = pygame.time.Clock()

while True:
    event = pygame.event.poll()
    
    # print(event)

    if event.type == pygame.QUIT:
        print("quit")
        break

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            # pad.move(0, 10)
            pad.sy = 10
            print("move down")
        elif event.key == pygame.K_UP:
            # pad.move(0,-10)
            pad.sy = -10
            print("move up")

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            pad.sy = 0
            print("stop")


    redraw()
    clock.tick(60)


pygame.quit()

# while TRUE: