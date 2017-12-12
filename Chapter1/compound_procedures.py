from operator import *


def square(x):
    return mul(x, x)


def sum_of_squares(x, y):
    return add(square(x), square(y))


def f(a):
    return sum_of_squares(
        add(a, 1),
        mul(a, 2)
    )


def run_the_magic():
    print(square(21))
    print(square(add(2, 5)))
    print(square(square(3)))
    print(sum_of_squares(3, 4))
    print(f(5))


if __name__ == '__main__':
    run_the_magic()
