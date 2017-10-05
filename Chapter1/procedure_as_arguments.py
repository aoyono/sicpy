# -*- coding: utf-8 -*-
"""
"""
from operator import add, gt, mul, truediv

from Chapter1.exercice1_8 import cube
from Chapter1.exercise1_9 import inc


# Trivial definitions
def sum_ints(a, b):
    if gt(a, b):
        return 0
    return add(
        a,
        sum_ints(add(a, 1), b)
    )


def sum_cubs(a, b):
    if gt(a, b):
        return 0
    return add(
        cube(a),
        sum_cubs(add(a, 1), b)
    )


def pi_sum1(a, b):
    if gt(a, b):
        return 0
    return add(
        truediv(1.0, mul(a, add(a, 2))),
        pi_sum1(add(a, 4), b)
    )


# End trivial definitions


# Generic sum definition (higher order function)
def generic_sum(term, a, next, b):
    if gt(a, b):
        return 0
    return add(
        term(a),
        generic_sum(term, next(a), next, b)
    )


# End Generic sum definition (higher order function)


# Application
def sum_cubes(a, b):
    return generic_sum(
        cube,
        a,
        inc,
        b
    )


def identity(x): return x


def sum_integers(a, b):
    return generic_sum(
        identity,
        a,
        inc,
        b
    )


def pi_sum(a, b):
    def pi_term(x): return truediv(
        1.0,
        mul(x, add(x, 2))
    )

    def pi_next(x): return add(x, 4)

    return generic_sum(
        pi_term,
        a,
        pi_next,
        b
    )


def integral(f, a, b, dx):
    def add_dx(x): return add(x, dx)

    return mul(
        generic_sum(
            f,
            add(
                a,
                truediv(dx, 2.0)
            ),
            add_dx,
            b
        ),
        dx
    )


# End applications


if __name__ == '__main__':
    a, b = 1, 10
    print(
        '(sum-cubes %(a)s %(b)s)' % locals(),
        sum_cubes(a, b),
        sep='\n'
    )
    print(
        '(sum-integers %(a)s %(b)s)' % locals(),
        sum_integers(a, b),
        sep='\n'
    )
    b = 1000
    print(
        '(* 8 (pi-sum %(a)s %(b)s))' % locals(),
        mul(8, pi_sum(a, b)),
        sep='\n'
    )
    a, b, dx = 0, 1, 0.1
    print(
        '(integral cube %(a)s %(b)s %(dx)s)' % locals(),
        integral(cube, a, b, dx),
        sep='\n'
    )
    dx = 0.01
    print(
        '(integral cube %(a)s %(b)s %(dx)s)' % locals(),
        integral(cube, a, b, dx),
        sep='\n'
    )
