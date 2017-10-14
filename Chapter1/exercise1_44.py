# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%_thm_1.44
"""
from operator import add, sub, truediv

from Chapter1.exercise1_43 import repeated
from Chapter1.newton_method import dx


def smooth(f):
    return lambda x: average(
        f(sub(x, dx())),
        f(x),
        f(add(x, dx()))
    )


def average(a, b, c):
    return truediv(
        add(add(a, b), c),
        3
    )


def nfold_smooth(f, n):
    return repeated(smooth, n)(f)
