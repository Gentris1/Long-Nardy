class Player:
    move_flag: bool
    dice_numbers: list[int]

    def __init__(self, move_flag, color):
        self.move_flag = move_flag
        self.color = color
        self.dice_numbers = []