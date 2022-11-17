from typing import List


def is_operator(symbol: str):
    return symbol in {'+', '-', '*', '/', '^'}


def is_preceeding_operator(first: str, second: str) -> bool:
    order = ['(', ')', '^', '*', '/', '+', '-']
    return order.index(first) <= order.index(second)


def is_open_parenthesis(symbol: str):
    return symbol in {'(', '[', '{'}


def is_closed_parenthesis(symbol: str):
    return symbol in {')', ']', '}'}


def is_parenthesis(symbol: str):
    return is_open_parenthesis(symbol) or is_closed_parenthesis(symbol)


def is_operand(symbol: str):
    return not is_operator(symbol) and not is_parenthesis(symbol)


def split_infix(expression: str) -> List[str]:
    continue_number = True
    continue_from = 0
    ret = []
    for i, char in enumerate(expression):
        if char.isdigit() and continue_number:
            continue
        if not char.isdigit() and continue_number:
            number = expression[continue_from: i]
            ret.append(number)
            continue_number = False
        if char.isdigit() and not continue_number:
            continue_number = True
            continue_from = i
        if not char.isdigit() and not continue_number:
            if is_operator(char) or is_parenthesis(char):
                ret.append(char)
    if continue_number:
        number = expression[continue_from: i + 1]
        ret.append(number)
    return [item for item in ret if item]

