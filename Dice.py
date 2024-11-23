import random
class Dice:
    @staticmethod
    def get_random_numbers():
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        if a == b:
            return [a]*4
        return [a, b]