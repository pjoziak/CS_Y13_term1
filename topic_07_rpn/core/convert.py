from typing import List

from topic_07_rpn.core.utils import (
    is_operand, is_open_parenthesis, is_closed_parenthesis, is_preceeding_operator, is_parenthesis, split_infix
)

# Infix to postfix conversion algorithm
# 1. Process entities one by one.
# 2. If we encounter an operand: push it onto the output stack.
# 3. If we process '(': push it onto the operator stack.
# 4. If we process ')': get an operator from operator stack and push it onto the output stack. Repeat until
#    we get '(' -- which we discard, along with ')'
# 5. If we process any other operator, and the operator stack is empty -- push the operator there.
# 6. Otherwise (we are processing operator distinct than parentheses and operator stack is non-empty):
#    get an operator from the operator stack. If the (got) operator preceeds (processed) operator, push
#    the (got) operator onto the output stack. Repeat until the (got) operator does not precees (processed) operator,
#    push back the (got) operator, and then push the (processed) operator onto the operator stack.
# 7. If all the entities have been processed, get an operator from operator stack and push it onto output stack.
#    Repeat until operator stack is empty.


def infix_to_rpn(expression: str) -> List[str]:
    symbols = split_infix(expression)
    operator_stack = []
    output_stack = []
    for symbol in symbols:
        if is_operand(symbol):
            output_stack.append(symbol)
        elif is_open_parenthesis(symbol):
            operator_stack.append(symbol)
        elif is_closed_parenthesis(symbol):
            operator = operator_stack.pop()
            while not is_open_parenthesis(operator):
                output_stack.append(operator)
                operator = operator_stack.pop()
        else:
            if len(operator_stack) == 0:
                operator_stack.append(symbol)
            else:
                last_operator = operator_stack.pop()
                while is_preceeding_operator(first=last_operator, second=symbol) and not is_parenthesis(last_operator):
                    output_stack.append(last_operator)
                    if len(operator_stack) == 0:
                        break
                    last_operator = operator_stack.pop()
                if is_preceeding_operator(first=symbol, second=last_operator) or is_parenthesis(last_operator):
                    operator_stack.append(last_operator)
                operator_stack.append(symbol)
    operator_stack.reverse()
    for operator in operator_stack:
        output_stack.append(operator)
    return output_stack
