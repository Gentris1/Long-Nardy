from Cell import Cell
from Checker import Checker
from Coordinates import Coordinates
from Player import Player
from Screen import Screen

main_board_mouse_x = 0

class Board:
    board: list[Cell]
    flag_keep: bool
    checker_keep: Checker
    home: list[Checker]
    white_total_checkers = 0
    black_total_checkers = 0
    is_ready_black: bool = False
    is_ready_white: bool = False

    def __init__(self):
        self.board = [Cell(x) for x in range(24)]
        self.flag_keep = False
        self.home = []

        #self.white_total_checkers =


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
        if player.color == (255, 255, 255):
            board_coord = Coordinates.convert_white_x_to_board_x(white_mouse_x)
        else:
            board_coord = Coordinates.convert_black_x_to_board_x(black_mouse_x)

        temp = set()
        for i in range(len(self.board)):
            if i == board_coord and len(self.board[board_coord].stack) > 0 and not self.flag_keep:
                for j in self.board[board_coord].possible_cells_to_move:
                    if j == len(self.board):
                        continue
                    #if 0 <= j < len(self.board[board_coord].possible_cells_to_move):
                        #print(j)

                    self.board[j].is_active = True
                    temp.add(j)
                    #else:
                    #    self.move_to_home(player, j)
            if i not in temp and not self.flag_keep:
                self.board[i].is_active = False

        # for i in range(len(self.board)):
        #     if self.board[i].is_active:
        #         print(i)
    def count_total_checkers(self):
        self.white_total_checkers = 0
        self.black_total_checkers = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i].stack)):
                if self.board[i].stack[j].color == (255, 255, 255):
                    self.white_total_checkers += 1
                else:
                    self.black_total_checkers += 1

        if self.flag_keep:
            if self.checker_keep.color == (255, 255, 255):
                self.white_total_checkers += 1
            else:
                self.black_total_checkers += 1
        #print(self.black_total_checkers)
    def get_ready_to_home(self):
        count = 0
        for i in range(6):
            if self.board[i].color == (0, 0, 0):
                count += len(self.board[i].stack)
        if count == self.black_total_checkers:
            self.is_ready_black = True

        count = 0
        for i in range(18, len(self.board)):
            if self.board[i].color == (255, 255, 255):
                count += len(self.board[i].stack)
        if count == self.white_total_checkers:
            self.is_ready_white = True

    def move_to_home(self, player, mouse_x, mouse_y):
        #print(cell_x)
        #print(self.white_total_checkers)
        #print(self.black_total_checkers)

        width, height = 800, 600
        point_width = width // 14
        board_margin = point_width

        count = 0
        black_mouse_x, white_mouse_x = Screen.converte_coords(mouse_x, mouse_y, player)
        if player.color == (255, 255, 255):
            if self.flag_keep and self.is_ready_white:
                for i in range(len(self.board)):
                    #print(board_margin, mouse_x)
                    if 24 in self.board[i].possible_cells_to_move and mouse_x > width - board_margin:
                        #print("append")
                        self.home.append(self.checker_keep)
                        for i in range(len(self.board)):
                            if len(self.board[i].stack) > 0:
                                self.board[i].possible_cells_to_move = set()
                        dice_number = abs(self.checker_keep.x - 24)
                        print(dice_number)
                        if len(player.remaining_moves) > 0 and max(player.remaining_moves) >= dice_number:
                            player.remaining_moves.remove(max(player.remaining_moves))
                        self.flag_keep = False

                #self.home.append(self.checker_keep)
                #self.flag_keep = False
                #self.checker_keep
        else:
            #count = 1

            if self.flag_keep and self.is_ready_black:
                #print(self.black_total_checkers)
                for i in range(len(self.board)):
                    #print(board_margin, mouse_x)
                    #print(self.board[i].possible_cells_to_move)
                    if 24 in self.board[i].possible_cells_to_move and mouse_x < board_margin:
                        #print("append")
                        self.home.append(self.checker_keep)
                        for i in range(len(self.board)):
                            if len(self.board[i].stack) > 0:
                                self.board[i].possible_cells_to_move = set()
                        #print(player.remaining_moves)
                        #board_mouse_x = Coordinates.convert_black_x_to_board_x(black_mouse_x)
                        dice_number = abs(self.checker_keep.x - 24)

                        if len(player.remaining_moves) > 0 and max(player.remaining_moves) >= dice_number:
                            player.remaining_moves.remove(max(player.remaining_moves))
                            self.flag_keep = False

        # if 18 <= self.checker_keep.x < 24:
        #     for dice_number in player.remaining_moves:
        #         print(self.checker_keep.x + dice_number)

    def move_checker(self, player: Player, mouse_x, mouse_y):
        global main_board_mouse_x
        black_mouse_x, white_mouse_x = Screen.converte_coords(mouse_x, mouse_y, player)
        if player.color == (255, 255, 255):
            board_mouse_x = Coordinates.convert_white_x_to_board_x(white_mouse_x)
        else:
            board_mouse_x = Coordinates.convert_black_x_to_board_x(black_mouse_x)

        board_stack = self.board[board_mouse_x].stack

        if self.flag_keep:
            for i in range(len(self.board)):
                if (board_mouse_x == i and self.board[i].is_active and
                        (len(board_stack) > 0 and board_stack[0].color == player.color or len(board_stack) == 0)):
                    if player.color == (255, 255, 255):
                        self.checker_keep.x = Coordinates.convert_board_x_to_white_x(i)
                        dice_number = abs(main_board_mouse_x - white_mouse_x)
                    else:
                        self.checker_keep.x = Coordinates.convert_board_x_to_black_x(i)
                        dice_number = abs(main_board_mouse_x - black_mouse_x)

                    board_stack.append(self.checker_keep)

                    for i in range(len(self.board)):
                        if len(self.board[i].stack) > 0:
                            self.board[i].possible_cells_to_move = set()

                    if dice_number > 0:
                        if dice_number in player.remaining_moves:
                            player.remaining_moves.remove(dice_number)

                    self.flag_keep = False
        elif len(board_stack) > 0 and board_stack[0].color == player.color:
            if player.color == (255, 255, 255):
                main_board_mouse_x = white_mouse_x
            else:
                main_board_mouse_x = black_mouse_x
            self.checker_keep = board_stack.pop()
            self.board[board_mouse_x].is_active = True
            self.flag_keep = True

    def get_checker_possible_moves(self, player):
        for i in range(len(self.board)):
            if len(self.board[i].stack) > 0 and self.board[i].stack[0].color == player.color:
                for j in range(len(self.board[i].stack)):
                    checker_x = self.board[i].stack[j].x
                    for dice_number in player.remaining_moves:
                        if player.color == (255, 255, 255):
                            board_checker_x = Coordinates.convert_white_x_to_board_x(checker_x + dice_number)
                        else:
                            board_checker_x = Coordinates.convert_black_x_to_board_x(checker_x + dice_number)

                        if (0 <= board_checker_x < len(self.board) and
                                (self.board[i].stack[0].color == player.color) and
                                (len(self.board[board_checker_x].stack) == 0 or
                                 len(self.board[board_checker_x].stack) > 0 and self.board[i].stack[0].color ==
                                 self.board[board_checker_x].stack[0].color)):

                            if len(self.board[i].possible_cells_to_move) < 2:
                                self.board[i].possible_cells_to_move.add(board_checker_x)

                        if board_checker_x > len(self.board) or board_checker_x < 0:
                            self.board[i].possible_cells_to_move.add(24)
                        #print(self.board[i].possible_cells_to_move)
