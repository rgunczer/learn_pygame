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

ball_radius = 20
half_ball_radius = ball_radius // 2
pos = (HALF_WIDTH, HALF_HEIGHT)
dx = 1
dy = 1
speed = 0.05

screen = pygame.display.set_mode([WIDTH, HEIGHT])

while run:
    screen.fill('blue')

    pygame.draw.circle(screen, GREEN, pos, ball_radius)

    new_x = pos[0] + (dx * speed)
    new_y = pos[1] + (dy * speed)

    if (new_x > WIDTH - half_ball_radius):
        dx *= -1
        new_x = WIDTH - half_ball_radius

    elif (new_x < 0 + half_ball_radius):
        dx *= -1
        new_x = half_ball_radius

    elif (new_y > HEIGHT - half_ball_radius):
        dy *= -1
        new_y = HEIGHT - half_ball_radius

    elif (new_y < 0 + half_ball_radius):
        dy *= -1
        new_y = half_ball_radius

    pos = (new_x, new_y)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
