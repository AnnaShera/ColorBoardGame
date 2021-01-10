import random
import constant


class GameBoard:
    """
    The game board
    matrix - representation of the board after every user move
    """
    def __init__(self):
        self.num_of_rows = constant.NUM_OF_ROWS
        self.num_of_columns = constant.NUM_OF_COLUMNS
        self.num_of_moves = 0
        self.matrix = [[0 for row in range(self.num_of_rows + 1)] for col in range(self.num_of_columns + 1)]
        for row in range(0, self.num_of_rows):
            for col in range(0, self.num_of_columns):
                rand = random.randrange(1, 4)
                self.matrix[row][col] = rand

    def color_board_move(self, new_color):
        """
        function makes a move on the board - the new color chosen spreads to all the neighbors of the starting cell
        which have the same color as it does, and increases the number of moves
        :param new_color: color chosen by the user
        """
        self.num_of_moves += 1
        previous_color = self.matrix[0][0]
        if previous_color == new_color:
            return
        row = 0
        col = 0
        if self.matrix[row][col] == previous_color:
            self.__color_board_internal(row, col, previous_color, new_color)

    def __color_board_internal(self, row, col, previous_color, new_color):
        """
        function colors the board by spreading to the neighbors in dfs traversal
        """
        if row < 0 or row > self.num_of_rows or col < 0 or col > self.num_of_columns or self.matrix[row][col] != previous_color:
            return
        self.matrix[row][col] = new_color
        self.__color_board_internal(row + 1, col, previous_color, new_color)
        self.__color_board_internal(row - 1, col, previous_color, new_color)
        self.__color_board_internal(row, col + 1, previous_color, new_color)
        self.__color_board_internal(row, col - 1, previous_color, new_color)
        return

    def check_winner(self):
        """
        function checks if all the board is colored in the same color
        :return: True if winner False otherwise
        """
        color = self.matrix[0][0]
        for row in range(0, self.num_of_rows):
            for col in range(0, self.num_of_columns):
                if self.matrix[row][col] != color:
                    return False
        return True
