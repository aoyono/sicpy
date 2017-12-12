# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%_thm_1.39
"""
from operator import mul, sub

from Chapter1.compound_procedures import square
from Chapter1.exercise1_37 import cont_frac


def tan_cf(x, k):
    return cont_frac(
        lambda i: x if i == 1 else square(x),
        lambda i: sub(mul(2, i), 1),
        k
    )


def run_the_magic():
    import math
    x, k = math.radians(90), 100
    print("(tan-cf %(x)s %(k)s)" % locals())
    print(tan_cf(x, k))


if __name__ == '__main__':
    run_the_magic()
