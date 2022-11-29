import sys
import random
import pygame


pygame.init()

run = True

WIDTH = 320
HEIGHT = 240
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

NUMBER_OF_BALLS = 9

GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

balls = []
for x in range(NUMBER_OF_BALLS):
    balls.append({})

# initialize balls with random values
for ball in balls:
    ball['x'] = random.randint(0, WIDTH)
    ball['y'] = random.randint(0, HEIGHT)
    ball['radius'] = random.randint(5, 10)
    ball['dx'] = random.randint(1, 3)
    ball['dy'] = random.randint(1, 3)
    ball['speed'] = random.uniform(0.02, 0.06)

# debug print initialized values
for ball in balls:
    print(ball)

screen = pygame.display.set_mode([WIDTH, HEIGHT])

while run:
    screen.fill('blue')

    for ball in balls:
        pygame.draw.circle(screen, GREEN, (ball['x'], ball['y']), ball['radius'])

        # update position
        ball['x'] = ball['x'] + (ball['dx'] * ball['speed'])
        ball['y'] = ball['y'] + (ball['dy'] * ball['speed'])

        half_ball_radius = ball['radius'] // 2

        if (ball['x'] > WIDTH - half_ball_radius):
            ball['dx'] *= -1
            ball['x'] = WIDTH - half_ball_radius

        elif (ball['x'] < 0 + half_ball_radius):
            ball['dx'] *= -1
            ball['x'] = half_ball_radius

        elif (ball['y'] > HEIGHT - half_ball_radius):
            ball['dy'] *= -1
            ball['y'] = HEIGHT - half_ball_radius

        elif (ball['y'] < 0 + half_ball_radius):
            ball['dy'] *= -1
            ball['y'] = half_ball_radius

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
