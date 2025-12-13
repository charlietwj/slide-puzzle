import pygame
import random
from enum import Enum, auto

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
TILE_SIZE = 80
HEIGHT = 4
WIDTH = 4
FPS = 60
X_START = 150
Y_START = 100

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (153, 204, 255)
DARKGRAY = (32, 32, 32)

TILE_COLOR = BLUE
BORDER_COLOR = DARKGRAY
BACKGROUND_COLOR = WHITE

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Slide Puzzle")
clock = pygame.time.Clock()
board = []

def setup_game():
    numbers = [i for i in range(WIDTH * HEIGHT)]
    random.shuffle(numbers)

    while board:
        board.pop()

    for i in range(HEIGHT):
        start = i * WIDTH
        end = (i+1) * WIDTH
        board.append(numbers[start:end])

setup_game()
running = True

class Move(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()

def make_move(move: Move) -> None:
    pos = None
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if board[i][j] == 0:
                pos = i, j
    
    i, j = pos
    if move == Move.LEFT:
        if j < WIDTH - 1:
            board[i][j] = board[i][j+1]
            board[i][j+1] = 0
    if move == Move.RIGHT:
        if j > 0:
            board[i][j] = board[i][j-1]
            board[i][j-1] = 0
    if move == Move.UP:
        if i < HEIGHT - 1:
            board[i][j] = board[i+1][j]
            board[i+1][j] = 0
    if move == Move.DOWN:
        if i > 0:
            board[i][j] = board[i-1][j]
            board[i-1][j] = 0

def handle_events():
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                make_move(Move.LEFT)
            elif event.key == pygame.K_RIGHT:
                make_move(Move.RIGHT)
            elif event.key == pygame.K_UP:
                make_move(Move.UP)
            elif event.key == pygame.K_DOWN:
                make_move(Move.DOWN)

def draw():
    screen.fill(BACKGROUND_COLOR)

    # Draw tiles
    for i in range(HEIGHT):
        for j in range(WIDTH):
            x = X_START + j * TILE_SIZE + j
            y = Y_START + i * TILE_SIZE + i
            pygame.draw.rect(screen, TILE_COLOR, (x, y, TILE_SIZE, TILE_SIZE))
    
    pygame.display.flip()

while running:
    handle_events()
    draw()
    clock.tick(FPS)

pygame.quit()

