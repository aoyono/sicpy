# -*- coding: utf-8 -*-
"""
Modify fixed-point so that it prints the sequence of approximations it generates, using the newline and display
primitives shown in exercise 1.22. Then find a solution to xx = 1000 by finding a fixed point of x log(1000)/log(x).
(Use Scheme's primitive log procedure, which computes natural logarithms.) Compare the number of steps this takes with
and without average damping. (Note that you cannot start fixed-point with a guess of 1, as this would cause division by
log(1) = 0.)
"""
from operator import sub, lt, truediv

from Chapter1.procedures_as_general_methods import tolerance
from Chapter1.sqrt_newton import average
from utils import let


def fixed_point(f, first_guess):
    def close_enough(v1, v2): return lt(abs(sub(v1, v2)), tolerance())

    def try_(guess):
        print(guess)
        with let(f(guess)) as (next,):
            if close_enough(guess, next):
                return next
            return try_(next)

    return try_(first_guess)


def run_the_magic():
    from math import log
    fg = 2.0
    print("(fixed-point (lambda (x) (/ (log 1000) (log x))) %(fg)s)" % locals())
    print(fixed_point(
        lambda x: truediv(log(1000), log(x)),
        fg
    ))

    # With average damping
    print("(fixed-point (lambda (x) (average x (/ (log 1000) (log x)))) %(fg)s)" % locals())
    print(fixed_point(
        lambda x: average(x, truediv(log(1000), log(x))),
        fg
    ))


if __name__ == '__main__':
    run_the_magic()
