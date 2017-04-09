import global_vars
from Enums import *


def get_initialized_board(rows=8, columns=8):
    global_vars.board = [[CELL_STATE.EMPTY for j in range(columns)] for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if (i + j) % 2:
                if i < 3:
                    global_vars.board[i][j] = CELL_STATE.WHITE
                elif ((rows - 3) <= i) and (i < rows):
                    global_vars.board[i][j] = CELL_STATE.BLACK
    return global_vars.board


def is_there_any_possible_move():
    for i in range(len(global_vars.board)):
        for j in range(len(global_vars.board[i])):
            if (global_vars.whos_turn.value == global_vars.board[i][j].value) and (
                    is_there_any_possible_move_for_piece(i, j)):
                return True
    return False


def is_there_any_possible_move_for_piece(row, column):
    return is_there_any_possible_eating_move_for_piece(row, column) or \
           is_there_any_possible_simple_move_for_piece(row, column)


def is_there_any_possible_eating_move():
    for i in range(len(global_vars.board)):
        for j in range(len(global_vars.board[i])):
            if (global_vars.whos_turn == global_vars.board[i][j]) and (
                    is_there_any_possible_eating_move_for_piece(i, j)):
                return True
    return False


def is_there_any_possible_eating_move_for_piece(start_row, start_column):
    if is_this_piece_is_at_the_2_last_rows(start_row):
        return False  # the piece is not able to move forward from this point the edge of the board

    for direction in left_or_right_direction:
        if is_eating_possible_for_direction(start_row, start_column, direction):
            return True
    return False


def is_this_piece_is_at_the_2_last_rows(start_row):
    expected_row = start_row + 2 * global_vars.whos_turn.value
    return len(global_vars.board) <= expected_row or 0 > expected_row


def is_in_boundaries(row, column):
    if 0 <= row < len(global_vars.board):
        if 0 <= column < len(global_vars.board):
            return True
    return False


def is_opponent_exists(row, column):
    assert (is_in_boundaries(row, column))
    if global_vars.board[row][column] == get_opponent():
        return True
    return False


def is_free_space_after_oponent(row, column):
    assert (is_in_boundaries(row, column))
    if global_vars.board[row][column] == CELL_STATE.EMPTY:
        return True
    return False


def is_eating_possible_for_direction(start_row, start_column, left_or_right):
    expected_column = start_column + 2 * left_or_right.value
    expected_row = start_row + 2 * global_vars.whos_turn.value
    if not is_in_boundaries(expected_row, expected_column):
        return False

    if (is_opponent_exists(start_row + global_vars.whos_turn.value, start_column + left_or_right.value) and
            (is_free_space_after_oponent(expected_row, expected_column))):
        return True
    return False


def is_there_any_possible_simple_move_for_piece(row, column):
    if is_in_boundaries(row + global_vars.whos_turn.value, column + 1):
        if global_vars.board[row + global_vars.whos_turn.value][column + 1] == CELL_STATE.EMPTY:
            return True
    if is_in_boundaries(row + global_vars.whos_turn.value, column - 1):
        if global_vars.board[row + global_vars.whos_turn.value][column - 1] == CELL_STATE.EMPTY:
            return True
    return False


def get_opponent():
    assert global_vars.whos_turn != CELL_STATE.EMPTY
    if global_vars.whos_turn == CELL_STATE.WHITE:
        return CELL_STATE.BLACK
    else:
        return CELL_STATE.WHITE


def get_who_won_according_to_the_balance():
    balance = 0
    for i in range(len(global_vars.board)):
        for j in range(len(global_vars.board[i])):
            balance += global_vars.board[i][j].value

    if 0 == balance:
        return game_result.TIE
    if balance > 0:
        return game_result.FIRST
    else:
        return game_result.SECOND
