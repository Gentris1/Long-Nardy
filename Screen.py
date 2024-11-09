import pygame

from Board import get_white_up_cord, get_white_down_cord, get_black_down_cord, \
    get_black_up_cord, convert_white_x_to_board_x, convert_black_x_to_board_x
from Cell import Cell

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Backgammon Board")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BEIGE = (245, 222, 179)
BROWN = (139, 69, 19)
DARK_BROWN = (160, 82, 45)

point_width = width // 14
point_height = height // 3

board_margin = point_width


class Screen:
    @staticmethod
    def draw_point(x, y, direction, color):
        if direction == 'down':
            pygame.draw.polygon(screen, color,
                                [(x, y),
                                 (x + point_width // 2, y + point_height),
                                 (x + point_width, y)])
        else:
            pygame.draw.polygon(screen, color,
                                [(x, y),
                                 (x + point_width // 2, y - point_height),
                                 (x + point_width, y)])
        pygame.draw.polygon(screen, BLACK, [(x, y), (
            x + point_width // 2,
            y + point_height) if direction == 'down' else (
            x + point_width // 2, y - point_height), (x + point_width, y)], 2)

    @staticmethod
    def draw_checker(x, y, color):
        pygame.draw.circle(screen, color, (x, y), point_width // 2 - 5)

        if color == BLACK:
            pygame.draw.circle(screen, WHITE, (x, y), point_width // 2 - 5, 2)
        else:
            pygame.draw.circle(screen, BLACK, (x, y), point_width // 2 - 5, 2)

    @staticmethod
    def draw_checkers_on_point(x, y, direction, color, count):
        checker_radius = point_width // 2 - 5
        available_height = point_height - checker_radius

        if 1 < count < 6:
            checker_spacing = available_height / (count - (-4 + count))  # 5

        elif count >= 6:
            checker_spacing = available_height / (count - 1)
        else:
            checker_spacing = 0

        for i in range(count):
            if direction == 'up':
                Screen.draw_checker(x, y - i * checker_spacing, color)
            else:
                Screen.draw_checker(x, y + i * checker_spacing, color)

    @staticmethod
    # Main loop
    def draw_backgammon_board(board: list[Cell], player1, player2):
        screen.fill(BEIGE)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        white_mouse_x = -1
        black_mouse_x = -1
        if board_margin < mouse_x < board_margin + 12 * point_width and board_margin < mouse_y < height - board_margin:
            if board_margin < mouse_y and mouse_y >= (
                    height - board_margin) / 2:
                if len(player1.dice_numbers)>0:
                    white_mouse_x = get_white_up_cord(
                        (board_margin - mouse_x) // point_width)
                else:
                    black_mouse_x = (mouse_x - board_margin) // point_width

            if board_margin < mouse_y < (height - board_margin) / 2:
                if len(player1.dice_numbers)>0:
                    white_mouse_x = get_white_up_cord(
                        (mouse_x - board_margin) // point_width)
                else:
                    black_mouse_x = get_black_down_cord(
                        (-board_margin + mouse_x) // point_width)

        def draw_brown_triangles():
            color = DARK_BROWN if i % 2 == 0 else BROWN

            x_point = board_margin + i * point_width
            y_point = board_margin

            Screen.draw_point(x_point, y_point, 'down', color)
            Screen.draw_point(x_point, height - y_point, 'up', color)

        def draw_green_triangle_for_player(get_up_cord, get_down_cord, mouse_x,
                                     convert_x_to_board_x, player, a1, b1,
                                     direction1, a2, b2, direction2, func):
            opponent_color = BLACK if player.color == WHITE else WHITE
            for dice_number in player.dice_numbers:
                down_cord = get_down_cord(mouse_x)
                up_cord = get_up_cord(mouse_x)

                z = up_cord - dice_number if player.color == WHITE else down_cord - dice_number

                cell_x = convert_x_to_board_x(mouse_x + dice_number)
                y_point = board_margin

                if a1 <= cell_x < b1 and board[up_cord].color == player.color:
                    direction = direction1
                    if player.color == BLACK:
                        z = func(z)
                        y_point = -y_point + height
                elif (a2 <= cell_x < b2 and
                      (mouse_x < 12 and board[up_cord].color == player.color or
                       mouse_x >= 12 and board[
                           down_cord].color == player.color)):
                    direction = direction2
                    if player.color == WHITE:
                        z = func(z)
                        y_point = -y_point + height
                else:
                    continue

                if board[cell_x].color == opponent_color:
                    continue

                Screen.draw_point(board_margin + z * point_width, y_point,
                                  direction, (0, 255, 0))

        for i in range(12):
            draw_brown_triangles()

            draw_green_triangle_for_player(
                get_up_cord=get_white_up_cord,
                get_down_cord=get_white_down_cord,
                mouse_x=white_mouse_x,
                convert_x_to_board_x=convert_white_x_to_board_x,
                player=player1,
                a1=0, b1=12, direction1='down',
                a2=12, b2=24, direction2='up',
                func=lambda x: -x - 1
            )

            draw_green_triangle_for_player(
                get_up_cord=get_black_up_cord,
                get_down_cord=get_black_down_cord,
                mouse_x=black_mouse_x,
                convert_x_to_board_x=convert_black_x_to_board_x,
                player=player2,
                a1=12, b1=24, direction1='up',
                a2=0, b2=12, direction2='down',
                func=lambda x: get_black_down_cord(x)
            )

        Screen.draw_lines()
        Screen.draw_checkers(board)

        pygame.display.flip()

    @staticmethod
    def draw_lines():
        pygame.draw.line(screen, BLACK, (width // 2, board_margin),
                         (width // 2, height - board_margin), 4)
        pygame.draw.line(screen, BLACK, (board_margin, board_margin),
                         (board_margin, height - board_margin), 4)
        pygame.draw.line(screen, BLACK, (width - board_margin, board_margin),
                         (width - board_margin, height - board_margin), 4)

    @staticmethod
    def draw_checkers(board):
        checker_radius = point_width // 2 - 5
        for i in range(len(board)):
            if len(board[i].stack) > 0:
                if i < 12:
                    Screen.draw_checkers_on_point(
                        board_margin + i * point_width + point_width // 2,
                        board_margin + checker_radius, 'down',
                        board[i].stack[0].color,
                        len(board[i].stack))

                if 12 <= i < 24:
                    Screen.draw_checkers_on_point(
                        board_margin * (i - 11) + point_width // 2,
                        height - board_margin - checker_radius,
                        'up',
                        board[i].stack[0].color,
                        len(board[i].stack))
