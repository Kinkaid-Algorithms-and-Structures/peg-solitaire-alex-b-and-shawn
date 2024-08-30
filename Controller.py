from Model import Model
class Controller:
    def __init__(self):
        self.any_valid_moves = False
        self.has_won = False
        self.starting_hole = [0,0]

    def is_move_valid(self, peg, final_position):
        if Model.game_board[final_position] is not None:
            return False



    def choose_starting_hole(self):
        """
        :param peg:
        :return: nothing
        """
        starting_hole = input("Which space do you want to be the first empty peg? Type it in form of \"2,3\" ")
