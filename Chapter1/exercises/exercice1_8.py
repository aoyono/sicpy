# -*- coding: utf-8 -*-
"""
Newton's method for cube roots is based on the fact that if y is an approximation to the cube root of x, then a better
approximation is given by the value:

(x/y² + 2y)/3

Use this formula to implement a cube-root procedure analogous to the square-root procedure. (In section 1.3.4 we will
see how to implement Newton's method in general as an abstraction of these square-root and cube-root procedures.)
"""
from operator import add, lt, mul, sub, truediv

from Chapter1.themes.compound_procedures import square
from Chapter1.themes.lisp_conditionals import lisp_abs


def cube_root(x):
    return cube_root_iter(1, x)


def cube_root_iter(guess, x):
    if is_good_enough(guess, x):
        return guess
    return cube_root_iter(improve(guess, x), x)


def is_good_enough(guess, x):
    return lt(
        lisp_abs(sub(cube(guess), x)),
        0.001
    )


def improve(guess, x):
    return truediv(
        add(
            truediv(x, square(guess)),
            mul(2, guess)
        ),
        3
    )


def cube(x):
    return mul(square(x), x)


def run_the_magic():
    print(cube_root(27))


if __name__ == '__main__':
    run_the_magic()
