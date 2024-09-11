from Model import Model
class Viewer:
    def __init__(self):
        self.peg_symbol = '📍'
        self.hole_symbol = '🕳'
        self.MyModel = Model()

    def print_board(self):
        for r in range(0, 5):
            for c in range(0, r + 1):
                print(self.MyModel.game_board[r][c], end="")
            print()