import pygame
from pygame import Vector2

WIDTH = 800
HEIGHT = 600

menu_items = [
    { "text": "PLAY" },
    { "text": "SCORES" },
    { "text": "SETTINGS" },
    { "text": "ABOUT" }
]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom (Font) Text Menu Rendering")

text_color = (200, 200, 200)
font = pygame.font.Font("fonts/Checkpoint Charlie.ttf", 40)

for menu_item in menu_items:
    print(menu_item)
    text_surface = font.render(menu_item["text"], True, text_color)
    menu_item["surface"] = text_surface

clock = pygame.time.Clock()
fps = 30
running = True
while running:
    elapsedMs = clock.tick(fps)

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue

    posy = screen.get_height() // 2
    for menu_item in menu_items:
        text_surface = menu_item["surface"]
        xcenter = ( screen.get_width() - text_surface.get_width() ) // 2
        screen.blit(text_surface, (xcenter, posy))
        posy += text_surface.get_height() * 1.2

    pygame.display.update()

pygame.quit()
