from Checker import Checker


class Cell:
    stack: list[Checker]
    accommodation: bool
    x: object

    def __init__(self, x):
        self.stack = []
        self.x = x
        self.accommodation = False

    @property
    def color(self):
        return self.stack[0].color if len(self.stack) > 0 else None