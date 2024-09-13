import logging, datetime
from KinkaidDecorators import log_start_stop_method
from Controller import Controller
from Viewer import Viewer
from Model import Model

logging.basicConfig(level=logging.INFO)  # simple version to the output console
# logging.basicConfig(level=logging.DEBUG, filename=f"log {datetime.datetime.now():%m-%d@%H:%M:%S}.txt",
#                     format="%(asctime)s %(levelname)s %(message)s",
#                     datefmt="%H:%M:%S %p --- ")  # more robust, sent to a file cNode = Tuple[int, T]

class PegSolitaireRunner:
    def __init__(self):
        logging.info("Initializing.")
        # add any code you want to set up variables for the game.
    
    def play_game(self):  # note: this is complaining (grey underline) that it could be static because it doesn't use
        # any variables or methods from "self." Once you do, it will stop pestering you about it.
        my_controller = Controller()
        my_viewer = Viewer()
        my_model = Model()

        my_viewer.set_controller(my_controller)
        my_controller.set_model(my_model)

        print("-------------------Welcome to Peg Solitaire!-------------------".center(69, " "))
        print("The goal of the game is to remove as many pegs as possible".center(69, " "))
        print('Remove pegs by "jumping" over them with other pegs'.center(69, " "))
        print("Each hole on the board is represented by a coordinate from 0,0 to 4,4".center(69, " "))
        print('Select pegs by typing their coordinates in the format "row,col"'.center(69, " "))
        print("---------------------------------------------------------------".center(69, " "))
        print()

        my_controller.choose_starting_hole()
        my_viewer.print_board()

        while True:
            my_controller.game_turn()
            my_viewer.print_board()
            if my_model.num_pegs_left == 1:
                print()
                print("*********************************************************************".center(69, " "))
                print()
                print("You Win!".center(69, " "))
                print()
                print("*********************************************************************".center(69, " "))
                break
            if not my_model.any_valid_moves():
                score = f"Score: {my_model.num_pegs_left}"
                print()
                print("*********************************************************************".center(69, " "))
                print()
                print("GAME OVER".center(69, " "))
                print("No More Valid Moves".center(69, " "))
                print(score.center(69, " "))
                print()
                print("*********************************************************************".center(69, " "))
                break


if __name__ == "__main__":
    game = PegSolitaireRunner()
    game.play_game()
