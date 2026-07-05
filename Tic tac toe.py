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
X_COLOR = (168, 50, 92)
O_COLOR = (235, 64, 52)

running = True
base_rect = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)
board = []
rects = [base_rect.copy() for i in range(ROWS*COLS)]


def draw_grid(screen):
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)


def draw_rect(screen):
    global rects 
    global board
    for x in range(ROWS):
        for y in range(COLS):
            rects[x*ROWS+y].y = y*CELL_SIZE
            rects[x*ROWS+y].x = x*CELL_SIZE
            pygame.draw.rect(screen, (BG_COLOR), rects[x*ROWS + y])
        board.append(['','',''])
    print(board)

def draw_markers(screen, rect, player):
    x0,y0 = rect.topleft
    x1,y1 = rect.bottomright

    x2,y2 = rect.topright
    x3,y3 = rect.bottomleft

    margin = 20
    if player == "X":
        pygame.draw.line(screen, X_COLOR, (x0+margin, y0+margin), (x1-margin, y1-margin), width=LINE_WIDTH)
        pygame.draw.line(screen, X_COLOR, (x2-margin, y2+margin), (x3+margin, y3-margin), width=LINE_WIDTH)
    else:
        pygame.draw.circle(screen, O_COLOR, rect.center, rect.width//2-20, width=LINE_WIDTH)


def winCheck(player):
    for row in range(ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True, row, "Row"
    for col in range(COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True, col, "Column"
        
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True, "LR", "Top - Bottom Diagonal"
            
    
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True, "RL", "Bottom - Top Diagonal"
    
    return False, "_", "_"
    
def boardFull():
    full = 0
    for row in board:
        for marker in row:
            if marker != "":
                full+=1
           
    if full == 9:
        return True

def winLine(screen, pos, winType):
    start = 0,0
    end = 0,0
    if winType == "Column":
        start = (0, pos*CELL_SIZE+CELL_SIZE//2)
        end = (CELL_SIZE * COLS, pos*CELL_SIZE+CELL_SIZE//2)
        
    if winType == "Row":
        start = (pos*CELL_SIZE+CELL_SIZE//2, 0)
        end = (pos*CELL_SIZE+CELL_SIZE//2, CELL_SIZE * ROWS)

    if winType == "Top - Bottom Diagonal":
        start = (0, 0)
        end = (CELL_SIZE * ROWS, CELL_SIZE * COLS)
    
    if winType == "Bottom - Top Diagonal":
        start = (0, CELL_SIZE * COLS)
        end = (CELL_SIZE * ROWS, 0)

    
    
    pygame.draw.line(screen, (230, 66, 25), start, end, width=LINE_WIDTH)

def main():
    pygame.init()
    global running
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG_COLOR)
    draw_rect(screen)
    draw_grid(screen)
    pygame.display.flip()

    player = "X"

    pygame.display.set_caption("Play Tic Tac Toe")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if running:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not boardFull():
                        if event.button == 1:
                            for rect in rects:
                                if rect.collidepoint(event.pos):
                                    x, y = event.pos
                                    x = x//CELL_SIZE
                                    y = y//CELL_SIZE
                                    board[x][y] = player
                                    print(board)
                                    draw_markers(screen,rect, player)

                            win,pos,winType = winCheck(player)

                            if win:
                                print(winType + ": " + player)
                                pygame.display.set_caption("Congratulations player " + player)
                                winLine(screen, pos, winType)
                                running = False

                            if player == "X":
                                player = "O"
                            else:
                                player = "X"
                    else:
                        pygame.display.set_caption("It's a tie!")

        pygame.display.flip()

main()
