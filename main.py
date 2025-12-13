import pygame
import random
from enum import Enum, auto

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
TILE_SIZE = 80
HEIGHT = 4
WIDTH = 4

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
        start = i * HEIGHT
        end = i * HEIGHT + WIDTH
        board.append(numbers[start:end])

setup_game()
running = True

class Move(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()

def make_move(move: Move) -> None:
    if move == Move.LEFT:
        print(f"Move left")
    if move == Move.RIGHT:
        print(f"Move right")
    if move == Move.UP:
        print(f"Move up")
    if move == Move.DOWN:
        print(f"Move down")


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
    
    pygame.display.flip()

while running:
    handle_events()
    draw()
    clock.tick(60)

pygame.quit()

