# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%_thm_1.43
"""
from operator import eq

from Chapter1.compound_procedures import square
from Chapter1.exercise1_42 import compose
from Chapter1.exercise1_9 import dec


def repeated(f, n):
    if eq(n, 1):
        return f
    return compose(f, repeated(f, dec(n)))


if __name__ == '__main__':
    print('((repeated square 2) 5)')
    print(repeated(square, 2)(5))
