import pygame
from pygame import Vector2
from turret import Turret

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)

pygame.display.set_caption("Turret Seek Test")

screen.fill((0, 0, 0))

def load_and_scale_image(scale, path_to_image):
    image = pygame.image.load(path_to_image)
    iwidth, iheight = image.get_size()
    new_size = (round(iwidth * scale), round(iheight * scale))
    scaled_image = pygame.transform.smoothscale(image, new_size)
    return scaled_image


image_scale = 0.25
tower_sprite = load_and_scale_image(image_scale, '../../assets/td_basic_towers/PNG/Tower.png')
cannon_sprite = load_and_scale_image(image_scale, '../../assets/td_basic_towers/PNG/Cannon.png')

mouse_dot_radius = 4
mousex = 0
mousey = 0
turrets = []
clock = pygame.time.Clock()
fps = 30
game_over = False

while not game_over:
    clock.tick(fps)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            continue
        elif event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            turrets.append(
                Turret(tower_sprite, cannon_sprite, (mousex, mousey))
            )

    for turret in turrets:
        # turret.update()
        turret.seekTarget(Vector2(mousex, mousey))
        turret.draw(screen)

    pygame.draw.circle(screen, (0, 255, 0), (mousex, mousey), mouse_dot_radius)

    pygame.display.update()

pygame.quit()
