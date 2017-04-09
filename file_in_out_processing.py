def read_input(file_name):
    f_input = open(file_name, 'r')
    new_move = f_input.readline()
    moves = []
    while (new_move is not None) and len(new_move) > 0:
        lst = [int(e) for e in new_move.split(",")]
        if is_a_not_valid_line(lst):
            return None
        moves.append(lst)
        new_move = f_input.readline()
    return moves


def is_a_not_valid_line(lst):
    if len(lst) != 4:
        return True
    for e in lst:
        if e < 0 or e > 7:
            return True
    return False


def get_illegal_move_string(move, line_number): #TODO - move to "input processing.py" and call the file in_out_processing.py
    return "line : " + "%d" % line_number + " illegal move: " + "%s" % str(move)