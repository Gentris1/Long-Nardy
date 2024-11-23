from Dice import Dice


class Player:
    move_flag: bool
    remaining_moves: list[int]
    dice_numbers: list[int]
    def __init__(self, move_flag, color):
        self.move_flag = move_flag
        self.color = color
        self.remaining_moves = Dice.get_random_numbers()
        self.dice_numbers = self.remaining_moves.copy()