# -*- coding: utf-8 -*-
"""
"""
from operator import add, sub, truediv

from Chapter1.compound_procedures import square
from Chapter1.procedures_as_general_methods import fixed_point


def deriv(g):
    return lambda x: truediv(
        sub(
            g(add(x, dx())),
            g(x)
        ),
        dx()
    )


def dx(): return 0.00001


def newton_transform(g):
    return lambda x: sub(
        x,
        truediv(
            g(x),
            deriv(g)(x)
        )
    )


def newtons_method(g, guess):
    return fixed_point(
        newton_transform(g),
        guess
    )


def sqrt(x):
    return newtons_method(
        lambda y: sub(
            square(y),
            x
        ),
        1.0
    )


def run_the_magic():
    x = 10000.0
    print('(sqrt %(x)s)' % locals())
    print(sqrt(x))


if __name__ == '__main__':
    run_the_magic()
