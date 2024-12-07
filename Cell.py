from Checker import Checker


class Cell:
    stack: list[Checker]
    is_active: bool
    x: int
    possible_cells_to_move: set[int]

    def __init__(self, x):
        self.stack = []
        self.x = x
        self.is_active = False
        self.possible_cells_to_move = set()

    @property
    def color(self):
        return self.stack[0].color if len(self.stack) > 0 else None