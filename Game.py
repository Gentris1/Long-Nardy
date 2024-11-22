from Dice import Dice


class Game:
    def __init__(self, player1, player2):
        self.player2 = player2
        self.player1 = player1

    def make_move(self):
        if self.player1.move_flag and len(self.player1.dice_numbers) == 0:
            self.player1.dice_numbers = Dice.get_random_numbers()
        if self.player2.move_flag and len(self.player2.dice_numbers) == 0:
            self.player2.dice_numbers = Dice.get_random_numbers()

        #if len(self.player1.dice_numbers) > 0 and len(self.player1.dice_numbers) == 0:
        #    self.player2.move_flag = True

        #if len(self.player2.dice_numbers) > 0 and len(self.player2.dice_numbers) == 0:
        #    self.player1.move_flag = True
