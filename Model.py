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

    def move_peg(self, peg, final_position):
        if()

if __name__ == "__main__":
    Game = Model()

