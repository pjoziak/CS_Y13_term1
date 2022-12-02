import unittest
from ddt import ddt, unpack, data

from topic_07_rpn.core.convert import infix_to_rpn


@ddt
class SplitInfixTestCase(unittest.TestCase):
    @data(
        ["1 * 2 - 3", ["1", "2", "*", "3", "-"]],
        ["2^3 - 6 / 2", ["2", "3", "^", "6", "2", "/", "-"]],
        # more examples, including parantheses
    )
    @unpack
    def test_convert(self, infix, rpn):
        self.assertEqual(infix_to_rpn(infix), rpn)


if __name__ == '__main__':
    unittest.main()
