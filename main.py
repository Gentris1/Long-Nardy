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

checkerBlack = Checker((0, 0, 0), 0)
checkerWhite = Checker((255, 255, 255), 0)
for i in range(15):
    board.add_checker(checkerBlack)
    #board.add_checker(checkerWhite)
checkerWhite = Checker((255, 255, 255), 3)
board.add_checker(checkerWhite)
checkerWhite = Checker((255, 255, 255), 9)
board.add_checker(checkerWhite)
checkerWhite = Checker((255, 255, 255), 11)
board.add_checker(checkerWhite)
checkerWhite = Checker((255, 255, 255), 13)
board.add_checker(checkerWhite)
checkerWhite = Checker((255, 255, 255), 21)
board.add_checker(checkerWhite)
checkerWhite = Checker((255, 255, 255), 20)
board.add_checker(checkerWhite)
checkerWhite = Checker((255, 255, 255), 19)
board.add_checker(checkerWhite)
checkerWhite = Checker((255, 255, 255), 22)
board.add_checker(checkerWhite)

player1 = Player(True, (255, 255, 255))
player2 = Player(False, (0, 0, 0))

game = Game(player1, player2)

while running:
    game.make_move()
    Screen.draw_backgammon_board(board.board, player1, player2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
