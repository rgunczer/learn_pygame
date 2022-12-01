import pygame

WIDTH = 640
HEIGHT = 480
GRID_SIZE = 128
GRID_LINE_WIDTH = 1

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

def draw_grid():
    pos_x = GRID_SIZE
    for x in range(WIDTH // GRID_SIZE):
        pygame.draw.line(screen, YELLOW, (pos_x, 0), (pos_x, HEIGHT), width=GRID_LINE_WIDTH)
        pos_x += GRID_SIZE

    pos_y = GRID_SIZE
    for y in range(HEIGHT // GRID_SIZE):
        pygame.draw.line(screen, YELLOW, (0, pos_y), (WIDTH, pos_y), width=GRID_LINE_WIDTH)
        pos_y += GRID_SIZE

def calc_tile_pos(x, y):
    new_x = (x // GRID_SIZE) * GRID_SIZE
    new_y = (y // GRID_SIZE) * GRID_SIZE
    print(f"new_x is: {new_x}, new_y is: {new_y}")
    return (new_x, new_y)

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

pygame.display.set_caption("Stamping with Mouse and Align Sprite to grid")

sprite = pygame.image.load('images/crate.png')
sprite = pygame.transform.scale(sprite, (128, 128))

spriteWidth = sprite.get_width()
spriteHeight = sprite.get_height()

crate_positions = []

game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            new_tile_pos = calc_tile_pos(x, y)
            crate_positions.append(new_tile_pos)

    screen.fill(BLACK)

    draw_grid()

    for pos in crate_positions:
        screen.blit(sprite, pos)

    pygame.display.update()

pygame.quit()
