from collections import deque

import pygame

from Coordinates import Coordinates
from Player import Player

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

    def draw_backgammon_board(board, player1: Player, player2, mouse_x, mouse_y):
        screen.fill(BEIGE)
        black_mouse_x, white_mouse_x = Screen.converte_coords(mouse_x, mouse_y,
                                                              player1)

        def draw_brown_triangles():
            color = DARK_BROWN if i % 2 == 0 else BROWN

            x_point = board_margin + i * point_width
            y_point = board_margin

            Screen.draw_point(x_point, y_point, 'down', color)
            Screen.draw_point(x_point, height - y_point, 'up', color)

        for i in range(12):
            draw_brown_triangles()

        if player1.move_flag:
            Screen.draw_green_triangle_for_player(
                get_up_cord=Coordinates.get_white_up_cord,
                get_down_cord=Coordinates.get_white_down_cord,
                mouse_x=white_mouse_x,
                convert_x_to_board_x=Coordinates.convert_white_x_to_board_x,
                player=player1,
                a1=0, b1=12, direction1='down',
                a2=12, b2=24, direction2='up',
                func=lambda x: -x - 1,
                board=board
            )
        if player2.move_flag:
            Screen.draw_green_triangle_for_player(
                get_up_cord=Coordinates.get_black_up_cord,
                get_down_cord=Coordinates.get_black_down_cord,
                mouse_x=black_mouse_x,
                convert_x_to_board_x=Coordinates.convert_black_x_to_board_x,
                player=player2,
                a1=12, b1=24, direction1='up',
                a2=0, b2=12, direction2='down',
                func=lambda x: Coordinates.get_black_down_cord(x),
                board=board
            )

        Screen.draw_lines()
        Screen.draw_checkers(board.board)

        if board.flag_keep:
            if player1.move_flag:
                Screen.draw_checker(mouse_x, mouse_y, WHITE)
            else:
                Screen.draw_checker(mouse_x, mouse_y, BLACK)
        Screen.draw_dice_numbers(player1, player2)
        pygame.display.flip()

    @staticmethod
    def draw_dice_numbers(player1, player2, size=40):
        """Рисует маленькие белые квадраты с цифрами в виде точек, как на игровом кубике."""

        center_y = height // 2
        if player1.move_flag:
            center_x = width - width // 3
        else:
            center_x = width // 3
        # Координаты квадратов
        dice_positions = [
            (center_x - size - 10, center_y - size // 2),  # Левый квадрат
            (center_x + 10, center_y - size // 2)  # Правый квадрат
        ]

        for idx, (x, y) in enumerate(dice_positions):
            pygame.draw.rect(screen, WHITE,
                             (x, y, size, size))  # Рисуем квадрат
            pygame.draw.rect(screen, BLACK, (x, y, size, size),
                             2)  # Черная рамка

            # Определяем число и точки
            if player1.move_flag:
                number = player1.dice_numbers[idx]  # Числа от 1 до 2 (или другие, если нужно)
            else:
                number = player2.dice_numbers[idx]
            Screen.draw_dice_dots(x, y, size, number)

    @staticmethod
    def draw_dice_dots(x, y, size, number):
        # Центр квадрата
        cx, cy = x + size // 2, y + size // 2
        radius = size // 10  # Радиус точек

        # Позиции точек на кубике
        dot_positions = {
            1: [(cx, cy)],  # Одна точка в центре
            2: [(cx - size // 4, cy - size // 4),
                (cx + size // 4, cy + size // 4)],
            3: [(cx - size // 4, cy - size // 4), (cx, cy),
                (cx + size // 4, cy + size // 4)],
            4: [(cx - size // 4, cy - size // 4),
                (cx + size // 4, cy - size // 4),
                (cx - size // 4, cy + size // 4),
                (cx + size // 4, cy + size // 4)],
            5: [(cx - size // 4, cy - size // 4),
                (cx + size // 4, cy - size // 4),
                (cx - size // 4, cy + size // 4),
                (cx + size // 4, cy + size // 4),
                (cx, cy)],
            6: [(cx - size // 4, cy - size // 4),
                (cx + size // 4, cy - size // 4),
                (cx - size // 4, cy + size // 4),
                (cx + size // 4, cy + size // 4),
                (cx - size // 4, cy), (cx + size // 4, cy)],
        }

        # Рисуем точки
        for dot in dot_positions.get(number, []):
            pygame.draw.circle(screen, BLACK, dot, radius)

    @staticmethod
    def converte_coords(mouse_x, mouse_y, player):

        white_mouse_x = -1
        black_mouse_x = -1
        if board_margin < mouse_x < board_margin + 12 * point_width and board_margin < mouse_y < height - board_margin:
            if board_margin < mouse_y and mouse_y >= (
                    height - board_margin) / 2:
                white_mouse_x = Coordinates.get_white_up_cord(
                    (board_margin - mouse_x) // point_width)
                black_mouse_x = (mouse_x - board_margin) // point_width

            if board_margin < mouse_y < (height - board_margin) / 2:
                white_mouse_x = Coordinates.get_white_up_cord(
                    (mouse_x - board_margin) // point_width)
                black_mouse_x = Coordinates.get_black_down_cord(
                    (-board_margin + mouse_x) // point_width)
        return black_mouse_x, white_mouse_x

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

    @staticmethod
    def draw_green_triangle_for_player(get_up_cord, get_down_cord, mouse_x,
                                       convert_x_to_board_x, player, a1, b1,
                                       direction1, a2, b2, direction2, func,
                                       board):
        opponent_color = BLACK if player.color == WHITE else WHITE

        if not hasattr(board, 'stored_points'):
            board.stored_points = deque(maxlen=2)

        if board.flag_keep:
            for point in board.stored_points:
                black_x, white_x = Screen.converte_coords(point['x'], point['y'], player)
                if point['direction'] == 'down':
                    black_x, white_x = Screen.converte_coords(point['x']+(point_width/2), point['y']+(point_width/2), player)
                else:
                    black_x, white_x = Screen.converte_coords(point['x'] + (point_width / 2),
                                                              point['y'] - (point_width / 2), player)
                white_x = int(white_x)
                black_x = int(black_x)
                #white_x += 1
                #print(Coordinates.convert_black_x_to_board_x(black_x))
                #print(mouse_x, mouse_y)
                #print(f"coord: {Coordinates.convert_white_x_to_board_x(point['x'] + dice_num)}")
                #print(point['x'])

                if board.board[Coordinates.convert_white_x_to_board_x(white_x)].is_active and player.color == WHITE:
                    #print()
                    Screen.draw_point(point['x'], point['y'], point['direction'], (0, 255, 0))
                    #print()
                    #board.board[Coordinates.convert_black_x_to_board_x(black_x + dice_num)].is_active):

                    #print(f"dfdfdf{point['x']}")
                if board.board[Coordinates.convert_black_x_to_board_x(black_x)].is_active and player.color == BLACK:
                    Screen.draw_point(point['x'], point['y'], point['direction'], (0, 255, 0))

            return

        down_cord = get_down_cord(mouse_x)
        up_cord = get_up_cord(mouse_x)

        for dice_num in player.remaining_moves:

            if player.color == WHITE:
                z = up_cord - dice_num
            else:
                z = down_cord - dice_num

            cell_x = convert_x_to_board_x(mouse_x + dice_num)
            #if cell_x > 23:
            #    cell_x = 23
            # if 0 <= cell_x < len(board.board) and not board.board[cell_x].is_active:
            #    if len(board.stored_points) > 0:
            #        board.stored_points.popleft()
            y_point = board_margin

            if a1 <= cell_x < b1 and board.board[
                up_cord].color == player.color:
                direction = direction1
                if player.color == BLACK:
                    z = func(z)
                    y_point = -y_point + height
            elif (a2 <= cell_x < b2 and
                  ((mouse_x < 12 and board.board[
                      up_cord].color == player.color) or
                   (mouse_x >= 12 and board.board[
                       down_cord].color == player.color))):
                direction = direction2
                if player.color == WHITE:
                    z = func(z)
                    y_point = -y_point + height

            else:
                #print(cell_x)
                # if player.color == WHITE:
                #     if cell_x >= len(board.board):
                #         if len(board.stored_points) > 0:
                #             board.stored_points.popleft()
                #     if cell_x < len(board.board) and board.board[cell_x].color == BLACK:
                #         if len(board.stored_points) > 0:
                #             board.stored_points.popleft()
                # else:
                #     if cell_x < 0:
                #         if len(board.stored_points) > 0:
                #             board.stored_points.popleft()
                #     if cell_x < len(board.board) and board.board[cell_x].color == WHITE:
                #         if len(board.stored_points) > 0:
                #             board.stored_points.popleft()

                continue

            if board.board[cell_x].color == opponent_color:
                continue



            #if cell_x == 23:
            #    z = 12


            draw_x = board_margin + z * point_width
            # if 0 <= cell_x < len(board.board) and not board.board[cell_x].is_active:
            # return
            # print(draw_x)


            Screen.draw_point(draw_x, y_point, direction, (0, 255, 0))

            #for i in range(len(board.board)):
            #    if board.board[i].is_active:

            black_x, white_x = Screen.converte_coords(draw_x, y_point, player)

            if board.board[cell_x].is_active:
                board.stored_points.append({
                    'x': draw_x,
                    'y': y_point,
                    'direction': direction
                })
            # else:
            #     board.stored_points.remove({
            #         'x': draw_x,
            #         'y': y_point,
            #         'direction': direction
            #     })

