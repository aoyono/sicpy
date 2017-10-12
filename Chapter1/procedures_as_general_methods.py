# -*- coding: utf-8 -*-
from operator import add, and_, lt, mul, sub, truediv

from Chapter1.sqrt_newton import average
from utils import error, let


def is_close_enough(x, y): return lt(abs(sub(x, y)), 0.001)


def is_positive(value): return value > 0


def is_negative(value): return value < 0


# Finding roots of equations by the half-interval method

def search(f, neg_point, pos_point):
    with let(average(neg_point, pos_point)) as (midpoint,):
        if is_close_enough(neg_point, pos_point):
            return midpoint
        with let(f(midpoint)) as (test_value,):
            if is_positive(test_value):
                return search(f, neg_point, midpoint)
            elif is_negative(test_value):
                return search(f, midpoint, pos_point)
            else:
                return midpoint


def half_internal_method(f, a, b):
    with let(f(a), f(b)) as (a_value, b_value):
        if and_(is_negative(a_value), is_positive(b_value)):
            return search(f, a, b)
        elif and_(is_negative(b_value), is_positive(a_value)):
            return search(f, b, a)
        else:
            error("Values are not of opposite sign", a, b)


# Finding fixed points of functions

def tolerance(): return 0.00001


def fixed_point(f, first_guess):
    def close_enough(v1, v2): return lt(abs(sub(v1, v2)), tolerance())

    def try_(guess):
        with let(f(guess)) as (next,):
            if close_enough(guess, next):
                return next
            return try_(next)

    return try_(first_guess)


# sqrt computation with fixed_point method using **average damping** (averaging successive approximations to a solution)
def sqrt(x):
    return fixed_point(
        lambda y: average(y, truediv(x, y)),
        1.0
    )


if __name__ == '__main__':
    from math import sin, cos

    a, b = 2.0, 4.0
    print("(half-interval-method sin %(a)s %(b)s)" % locals())
    print(half_internal_method(sin, a, b))
    a, b = 1.0, 2.0
    print("(half-interval-method (lambda (x) (- (* x x x) (* 2 x) 3) %(a)s %(b)s)" % locals())
    print(half_internal_method(
        lambda x: sub(sub(mul(x, mul(x, x)), mul(2, x)), 3),
        a,
        b
    ))

    fg = 1.0
    print("(fixed-point cos %(fg)s)" % locals())
    print(fixed_point(cos, fg))

    fg = 1.0
    print("(fixed-point (lambda (y) (+ (sin y) (cos y))) %(fg)s)" % locals())
    print(fixed_point(
        lambda y: add(sin(y), cos(y)),
        fg
    ))
