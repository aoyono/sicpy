# -*- coding: utf-8 -*-
"""
The sum procedure above generates a linear recursion. The procedure can be rewritten so that the sum is performed
iteratively. Show how to do this by filling in the missing expressions in the following definition:

(define (sum term a next b)
  (define (iter a result)
    (if <??>
        <??>
        (iter <??> <??>)))
  (iter <??> <??>))
"""
from operator import add, eq, gt, mod, mul, sub, truediv

from Chapter1.exercises.exercice1_8 import cube
from Chapter1.exercises.exercise1_9 import inc


def generic_sum_iterative(term, a, next, b):
    def iterate(a, result):
        if gt(a, b):
            return result
        return iterate(
            next(a),
            add(
                result,
                term(a)
            )
        )

    return iterate(a, 0)


# Application
def sum_cubes(a, b):
    return generic_sum_iterative(
        cube,
        a,
        inc,
        b
    )


def identity(x): return x


def sum_integers(a, b):
    return generic_sum_iterative(
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

    return generic_sum_iterative(
        pi_term,
        a,
        pi_next,
        b
    )


def integral(f, a, b, dx):
    def add_dx(x): return add(x, dx)

    return mul(
        generic_sum_iterative(
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


def integral_simpson(f, a, b, n):
    def h():
        return truediv(
            sub(b, a),
            n
        )

    def simpson_term(k):
        if eq(k, 0):
            return f(a)
        if eq(k, n):
            return f(b)
        if eq(mod(k, 2), 0):
            return mul(
                2,
                f(add(
                    a,
                    mul(k, h())
                ))
            )
        return mul(
            4,
            f(add(
                a,
                mul(k, h())
            ))
        )

    return mul(
        generic_sum_iterative(
            simpson_term,
            0,
            inc,
            n
        ),
        truediv(h(), 3.0)
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
    a, b = 0, 1
    for n in (100, 1000):
        try:
            print(
                '(integral-simpson cube %(a)s %(b)s %(n)s)' % locals(),
                integral_simpson(cube, a, b, n),
                sep='\n'
            )
        except RecursionError:
            print('Recursion error for n = %(n)s' % locals())

if __name__ == '__main__':
    run_the_magic()
