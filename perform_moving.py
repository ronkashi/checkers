import global_vars
from Enums import *
from Utils import *


def perform_move(move, move_result):
    assert (move_result != MOVE_STATUS.WRONG_MOVE)
    start_column, start_row, next_column, next_row = move[0], move[1], move[2], move[3]

    global_vars.board[next_row][next_column] = global_vars.board[start_row][start_column]
    global_vars.board[start_row][start_column] = CELL_STATE.EMPTY

    if MOVE_STATUS.NORMAL_MOVE == move_result:
        change_whos_turn()
    if MOVE_STATUS.EATING_MOVE == move_result:
        global_vars.board[(next_row + start_row) // 2][(next_column + start_column) // 2] = CELL_STATE.EMPTY
        if not is_there_any_possible_eating_move_for_piece(next_row, next_column):
            change_whos_turn()


def change_whos_turn():
    assert global_vars.whos_turn != CELL_STATE.EMPTY
    global_vars.whos_turn = get_opponent()
