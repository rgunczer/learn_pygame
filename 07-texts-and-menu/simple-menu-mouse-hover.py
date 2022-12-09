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

def is_mouse_inside(menu_item, posy, mousex, mousey):
    rect = menu_item["rect"]
    print(rect)
    xcenter = ( screen.get_width() - rect.width ) // 2
    if mousex > xcenter and mousex < (xcenter + rect.width) and \
        mousey > posy and mousey < (posy + rect.height):
        return True

    return False


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom (Font) Text Menu Rendering with Mouse Hover")

text_color = (150, 150, 150)
text_color_hover = (255, 250, 250)
font = pygame.font.Font("fonts/Checkpoint Charlie.ttf", 40)

for menu_item in menu_items:
    print(menu_item)
    text_surface = font.render(menu_item["text"], True, text_color)
    menu_item["surface"] = text_surface
    menu_item["rect"] = text_surface.get_rect()

    text_surface_hover = font.render(menu_item["text"], True, text_color_hover)
    menu_item["surface_hover"] = text_surface_hover

mouse_dot_radius = 4
mousex = 0
mousey = 0
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
        elif event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos

    posy = screen.get_height() // 2
    for menu_item in menu_items:
        if is_mouse_inside(menu_item, posy, mousex, mousey):
            surface_key = "surface"
        else:
            surface_key = "surface_hover"

        text_surface = menu_item[surface_key]
        xcenter = ( screen.get_width() - text_surface.get_width() ) // 2
        screen.blit(text_surface, (xcenter, posy))
        posy += text_surface.get_height() * 1.2

    pygame.draw.circle(screen, (0, 255, 0), (mousex, mousey), mouse_dot_radius)

    pygame.display.update()

pygame.quit()
