import global_vars
from Utils import *
from Enums import *


def understand_move(move):
    if (not is_the_move_is_in_boundaries(move)) or (not is_the_target_space_empty(move)):
        return MOVE_STATUS.WRONG_MOVE
    if not is_the_move_starts_with_the_right_piece(move):
        return MOVE_STATUS.WRONG_MOVE
    if is_there_any_possible_eating_move():
        if is_the_move_a_valid_eating_move(move):
            return MOVE_STATUS.EATING_MOVE
        else:
            return MOVE_STATUS.WRONG_MOVE
    else:
        if is_the_move_a_valid_simple_move(move):
            return MOVE_STATUS.NORMAL_MOVE
    return MOVE_STATUS.WRONG_MOVE


def is_the_move_is_in_boundaries(move):
    start_column, start_row, next_column, next_row = move[0], move[1], move[2], move[3]
    if not is_in_boundaries(start_row, start_row):
        return False
    if not is_in_boundaries(next_row, next_column):
        return False
    return True


def is_the_move_a_valid_eating_move(move):
    start_column, start_row, next_column, next_row = move[0], move[1], move[2], move[3]
    if not (next_row - start_row == 2 * global_vars.whos_turn.value):
        return False
    if next_column - start_column == 2:
        return is_eating_possible_for_direction(start_row, start_column, left_or_right_direction.RIGHT)
    if next_column - start_column == -2:
        return is_eating_possible_for_direction(start_row, start_column, left_or_right_direction.LEFT)
    return False


def is_the_move_a_valid_simple_move(move):
    start_column, start_row, next_column, next_row = move[0], move[1], move[2], move[3]
    return (1 == abs(next_column - start_column)) and ((next_row - start_row) == global_vars.whos_turn.value)


def is_the_target_space_empty(move):
    next_column, next_row = move[2], move[3]
    return CELL_STATE.EMPTY == global_vars.board[next_row][next_column]


def is_the_move_starts_with_the_right_piece(move):
    start_column, start_row = move[0], move[1]
    return global_vars.whos_turn == global_vars.board[start_row][start_column]
