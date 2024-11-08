from typing import List, Any


class Cell:
    accommodation: bool
    x: object
    stack: list[Any]

    def __init__(self, x):
        self.stack = []
        self.x = x
        self.accommodation = False
