class Coordinates:
    @staticmethod
    def get_white_up_cord(x):
        return 11 - x

    @staticmethod
    def convert_white_x_to_board_x(white_x):
        if white_x < 12:
            return Coordinates.get_white_up_cord(white_x)
        return Coordinates.get_white_down_cord(white_x)

    @staticmethod
    def convert_black_x_to_board_x(black_x):
        if black_x < 12:
            return Coordinates.get_black_up_cord(black_x)
        return Coordinates.get_black_down_cord(black_x)

    @staticmethod
    def get_white_down_cord(x):
        return x

    @staticmethod
    def get_black_up_cord(x):
        return x + 12

    @staticmethod
    def get_black_down_cord(x):
        return 23 - x