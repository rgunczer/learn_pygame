import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
GRID_SIZE = 64
GRID_LINE_WIDTH = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

pygame.display.set_caption("Draw Grid")

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    screen.fill(BLACK)

    pos_x = GRID_SIZE
    for x in range(WIDTH // GRID_SIZE):
        pygame.draw.line(screen, YELLOW, (pos_x, 0), (pos_x, HEIGHT), width=GRID_LINE_WIDTH)
        pos_x += GRID_SIZE

    pos_y = GRID_SIZE
    for y in range(HEIGHT // GRID_SIZE):
        pygame.draw.line(screen, YELLOW, (0, pos_y), (WIDTH, pos_y), width=GRID_LINE_WIDTH)
        pos_y += GRID_SIZE

    pygame.display.update()

pygame.quit()
