import pygame
import sys
import random

from Board import Board
from Checker import Checker
from Game import Game
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
#checkerBlack = Checker((0, 0, 0), 10)
#board.add_checker(checkerBlack)
#checkerBlack = Checker((0, 0, 0), 9)
#board.add_checker(checkerBlack)
# checkerBlack = Checker((255, 255, 255), 18)
# board.add_checker(checkerBlack)
# checkerBlack = Checker((255, 255, 255), 22)
# board.add_checker(checkerBlack)


width, height = 800, 600
point_width = width // 14
board_margin = point_width
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    board.count_total_checkers()
    if board.black_total_checkers == 0 or board.white_total_checkers == 0:
        game.reset_game(board)
        #continue
    game.make_move()
    Screen.draw_backgammon_board(board, player1, player2, mouse_x, mouse_y)



    board.get_ready_to_home()

    if player1.move_flag:
        board.activate_cells(mouse_x, mouse_y, player1)
        board.get_checker_possible_moves(player1)
    if player2.move_flag:
        board.activate_cells(mouse_x, mouse_y, player2)
        board.get_checker_possible_moves(player2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if player1.move_flag:
                    board.move_checker(player1, mouse_x, mouse_y)
                    if board.flag_keep: #and mouse_x > width - board_margin:
                        board.move_to_home(player1, mouse_x, mouse_y)

                    #board.move_to_home(player1)
                    #board.move_home()
                if player2.move_flag:
                    board.move_checker(player2, mouse_x, mouse_y)

                    #if board.flag_keep: #and mouse_x > width - board_margin:
                    board.move_to_home(player2, mouse_x, mouse_y)


                print(f"Левая кнопка мыши нажата на позиции {event.pos}")

pygame.quit()
sys.exit()
