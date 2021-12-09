import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS 


RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (44, 210, 215)
GREY = (128, 128, 128)
GREEN = (0,255,0)

BROWN = (156, 124, 101)
LIGHT_BROWN = (225, 210, 187)
DARK_BROWN = (101, 87, 84)
LIGHT_GREY = (240, 222, 176)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))