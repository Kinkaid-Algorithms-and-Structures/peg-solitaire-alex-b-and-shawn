from typing import final


class Model:
    def __init__(self):
        self.num_pegs_left = 0
        self.direction = 0
        self.game_board = [[0 for c in range(5)] for r in range(5)]
        self.fill_board()
        print(self.game_board[0])
        print(self.game_board[1])
        print(self.game_board[2])
        print(self.game_board[3])
        print(self.game_board[4])
        sr = int(input("sr?"))
        sc = int(input("sc?"))
        fr = int(input("fr?"))
        fc = int(input("fc?"))
        self.check_valid_move(sr, sc, fr, fc)
        print(self.direction)

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
        if self.is_inbounds(peg_row, peg_column) and self.is_inbounds(final_row, final_col):
            print("inbounds")
        else:
            print("outofbounds")

        if peg_row > final_row:
            if peg_column > final_col:
                self.direction = 1
            elif peg_column == final_col:
                self.direction = 2
            elif peg_column < final_col:
                self.direction = 3
        elif peg_row < final_row:
            if peg_column < final_col:
                self.direction = 5
            elif peg_column == final_col:
                self.direction = 6
            elif peg_column > final_col:
                self.direction = 7
        elif peg_column < final_col:
                self.direction = 4
        else:
            self.direction = 8

if __name__ == "__main__":
    Game = Model()

