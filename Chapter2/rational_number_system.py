# -*- coding: utf-8 -*-
"""
"""
from Chapter1.great_common_divisor import gcd
from Chapter2.lisp_list_structured_data import car, cdr, cons
from utils import let


def make_rat(num, den):
    """The IF block comes from exercise 2.1"""
    with let(gcd(num, den)) as (g,):
        if num * den < 0:
            return cons(
                - abs(num) // g,
                abs(den) // g
            )
        return cons(
            abs(num) // g,
            abs(den) // g
        )


def numer(x):
    return car(x)


def denom(x):
    return cdr(x)


def add_rat(x, y):
    return make_rat(
        numer(x) * denom(x) + numer(y) * denom(y),
        denom(x) * denom(y)
    )


def sub_rat(x, y):
    return make_rat(
        numer(x) * denom(x) - numer(y) * denom(y),
        denom(x) * denom(y)
    )


def mul_rat(x, y):
    return make_rat(
        numer(x) * numer(y),
        denom(x) * denom(y)
    )


def div_rat(x, y):
    return make_rat(
        numer(x) * denom(y),
        denom(x) * numer(y)
    )


def equal_rat(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


def print_rat(x):
    print('{}/{}'.format(numer(x), denom(x)))


if __name__ == '__main__':
    def one_half(): return make_rat(1, 2)
    print('(print-rat one-half)')
    print_rat(one_half())

    def one_third(): return make_rat(1, 3)
    print('(print-rat (add-rat one-half one-third))')
    print_rat(
        add_rat(
            one_half(),
            one_third()
        )
    )
    print('(print-rat (mul-rat one-half one-third))')
    print_rat(
        mul_rat(
            one_half(),
            one_third()
        )
    )
    print('(print-rat (add-rat one-third one-third))')
    print_rat(
        add_rat(
            one_third(),
            one_third()
        )
    )
