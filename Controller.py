from itertools import filterfalse
from Model import Model

class Controller:
    def __init__(self):
        self.any_valid_moves = False
        self.has_won = False
        self.starting_hole = [0,0]

    def set_model(self, model):
        self.model = model

    def choose_starting_hole(self):
        starting_hole = input("Which space do you want to be the first empty peg? Please type it in form of \"2,3\"")
        starting_row = int(starting_hole[0])
        starting_col = int(starting_hole[2])
        self.model.delete_peg(starting_row, starting_col)

    def game_turn(self):
        starting_peg = input("Which peg would you like to move?")
        final_peg = input("Where would you like to move it?")
        starting_row = int(starting_peg[0])
        starting_col = int(starting_peg[2])
        final_row = int(final_peg[0])
        final_col = int(final_peg[2])
        print(starting_row, starting_col, final_row, final_col)
        self.model.make_move(starting_row, starting_col, final_row, final_col)


