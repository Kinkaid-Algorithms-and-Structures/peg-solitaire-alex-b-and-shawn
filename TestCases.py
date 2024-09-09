import unittest
from Controller import Controller


class MyTestCase(unittest.TestCase):

    def test_is_valid(self):
        self_my_controller = Controller()
        self.assertFalse(self_my_controller.is_move_valid(0, 0, 1, 0), "first test failed")
        self.assertFalse(self_my_controller.is_move_valid(0, 0, 0, 0), "first test failed")
        self.assertFalse(self_my_controller.is_move_valid(0, 0, 6, 0), "first test failed")
        self.assertFalse(self_my_controller.is_move_valid(7, 0, 1, 0), "first test failed")
        self.assertFalse(self_my_controller.is_move_valid(0, 0, 2, 0), "first test failed")


def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
