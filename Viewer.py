from Model import game_board[]
class Viewer:
    def __init__(self):
        self.peg_symbol = '📍'
        self.hole_symbol = '🕳'

    def print_board(self):
        for i in range(0, 4):
            for j in range(0, i+1):
                print(game_board[i][j])
