import pygame 

from checkers.constants import DARK_BROWN, SQUARE_SIZE, LIGHT_GREY, WIDTH, HEIGHT
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

DEPTH = 4
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while run:
        clock.tick(FPS)

        if game.turn == LIGHT_GREY:
            value, new_board = minimax(game.get_board(), DEPTH, LIGHT_GREY, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()