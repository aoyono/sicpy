# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%_thm_1.38
"""
from operator import mul, truediv, add

from Chapter1.exercise1_37 import cont_frac
from Chapter1.exercise1_9 import inc
from Chapter1.tfp_searching_for_divisors import divides


def approx_e(k):
    def d(i):
        if divides(3, inc(i)):
            return mul(
                2,
                truediv(3, inc(i))
            )
        return 1.0
    return add(
        2.0,
        cont_frac(
            lambda i: 1.0,
            d,
            k
        )
    )


if __name__ == '__main__':
    from math import e

    k = 1
    while True:
        try:
            print("(approx-e %(k)s)" % locals())
            print(approx_e(k))
            k = inc(k)
        except RecursionError:
            print("RecursionError")
            break
        finally:
            print("---------------------------------------------------------------")

    print("(e)")
    print(e)