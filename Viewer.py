from Model import Model
from Controller import Controller

class Viewer:
    def __init__(self):
        self.peg_symbol = '📍'
        self.hole_symbol = '🕳'


    def set_controller(self, controller):
        self.controller = controller

    def print_board(self):
        for r in range(0, 5):
            print(r, end =" ")
            for c in range(0, r + 1):
                if self.controller.model.game_board[r][c] == 1:
                    print(self.peg_symbol, end ="")
                else:
                    print(self.hole_symbol, end ="")
            print()
        print("   0 1 2 3 4")