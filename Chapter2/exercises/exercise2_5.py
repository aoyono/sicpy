# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#%_thm_2.5
"""
import math

from Chapter1.exercises.exercise1_9 import inc
from Chapter1.themes.tfp_searching_for_divisors import divides


def cons(a, b):
    return math.pow(2, a) * math.pow(3, b)


def extract_expt(a, n):
    def iterate(n, acc):
        if divides(a, n):
            return iterate(
                n // a,
                inc(acc)
            )
        return acc
    return iterate(n, 0)


def car(z):
    return extract_expt(2, z)


def cdr(z):
    return extract_expt(3, z)


def run_the_magic():
    a, b = 2, 3
    x = cons(a, b)
    print('(define x (cons %(a)s %(b)s))' % locals())
    print('(car x)')
    print(car(x))
    print('(cdr x)')
    print(cdr(x))


if __name__ == '__main__':
    run_the_magic()
