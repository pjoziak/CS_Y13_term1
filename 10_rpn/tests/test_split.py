import unittest

from rpn.core.utils import split_infix


class SplitInfixTestCase(unittest.TestCase):
    infix_0 = "1 * 2 - 3"
    splitted_0 = ["1", "*", "2", "-", "3"]

    infix_1 = "(7 + 10 / 5) * (6 + 2)"
    splitted_1 = ["(", "7", "+", "10", "/", "5", ")", "*", "(", "6", "+", "2", ")"]

    infix_2 = "6 * (3 - (3 - 2 / 1)) + 1"
    splitted_2 = ["6", "*", "(", "3", "-", "(", "3", "-", "2", "/", "1", ")", ")", "+", "1"]

    infix_3 = "2^3 - 6 / 2"
    splitted_3 = ["2", "^", "3", "-", "6", "/", "2"]

    def test_split_0(self):
        splitted = split_infix(self.infix_0)
        self.assertEqual(splitted, self.splitted_0)

    def test_split_1(self):
        splitted = split_infix(self.infix_1)
        self.assertEqual(splitted, self.splitted_1)


if __name__ == '__main__':
    unittest.main()