import pygame
from pygame import Vector2

WIDTH = 800
HEIGHT = 600


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Text Rendering")

simple_text_color = (200, 200, 200)
simple_font = pygame.font.SysFont('Arial', 20)
simple_text = simple_font.render('Play', True, simple_text_color)

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


    screen.blit(simple_text, (0, 0))

    pygame.display.update()

pygame.quit()
