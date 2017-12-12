# -*- coding: utf-8 -*-
"""
"""
from operator import truediv

from Chapter1.compound_procedures import square
from Chapter1.procedures_as_general_methods import fixed_point
from Chapter1.sqrt_newton import average


def average_damp(f):
    return lambda x: average(x, f(x))


def sqrt(x):
    return fixed_point(
        average_damp(lambda y: truediv(x, y)),
        1.0
    )


def cube_root(x):
    return fixed_point(
        average_damp(lambda y: truediv(x, square(y))),
        1.0
    )


def run_the_magic():
    f, x = square.__name__, 100
    print('((average-damp %(f)s) %(x)s)' % locals())
    print(average_damp(square)(x))
    print('(sqrt %(x)s)' % locals())
    print(sqrt(x))
    print('(cube-root %(x)s)' % locals())
    print(cube_root(x))


if __name__ == '__main__':
    run_the_magic()
