from Cell import Cell


class Board:
    board: list[Cell]
    def __init__(self):
        self.board = [Cell(x) for x in range(24)]

    def add_checker(self, checker):
        if checker.color == (255, 255, 255):
            self.add_color_checker(checker, get_white_up_cord(checker.x),
                                   get_white_down_cord(checker.x))

        if checker.color == (0, 0, 0):
            self.add_color_checker(checker, get_black_up_cord(checker.x), get_black_down_cord(checker.x))

    def add_color_checker(self, checker, up_cords, down_cords):
        if checker.x < 12:
            self.board[up_cords].stack.append(checker)
        elif 12 <= checker.x < 24:
            self.board[down_cords].stack.append(checker)
        else:
            raise ValueError

def convert_white_x_to_board_x(white_x):
    if white_x < 12:
        return get_white_up_cord(white_x)
    return get_white_down_cord(white_x)

def convert_black_x_to_board_x(black_x):
    if black_x < 12:
        return get_black_up_cord(black_x)
    return get_black_down_cord(black_x)

def get_white_up_cord(x):
    return 11 - x

def get_white_down_cord(x):
    return x
def get_black_up_cord(x):
    return x + 12

def get_black_down_cord(x):
    return 23 - x
