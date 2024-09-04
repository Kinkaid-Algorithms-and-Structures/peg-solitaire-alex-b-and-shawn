from itertools import filterfalse

from Model import Model
class Controller:
    def __init__(self):
        self.any_valid_moves = False
        self.has_won = False
        self.starting_hole = [0,0]
        self.MyModel = Model()

    def is_in_bounds(self, position_X, position_Y):
        """

        :param position_X:
        :param position_Y:
        :return: boolean
        """
        if position_X >= 5:
            return False
        elif position_Y >= 5:
            return False
        else:
            return True

    def is_move_valid(self, final_positionX, final_positionY, initial_positionX, initial_positionY):
        if self.is_in_bounds(final_positionX, final_positionY) == False or self.is_in_bounds(initial_positionX, initial_positionY) == False:
            return False
        if self.MyModel.game_board[final_positionY][final_positionX] is not None:
            return False
        elif self.MyModel.game_board[final_positionY][final_positionX] == self.MyModel.game_board[initial_positionY][initial_positionX]:
            return False
        if final_positionY == initial_positionY:
            if initial_positionX == final_positionX + 1 or initial_positionX == final_positionX-1:
                return False
        if final_positionX == final_positionX:
            if initial_positionY == final_positionY+1 or initial_positionY == final_positionY-1:
                return False



    def choose_starting_hole(self):
        """
        :param peg:
        :return: nothing
        """
        starting_hole = input("Which space do you want to be the first empty peg? Type it in form of \"2,3\" ")
