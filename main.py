import data_model
import constant
from game_board import GameBoard

if __name__ == '__main__':
    board = GameBoard()
    data_model.print_board(board)
    for current_move in range(0, constant.MAX_NUM_MOVES):
        move = data_model.get_next_move()
        board.color_board_move(move)
        data_model.print_board(board)
        if board.check_winner():
            print("you won!!")
            break
    if current_move > constant.MAX_NUM_MOVES - 1:
        print("you lose :(")
