import unittest

from FirstModule.mylib import *


class TestCaseMyLib(unittest.TestCase):

    def test_calculate_multiplication(self):
        result = calculate(1, 3, "*")
        self.assertEqual(result, 3)

    def test_calculate_addition(self):
        result = calculate(1, 3, "+")
        self.assertEqual(result, 4)

    def test_calculate_subtraction(self):
        result = calculate(1, 3, "-")
        self.assertEqual(result, -2)

    def test_calculate_division(self):
        result = calculate(4, 2, "/")
        self.assertEqual(result, 2)

    def test_calculate_division_exception(self):
        self.assertEqual("__error__", calculate(1, 0, "/"))

    def test_mymap_square_function(self):
        testlist = list(range(1, 4))
        listhouldbe = [1, 4, 9]
        mymap(testlist, square)
        self.assertEqual(testlist, listhouldbe)

    def test_mymap_decrement_function(self):
        testlist = list(range(1, 4))
        listshouldbe = [0, 1, 2]
        mymap(testlist, decrement)
        self.assertEqual(testlist, listshouldbe)


if __name__ == '__main__':
    unittest.main()