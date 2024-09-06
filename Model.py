from typing import final


class Model:
    def __init__(self):
        self.num_pegs_left = 0
        self.game_board = [[0 for c in range(5)] for r in range(5)]
        self.fill_board()
        print(self.game_board)

    def fill_board(self):
        for r in range(0, 5):
            for c in range(0, r+1):
                self.game_board[r][c] = 1

    def is_inbounds(self, row, col):
        if row > 4 or col > 4 or row < 0 or col < 0:
            return False

        elif col > row:
            return False

        else:
            return True

    def check_valid_move(self, peg_row, peg_column, final_row, final_col):
        if self.is_inbounds(final_row, final_col):
            print("inbounds")
        else: print ("outofbounds")



if __name__ == "__main__":
    Game = Model()

