import pygame

from Board import get_white_up_cord, get_white_down_cord, get_black_down_cord, \
    get_black_up_cord

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
    def draw_backgammon_board(board, player1, player2):
        screen.fill(BEIGE)
        mouse_x = -1
        if len(player1.dice_numbers) > 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if board_margin < mouse_x < board_margin + 12 * point_width and board_margin < mouse_y < height - board_margin:
                if board_margin < mouse_y < (height - board_margin) / 2:
                    mouse_x = get_white_up_cord(
                        (mouse_x - board_margin) // point_width)
                    print(mouse_x, mouse_y)
                if board_margin < mouse_y and mouse_y >= (
                        height - board_margin) / 2:
                    mouse_x = get_white_up_cord(
                        (board_margin - mouse_x) // point_width)
                    print(mouse_x, mouse_y)

        if player2.move_flag:
            pass

        print(mouse_x)
        for i in range(12):
            color = DARK_BROWN if i % 2 == 0 else BROWN

            Screen.draw_point(board_margin + i * point_width, board_margin,
                              'down',
                              color)
            Screen.draw_point(board_margin + i * point_width,
                              height - board_margin,
                              'up',
                              color)

            for dice_number in player1.dice_numbers:
                white_down_cord = get_white_down_cord(mouse_x)
                white_up_cord = get_white_up_cord(mouse_x)

                z = white_up_cord - dice_number
                y_point = board_margin

                if mouse_x + dice_number < 12 and len(board[white_up_cord].stack) > 0:
                        direction = 'down'

                elif 12 <= mouse_x + dice_number < 24 and (mouse_x < 12 and len(board[white_up_cord].stack) > 0 or mouse_x >= 12 and len(board[white_down_cord].stack) > 0):
                        direction = 'up'
                        z = -z - 1
                        y_point = -y_point + height
                else:
                    continue
                board[white_down_cord].accomodation = True
                Screen.draw_point(
                    board_margin + z * point_width,
                    y_point,
                    direction,
                    (0, 255, 0))

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
