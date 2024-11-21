from Cell import Cell
from Checker import Checker
from Coordinates import Coordinates
from Player import Player
from Screen import Screen


class Board:
    board: list[Cell]
    flag_keep: bool
    checker_keep: Checker

    def __init__(self):
        self.board = [Cell(x) for x in range(24)]
        self.flag_keep = False

    def add_checker(self, checker):
        if checker.color == (255, 255, 255):
            self.add_color_checker(checker,
                                   Coordinates.get_white_up_cord(checker.x),
                                   Coordinates.get_white_down_cord(checker.x))

        if checker.color == (0, 0, 0):
            self.add_color_checker(checker,
                                   Coordinates.get_black_up_cord(checker.x),
                                   Coordinates.get_black_down_cord(checker.x))

    def add_color_checker(self, checker, up_cords, down_cords):
        if checker.x < 12:
            self.board[up_cords].stack.append(checker)
        elif 12 <= checker.x < 24:
            self.board[down_cords].stack.append(checker)
        else:
            raise ValueError

    def activate_cells(self, mouse_x: int, mouse_y: int, player: Player):
        black_mouse_x, white_mouse_x = Screen.converte_coords(mouse_x, mouse_y,
                                                              player)
        for i in range(len(self.board)):
            if not self.flag_keep:
                for dice_number in player.dice_numbers:
                    if Coordinates.convert_white_x_to_board_x(white_mouse_x + dice_number) < len(self.board):
                        self.board[Coordinates.convert_white_x_to_board_x(white_mouse_x + dice_number)].is_active = True

                if (i != Coordinates.convert_white_x_to_board_x(white_mouse_x + player.dice_numbers[0])
                        and i != Coordinates.convert_white_x_to_board_x(white_mouse_x + player.dice_numbers[1])):
                    self.board[i].is_active = False

        for i in range(0, len(self.board)):
            if self.board[i].is_active:
                print(i)

    @staticmethod
    def move_checker(board, player1, player2, mouse_x, mouse_y):
        black_mouse_x, white_mouse_x = Screen.converte_coords(mouse_x, mouse_y,
                                                              player1)
        board_white_mouse_x = Coordinates.convert_white_x_to_board_x(
            white_mouse_x)

        if board.flag_keep:
            for i in range(len(board.board)):
                if board_white_mouse_x == i and board.board[i].is_active:
                    board.board[board_white_mouse_x].stack.append(
                        board.checker_keep)
                    for i in range(len(board.board)):
                        board.board[i].is_active = False

                    board.flag_keep = False
        elif board.board[board_white_mouse_x].stack:
            board.checker_keep = board.board[board_white_mouse_x].stack.pop()
            board.board[board_white_mouse_x].is_active = True
            board.flag_keep = True
