import pygame
import sys

# Window size
WIDTH = 600
HEIGHT = 600

# Grid
ROWS = COLS = 3
CELL_SIZE = WIDTH//ROWS

# Colors (R, G, B)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
LINE_WIDTH = 15 

running = True
base_rect = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)
rects = [base_rect.copy() for i in range(ROWS*COLS)]


def draw_grid(screen):
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)


def draw_rect(screen):
    global rects 
    for x in range(ROWS):
        for y in range(COLS):
            rects[x*ROWS+y].y = y*CELL_SIZE
            rects[x*ROWS+y].x = x*CELL_SIZE
            pygame.draw.rect(screen, (BG_COLOR), rects[x*ROWS + y])

def draw_markers(screen, rect):
    pygame.draw.line(screen, (0, 0, 0), rect.topleft, rect.bottomright, width=LINE_WIDTH)
    pygame.draw.line(screen, (0, 0 ,0), rect.topright, rect.bottomleft, width=LINE_WIDTH)
    

def main():
    pygame.init()
    global running
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG_COLOR)
    draw_rect(screen)
    draw_grid(screen)
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for rect in rects:
                        if rect.collidepoint(event.pos):
                            draw_markers(screen,rect)

        pygame.display.flip()

main()
