import random
class Dice:
    @staticmethod
    def get_random_numbers():
        return [random.randint(1, 6), random.randint(1, 6)]