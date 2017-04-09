from enum import Enum


class CELL_STATE(Enum):
    EMPTY = 0
    WHITE = 1
    BLACK = -1


class MOVE_STATUS(Enum):
    WRONG_MOVE = 0
    NORMAL_MOVE = 1
    EATING_MOVE = 2


class game_result(Enum):
    TIE = 0
    FIRST = 1
    SECOND = 2
    ILLEGAL = 3


class left_or_right_direction(Enum):
    RIGHT = 1
    LEFT = -1
