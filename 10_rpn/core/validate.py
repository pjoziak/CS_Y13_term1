from rpn.core.utils import is_operator


def validate_rpn(*symbols: str):
    assert len(symbols) % 2 == 1
    if len(symbols) >= 2:
        assert not is_operator(symbols[0]) and not is_operator(symbols[1])
    operators = []
    numbers = []
    for symbol in symbols:
        if is_operator(symbol):
            operators.append(symbol)
        else:
            numbers.append(symbol)
        assert len(operators) < len(symbols)
    assert len(numbers) - len(operators) == 1
