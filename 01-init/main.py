import pygame

pygame.init()

run = True

WIDTH = 320
HEIGHT = 240
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

GREEN = (0, 255, 0)

radius = 20
pos = (HALF_WIDTH, HALF_HEIGHT)

screen = pygame.display.set_mode([WIDTH, HEIGHT])

while run:
    screen.fill('blue')

    pygame.draw.circle(screen, GREEN, pos, radius)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
