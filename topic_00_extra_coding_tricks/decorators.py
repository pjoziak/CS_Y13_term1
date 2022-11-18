from typing import Callable, Dict
from random import gauss


def decorator_1(func):
    def inner(*arg, **kwarg):
        print('[decorator_1] Before func evaluation')
        ret = func(*arg, **kwarg)
        print('[decorator_1] After func evaluation')
        return ret
    return inner


@decorator_1
def print_hello_world():
    print('Hello, world!')


@decorator_1
def hello_name(name: str):
    print(f'Hello, {name}!')


def noisy(generator: Callable, params: Dict = {}):
    def noisy_func(func: Callable[[float, ...], float]):
        def noised_func(*arg):
            noise = generator(**params)
            return func(*arg) + noise
        return noised_func
    return noisy_func


@noisy(generator=gauss, params={'mu': 0, 'sigma': 0.16})
def square(x: float) -> float:
    return x ** 2


if __name__ == '__main__':
    print_hello_world()
    hello_name('Pawel')
    for _ in range(4):
        print(f'Noised 4**2 is {square(4)}')

