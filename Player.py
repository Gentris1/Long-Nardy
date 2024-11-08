class Player:
    move_flag = False
    dice_numbers = None

    def __init__(self, move_flag, color):
        self.move_flag = move_flag
        self.color = color
