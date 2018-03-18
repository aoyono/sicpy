# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#%_thm_2.4

Procedural representation of data is called Message Passing
"""


def cons(x, y):
    return lambda m: m(x, y)


def car(z):
    return z(lambda p, q: p)


def cdr(z):
    return z(lambda p, q: q)
