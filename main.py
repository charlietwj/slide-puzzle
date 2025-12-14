import pygame
import random
from enum import Enum, auto

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
TILE_SIZE = 80
HEIGHT = 4
WIDTH = 4
FPS = 240
X_START = 200
Y_START = 100
FONT_SIZE = TILE_SIZE // 3
BORDER_WIDTH = 4
ANIMATION_SPEED = 1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (153, 204, 255)
DARKGRAY = (32, 32, 32)
LIGHTGRAY = (192, 192, 192)
DARKBLUE = (0, 76, 153)

TILE_COLOR = BLUE
BORDER_COLOR = DARKBLUE
BACKGROUND_COLOR = WHITE
FONT_COLOR = DARKGRAY

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Slide Puzzle")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", int(FONT_SIZE))
board = [[0] * WIDTH for _ in range(HEIGHT)]

class Move(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()

def draw_tile(i, j, offset: tuple = (0, 0)):
    x = X_START + j * TILE_SIZE + j + offset[0]
    y = Y_START + i * TILE_SIZE + i + offset[1]
    pygame.draw.rect(screen, TILE_COLOR, (x, y, TILE_SIZE, TILE_SIZE))

    number = board[i][j]
    text_surface = font.render(str(number), True, FONT_COLOR)
    text_rect = text_surface.get_rect()
    x += TILE_SIZE // 2
    y += TILE_SIZE // 2
    text_rect.center = x, y
    screen.blit(text_surface, text_rect)

def animate(start: tuple, dx: int, dy: int):
    i, j = start
    surface = screen.copy()
    x = X_START + j * TILE_SIZE + j
    y = Y_START + i * TILE_SIZE + i
    pygame.draw.rect(surface, BACKGROUND_COLOR, (x, y, TILE_SIZE, TILE_SIZE))

    for k in range(0, TILE_SIZE + 1, ANIMATION_SPEED):
        screen.blit(surface, (0, 0))
        distance = k
        offset_x = dx * distance
        offset_y = dy * distance
        draw_tile(i, j, (offset_x, offset_y))
        pygame.display.flip()
        clock.tick(FPS)

def make_move(move: Move, slide_animation: bool = True) -> None:
    pos = None
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if board[i][j] == 0:
                pos = i, j
    
    i, j = pos
    dx, dy = None, None
    start = None
    
    if move == Move.LEFT:
        if j < WIDTH - 1:
            start = (i, j+1)
            dx = -1
            dy = 0
    if move == Move.RIGHT:
        if j > 0:
            start = (i, j-1)
            dx = 1
            dy = 0
    if move == Move.UP:
        if i < HEIGHT - 1:
            start = (i+1, j)
            dx = 0
            dy = -1
    if move == Move.DOWN:
        if i > 0:
            start = (i-1, j)
            dx = 0
            dy = 1

    if start:
        if slide_animation:
            animate(start, dx, dy)
        board[i][j] = board[start[0]][start[1]]
        board[start[0]][start[1]] = 0

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
            if board[i][j] == 0:
                continue
            
            draw_tile(i, j)

    # Draw border
    x = X_START - BORDER_WIDTH
    y = Y_START - BORDER_WIDTH
    width = TILE_SIZE * WIDTH + (WIDTH - 1) + BORDER_WIDTH * 2
    height = TILE_SIZE * HEIGHT + (HEIGHT - 1) + BORDER_WIDTH * 2
    pygame.draw.rect(screen, BORDER_COLOR, (x, y, width, height), BORDER_WIDTH)
    
    pygame.display.flip()


def setup_game():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            board[i][j] = i * WIDTH + j + 1
    board[HEIGHT-1][WIDTH-1] = 0

    shuffle_moves = 10000
    moves = [Move.LEFT, Move.RIGHT, Move.UP, Move.DOWN]
    for _ in range(shuffle_moves):
        i = random.randint(0, 3)
        make_move(moves[i], slide_animation=False)

setup_game()
running = True

while running:
    handle_events()
    draw()

pygame.quit()

