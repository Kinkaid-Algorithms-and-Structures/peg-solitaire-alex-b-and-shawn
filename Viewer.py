from Model import Model
class Viewer:
    def __init__(self):
        self.peg_symbol = '📍'
        self.hole_symbol = '🕳'
        self.MyModel = Model()

    def print_board(self):
        for i in range(0, 5):
            for j in range(0, i+1):
                print(self.MyModel.game_board[i][j])
