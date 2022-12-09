import pygame
from pygame import Vector2

WIDTH = 800
HEIGHT = 600


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom (Font) Text Rendering")

text_color = (200, 200, 200)
font = pygame.font.Font("fonts/Checkpoint Charlie.ttf", 30)
text = font.render('PLAY', True, text_color)

clock = pygame.time.Clock()
fps = 30
running = True
while running:
    clock.tick(fps)

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue


    screen.blit(text, (0, 0))

    pygame.display.update()

pygame.quit()
