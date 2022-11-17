from typing import Union

from .utils import is_operator
from .validate import validate_rpn


def perform_operation(operand1: str, operand2: str, operator: str):
    op1 = float(operand1)
    op2 = float(operand2)
    if op1.is_integer():
        op1 = int(op1)
    if op2.is_integer():
        op2 = int(op2)
    if operator == '+':
        return op1 + op2
    if operator == '-':
        return op1 - op2
    if operator == '*':
        return op1 * op2
    if operator == '/':
        return op1 / op2
    if operator == '^':
        return op1 ** op2


def evaluate_rpn(*symbols: str) -> Union[int, float]:
    try:
        validate_rpn(*symbols)
    except AssertionError:
        print('Not a valid expression')
        return 0.
    stack = []
    for symbol in symbols:
        if is_operator(symbol):
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(perform_operation(operand2, operand1, symbol))
        else:
            stack.append(symbol)
    ret = float(stack.pop())
    if ret.is_integer():
        return int(ret)
    return ret
