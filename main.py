import pygame
import sys
import random

from Board import Board
from Checker import Checker
from Game import Game
from Menu import Menu
from Player import Player
from Screen import Screen

pygame.init()

running = True

number = random.randint(1, 6)
board = Board()

player1 = Player(True, (255, 255, 255))
player2 = Player(False, (0, 0, 0))

game = Game(player1, player2)

game.start_game(board)

# for i in range(15):
#    checkerBlack = Checker((0, 0, 0), 0)
#    board.add_checker(checkerBlack)
#    checkerWhite = Checker((255, 255, 255), 0)
#    board.add_checker(checkerWhite)
# checkerBlack = Checker((255, 255, 255), 9)
# board.add_checker(checkerBlack)
# checkerBlack = Checker((255, 255, 255), 14)
# board.add_checker(checkerBlack)
# checkerBlack = Checker((255, 255, 255), 18)
# board.add_checker(checkerBlack)
# checkerBlack = Checker((255, 255, 255), 9)
# board.add_checker(checkerBlack)
# checkerBlack = Checker((255, 255, 255), 9)
# board.add_checker(checkerBlack)
# checkerBlack = Checker((0, 0, 0), 1)
# board.add_checker(checkerBlack)
# checkerBlack = Checker((0, 0, 0), 2)
# board.add_checker(checkerBlack)
# checkerBlack = Checker((0, 0, 0), 0)
# board.add_checker(checkerBlack)
# checkerBlack = Checker((0, 0, 0), 4)
# board.add_checker(checkerBlack)
# checkerBlack = Checker((0, 0, 0), 10)
# board.add_checker(checkerBlack)
# checkerBlack = Checker((0, 0, 0), 9)
# board.add_checker(checkerBlack)
# checkerBlack = Checker((255, 255, 255), 18)
# board.add_checker(checkerBlack)
# checkerBlack = Checker((255, 255, 255), 22)
# board.add_checker(checkerBlack)


width, height = 800, 600
point_width = width // 14
board_margin = point_width

Menu.draw_menu(game, board)

while running:

    mouse_x, mouse_y = pygame.mouse.get_pos()
    board.count_total_checkers()
    if board.black_total_checkers == 0 or board.white_total_checkers == 0:
        game.reset_game(board)
        # continue
    game.make_move()
    Screen.draw_backgammon_board(board, game.player1, game.player2, mouse_x, mouse_y)

    board.get_ready_to_home()

    if game.player1.move_flag:
        board.activate_cells(mouse_x, mouse_y, game.player1)
        board.get_checker_possible_moves(game.player1)
    if game.player2.move_flag:
        board.activate_cells(mouse_x, mouse_y, game.player2)
        board.get_checker_possible_moves(game.player2)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if Screen.save_button_rect.collidepoint(mouse_pos):
                game.save_game(board, game.player1, game.player2)
            elif Screen.load_button_rect.collidepoint(mouse_pos):
                loaded_board, loaded_player1, loaded_player2 = game.load_game()
                if loaded_board:
                    board = loaded_board
                    game.player1.remaining_moves = loaded_player1.remaining_moves.copy()
                    game.player1.move_flag = loaded_player1.move_flag
                    game.player1.dice_numbers = loaded_player1.dice_numbers.copy()

                    game.player2.remaining_moves = loaded_player2.remaining_moves.copy()
                    game.player2.move_flag = loaded_player2.move_flag
                    game.player2.dice_numbers = loaded_player2.dice_numbers.copy()
            elif event.button == 1:
                if game.player1.move_flag:
                    board.move_checker(game.player1, mouse_x, mouse_y)
                    if board.flag_keep:  # and mouse_x > width - board_margin:
                        board.move_to_home(game.player1, mouse_x, mouse_y)

                    # board.move_to_home(player1)
                    # board.move_home()
                if game.player2.move_flag:
                    board.move_checker(game.player2, mouse_x, mouse_y)

                    # if board.flag_keep: #and mouse_x > width - board_margin:
                    board.move_to_home(game.player2, mouse_x, mouse_y)

                print(f"Левая кнопка мыши нажата на позиции {event.pos}")

pygame.quit()
sys.exit()
