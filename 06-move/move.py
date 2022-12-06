import pygame
from pygame import Vector2
import colors

WIDTH = 800
HEIGHT = 600


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the thing with keyboard")

hero_pos = Vector2(WIDTH / 2, HEIGHT / 2)

clock = pygame.time.Clock()
fps = 30
running = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT]:
        hero_pos.x -= 3

    if key_pressed[pygame.K_RIGHT]:
        hero_pos.x += 3

    screen.fill(colors.GREEN)

    pygame.draw.rect(screen, colors.RED, (hero_pos.x, hero_pos.y, 100, 100))

    pygame.display.update()

pygame.quit()
