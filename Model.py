from typing import final

class Model:
    def __init__(self):
        self.num_pegs_left = 14
        self.x_direction = 0
        self.y_direction = 0
        self.game_board = [[0 for c in range(5)] for r in range(5)]
        self.fill_board()

# temporary — sets 0, 0 to be open, controller should change this to allow user to pick open peg
        # self.game_board[0][0] = 0

# temporary — viewer should draw board
        # self.draw_board()

# temporary — game controls for testing
        # while self.num_pegs_left > 0:
        #     self.x_direction = 0
        #     self.y_direction = 0
        #     pr = int(input("pr"))
        #     pc = int(input("pc"))
        #     fr = int(input("fr"))
        #     fc = int(input("fc"))
        #     self.make_move(pr, pc, fr, fc)
        #     self.draw_board()

    def fill_board(self):
        for r in range(0, 5):
            for c in range(0, r+1):
                self.game_board[r][c] = 1

# temporary — viewer should draw board
    # def draw_board(self):
    #     for r in range(0, 5):
    #         for c in range(0, r+1):
    #             print(self.game_board[r][c], end ="")
    #         print()

    def is_inbounds(self, row, col):
        if row > 4 or col > 4 or row < 0 or col < 0:
            return False

        elif col > row:
            return False

        else:
            return True

    def delete_peg(self, row, col):
        self.game_board[row][col] = 0

    def get_direction(self, peg_row, peg_col, final_row, final_col):
        self.x_direction = int((final_row-peg_row)/2)
        self.y_direction = int((final_col - peg_col)/2)

    def check_valid_move(self, peg_row, peg_col, final_row, final_col):
        if self.is_inbounds(peg_row, peg_col) and self.is_inbounds(final_row, final_col) and self.game_board[peg_row][peg_col] == 1 and self.game_board[peg_row+self.x_direction][peg_col+self.y_direction] == 1 and self.game_board[final_row][final_col] == 0:
            return True
        else:
            return False

    def make_move(self, peg_row, peg_col, final_row, final_col):
        self.get_direction(peg_row, peg_col, final_row, final_col)
        if self.check_valid_move(peg_row, peg_col, final_row, final_col):
            self.game_board[peg_row][peg_col] = 0
            self.game_board[peg_row+self.x_direction][peg_col+self.y_direction] = 0
            self.game_board[final_row][final_col] = 1
            self.num_pegs_left -= 1
        else:
            print("Invalid Move! Try Again!")

if __name__ == "__main__":
    Game = Model()

