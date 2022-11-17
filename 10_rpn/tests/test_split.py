import unittest
from ddt import ddt, data, unpack

from ..core.utils import split_infix

@ddt
class SplitInfixTestCase(unittest.TestCase):
    @data(
        ["1 * 2 - 3", ["1", "*", "2", "-", "3"]],
        ["(7 + 10 / 5) * (6 + 2)", ["(", "7", "+", "10", "/", "5", ")", "*", "(", "6", "+", "2", ")"]],
        ["6 * (3 - (3 - 2 / 1)) + 1", ["6", "*", "(", "3", "-", "(", "3", "-", "2", "/", "1", ")", ")", "+", "1"]],
        ["2^3 - 6 / 2", ["2", "^", "3", "-", "6", "/", "2"]]
    )
    @unpack
    def test_split(self, infix, splitted):
        self.assertEqual(split_infix(infix), splitted)


if __name__ == '__main__':
    unittest.main()