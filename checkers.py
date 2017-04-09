import global_vars
from file_in_out_processing import read_input, get_illegal_move_string
from UnderstandMove import understand_move
from perform_moving import perform_move
from Enums import *
from Utils import *
from sys import argv


def run_game(moves):
    global_vars.board = get_initialized_board()
    for i in range(len(moves)):
        move_result = understand_move(moves[i])
        if MOVE_STATUS.WRONG_MOVE != move_result:
            perform_move(moves[i], move_result)
        else:
            return get_illegal_move_string(moves[i], i + 1)
    if is_there_any_possible_move():
        return "incomplete"
    return str(get_who_won_according_to_the_balance())


def main():
    moves = read_input(argv[1])
    if moves is None:
        print("Error: Bad input file")
        return -1

    result_str = run_game(moves)
    print(result_str)
    return 0


if __name__ == "__main__":
    main()

