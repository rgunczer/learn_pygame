import pygame

pygame.init()

run = True

WIDTH = 320
HEIGHT = 240
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

radius = 20
pos = (HALF_WIDTH, HALF_HEIGHT)

screen = pygame.display.set_mode([WIDTH, HEIGHT])

while run:
    screen.fill('blue')

    pygame.draw.rect(screen, RED, (10, 40, 100, 20))
    pygame.draw.circle(screen, GREEN, pos, radius)
    pygame.draw.polygon(screen, YELLOW, ((0,0), (100, 10), (90,20), (30, 40)))
    pygame.draw.line(screen, WHITE, (200, 200), (300, 220), width=3)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
