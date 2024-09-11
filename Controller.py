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
        if position_X > position_Y:
            return False
        if position_X > 4:
            return False
        elif position_Y > 4:
            return False
        else:
            return True


    def is_move_valid(self, final_positionX, final_positionY, initial_positionX, initial_positionY):
        """
        :param final_positionX:
        :param final_positionY:
        :param initial_positionX:
        :param initial_positionY:
        :return: boolean
        """
        if self.is_in_bounds(final_positionX, final_positionY) == False or self.is_in_bounds(initial_positionX, initial_positionY) == False:
            return False
        if self.MyModel.game_board[final_positionY][final_positionX] is not None:
            return False
        elif self.MyModel.game_board[final_positionY][final_positionX] == self.MyModel.game_board[initial_positionY][initial_positionX]:
            return False
        if final_positionY == initial_positionY:
            if initial_positionX == final_positionX +2:
                if self.MyModel.game_board[final_positionY][final_positionX-1]:
                    return True
            if initial_positionX == final_positionX-2:
                if self.MyModel.game_board[final_positionY][final_positionX+1]:
                    return True
        if final_positionX == final_positionX:
            if initial_positionY == final_positionY+2:
                if self.MyModel.game_board[final_positionY-1][final_positionX]:
                    return True
            if initial_positionY == final_positionY-2:
                if self.MyModel.game_board[final_positionY+1][final_positionX]:
                    return True
        return False

    def choose_starting_hole(self):
        starting_hole = input("Which space do you want to be the first empty peg? Type it in form of \"2,3\" ")
        starting_row = starting_hole[0]
        starting_col = starting_hole[0]
        Model.delete_peg(self.MyModel, starting_row, starting_col)



