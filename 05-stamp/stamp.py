import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

pygame.display.set_caption("Stamping with Mouse")

BLACK = (0, 0, 0)

sprite = pygame.image.load('images/crate.png')
sprite = pygame.transform.scale(sprite, (128, 128))

spriteWidth = sprite.get_width()
spriteHeight = sprite.get_height()

crate_positions = [(0, 0), (300, 200)]

game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            crate_positions.append((x, y))

    screen.fill(BLACK)

    for pos in crate_positions:
        screen.blit(sprite, pos)

    pygame.display.update()

pygame.quit()
