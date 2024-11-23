class Checker:
    possible_cells_to_move: set[int]
    def __init__(self, color, x):
        self.x = x
        self.color = color
        self.possible_cells_to_move = set()
