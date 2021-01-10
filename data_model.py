from colored import bg, attr
import constant
import enum


class Colors(enum.Enum):
    """
    enum representation of the available colors
    """
    r = 1
    g = 2
    y = 3
    b = 4


def get_next_move():
    """
    function read char from user, will continue until a char between the valid options will be received
    :return: chars value representation
    """
    while True:
        char = input("Choose a char from the following colors red(r), green(g), yellow(y), blue(b):")
        if char not in Colors.member_names_:
            print(F"Error: {char} char is not supported")
            continue
        else:
            return Colors[char].value


def print_board(board):
    """
    :param board: The gaming board
    function prints the board representation and current move
    """
    for row in range(0, board.num_of_rows):
        for col in range(0, board.num_of_columns):
            print(F"{bg(board.matrix[row][col])}  {attr(0)}", end="")
        print("")
    print(F"{board.num_of_moves}/{constant.MAX_NUM_MOVES} moves")
