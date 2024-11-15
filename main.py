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

color = (255, 255, 255)
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
