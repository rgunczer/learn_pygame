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

    for y in range(screen.get_height() // GRID_SIZE + 1): # rows
        for x in range(screen.get_width() // GRID_SIZE + 1): # cols
            pygame.draw.rect(screen, YELLOW, [x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE], 1)

    pygame.display.update()

pygame.quit()
