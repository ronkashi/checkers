import global_var


def print_board(move):
    print("BOARD")
    print("Move is ", move)
    print("Turn is ", global_var.whos_turn)
    for i in range(len(global_var.board)):
        for j in range(len(global_var.board)):
            res = " . "
            if global_var.board[i][j].value == 1:
                res = " X "
            if global_var.board[i][j].value == -1:
                res = " V "
            print(res, end="")
        print(" ", end="")
        print(i)