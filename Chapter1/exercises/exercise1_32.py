# -*- coding: utf-8 -*-
"""
a. Show that sum and product (exercise 1.31) are both special cases of a still more general notion called accumulate
that combines a collection of terms, using some general accumulation function:

(accumulate combiner null-value term a next b)

Accumulate takes as arguments the same term and range specifications as sum and product, together with a combiner
procedure (of two arguments) that specifies how the current term is to be combined with the accumulation of the
preceding terms and a null-value that specifies what base value to use when the terms run out. Write accumulate and show
how sum and product can both be defined as simple calls to accumulate.

b. If your accumulate procedure generates a recursive process, write one that generates an iterative process. If it
generates an iterative process, write one that generates a recursive process.
"""
from operator import add, gt, mul, sub, truediv

from Chapter1.themes.compound_procedures import square
from Chapter1.exercises.exercice1_8 import cube
from Chapter1.exercises.exercise1_9 import inc


def accumulate_recursive(combiner, null_value, term, a, next, b):
    if gt(a, b):
        return null_value
    return combiner(
        term(a),
        accumulate_recursive(combiner, null_value, term, next(a), next, b)
    )


def accumulate(combiner, null_value, term, a, next, b):
    def iterate(a, result):
        if gt(a, b):
            return result
        return iterate(
            next(a),
            combiner(
                result,
                term(a)
            )
        )
    return iterate(a, null_value)


def generic_sum(term, a, next, b):
    return accumulate(
        combiner=add,
        null_value=0,
        term=term,
        a=a,
        next=next,
        b=b
    )


def product(term, a, next, b):
    return accumulate(
        combiner=mul,
        null_value=1,
        term=term,
        a=a,
        next=next,
        b=b
    )


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


def factorial(n):
    return product(
        identity,
        1,
        inc,
        n
    )


def inv(x): return truediv(1, x)


def pi_wallis(n):
    def term(k): return sub(
        1,
        inv(square(inc(mul(2, k))))
    )

    return mul(
        4,
        product(term, 1, inc, n)
    )


# End applications


def run_the_magic():
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
    n = 990
    print('(factorial {})'.format(n))
    print(factorial(n))
    print('(pi-wallis %(n)s)' % locals())
    print(pi_wallis(n))


if __name__ == '__main__':
    run_the_magic()
