# -*- coding: utf-8 -*-
"""
Alyssa P. Hacker doesn't see why if needs to be provided as a special form. ``Why can't I
just define it as an ordinary procedure in terms of cond?'' she asks. Alyssa's friend Eva
Lu Ator claims this can indeed be done, and she defines a new version of if:

(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))

Eva demonstrates the program for Alyssa:

(new-if (= 2 3) 0 5)
5

(new-if (= 1 1) 0 5)
0

Delighted, Alyssa uses new-if to rewrite the square-root program:

(define (sqrt-iter guess x)
  (new-if (good-enough? guess x)
          guess
          (sqrt-iter (improve guess x)
                     x)))

What happens when Alyssa attempts to use this to compute square roots? Explain.
"""
from operator import eq

from Chapter1.lisp_conditionals import lisp_cond
from Chapter1.sqrt_newton import is_good_enough, improve


def new_if(predicate, then_clause, else_clause):
    return lisp_cond(
        (predicate, then_clause),
        _else=else_clause
    )


def sqrt_iter(guess, x):
    """This will generate an infinite recursion loop due to the model of evaluation (application-order)

    new_if is a procedure and not a special form => the arguments are evaluated first, before application of new_if,
    but the else_clause of new_if is a recursive call to sqrt_iter, leading to new_if never being called (applied to
    its parameters)
    """
    return new_if(
        is_good_enough(guess, x),
        guess,
        sqrt_iter(improve(guess, x), x)
    )


def sqrt(x):
    return sqrt_iter(1.0, x)


if __name__ == '__main__':
    print('Testing new_if ...')
    print(
        new_if(
            eq(2, 3),
            0,
            5
        )
    )
    print(
        new_if(
            eq(1, 1),
            0,
            5
        )
    )
    print('Testing new_if in sqrt(10000) ...')
    print(
        sqrt(10000)
    )
