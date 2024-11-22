import pygame
import sys
import random

from Board import Board
from Checker import Checker
from Dice import Dice
from Game import Game
from Player import Player
from Screen import Screen

pygame.init()

running = True

number = random.randint(1, 6)
board = Board()

color = (0, 0, 0)
player1 = Player(False, (255, 255, 255))
player2 = Player(True, (0, 0, 0))

# color = (255, 255, 255)
# player1 = Player(True, (255, 255, 255))
# player2 = Player(False, (0, 0, 0))

checkerBlack = Checker(color, 0)
checkerWhite = Checker((255, 255, 255), 0)
for i in range(15):
    board.add_checker(checkerBlack)
    #board.add_checker(checkerWhite)

checkerBlack = Checker(color, 21)
board.add_checker(checkerBlack)

checkerBlack = Checker(color, 5)
board.add_checker(checkerBlack)
checkerBlack = Checker(color, 6)
board.add_checker(checkerBlack)
checkerBlack = Checker(color, 7)
board.add_checker(checkerBlack)

checkerBlack = Checker(color, 8)
board.add_checker(checkerBlack)
checkerBlack = Checker(color, 9)
board.add_checker(checkerBlack)
checkerBlack = Checker(color, 10)
board.add_checker(checkerBlack)
checkerBlack = Checker(color, 11)
board.add_checker(checkerBlack)
checkerBlack = Checker(color, 13)
board.add_checker(checkerBlack)
checkerBlack = Checker(color, 15)
board.add_checker(checkerBlack)
#checkerBlack = Checker(color, 12)
#board.add_checker(checkerBlack)


game = Game(player1, player2)

while running:
    game.make_move()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    Screen.draw_backgammon_board(board, player1, player2, mouse_x, mouse_y)
    if player1.move_flag:
        board.activate_cells(mouse_x, mouse_y, player1)
    if player2.move_flag:
        board.activate_cells(mouse_x, mouse_y, player2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if player1.move_flag:
                    Board.move_checker(board, player1, mouse_x, mouse_y)
                if player2.move_flag:
                    Board.move_checker(board, player2, mouse_x, mouse_y)
                print(f"Левая кнопка мыши нажата на позиции {event.pos}")

pygame.quit()
sys.exit()
