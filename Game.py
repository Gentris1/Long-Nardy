import pickle

from Checker import Checker
from Dice import Dice


class Game:
    def __init__(self, player1, player2):
        self.player2 = player2
        self.player1 = player1

    def start_game(self, board):
        for i in range(15):
            checkerBlack = Checker((0, 0, 0), 0)
            board.add_checker(checkerBlack)
            checkerBlack = Checker((255, 255, 255), 0)
            board.add_checker(checkerBlack)
        #checkerBlack = Checker((0, 0, 0), 0)
        #board.add_checker(checkerBlack)
        # checkerBlack = Checker((0, 0, 0), 0)
        # board.add_checker(checkerBlack)
        # checkerBlack = Checker((0, 0, 0), 17)
        # board.add_checker(checkerBlack)
        # checkerBlack = Checker((0, 0, 0), 15)
        # board.add_checker(checkerBlack)

        #checkerBlack = Checker((255, 255, 255), 0)
        #board.add_checker(checkerBlack)
        # checkerBlack = Checker((255, 255, 255), 0)
        # board.add_checker(checkerBlack)
    def make_move(self):
        if self.player1.move_flag and len(self.player1.remaining_moves) == 0:
            self.player1.move_flag = False
            self.player2.move_flag = True
            self.player2.remaining_moves = Dice.get_random_numbers()
            self.player2.dice_numbers = self.player2.remaining_moves.copy()
        if self.player2.move_flag and len(self.player2.remaining_moves) == 0:
            self.player2.move_flag = False
            self.player1.move_flag = True
            self.player1.remaining_moves = Dice.get_random_numbers()
            self.player1.dice_numbers = self.player1.remaining_moves.copy()
        #if len(self.player1.dice_numbers) > 0 and len(self.player1.dice_numbers) == 0:
        #    self.player2.move_flag = True

        #if len(self.player2.dice_numbers) > 0 and len(self.player2.dice_numbers) == 0:
        #    self.player1.move_flag = True
    def reset_game(self, board):
        for i in range(len(board.board)):
            board.board[i].stack = []

        self.player1.move_flag = True
        self.player1.remaining_moves = Dice.get_random_numbers()
        self.player1.dice_numbers = self.player1.remaining_moves.copy()

        self.player2.move_flag = False
        self.player2.remaining_moves = Dice.get_random_numbers()
        self.player2.dice_numbers = self.player2.remaining_moves.copy()

        self.start_game(board)
    def save_game(self, board, player1, player2):
        game_state = {
            'board': board,
            'player1': player1,
            'player2': player2
        }
        with open('savegame.pkl', 'wb') as f:
            pickle.dump(game_state, f)
        print("Game saved successfully.")

    # Function to load the game state
    def load_game(self):
        try:
            with open('savegame.pkl', 'rb') as f:
                game_state = pickle.load(f)
                print("Game loaded successfully.")
                return game_state['board'], game_state['player1'], game_state['player2']
        except FileNotFoundError:
            print("No saved game found.")
            return None, None, None
