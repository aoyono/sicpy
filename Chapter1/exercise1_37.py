# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%_thm_1.37
"""
from operator import add, truediv

from Chapter1.exercise1_9 import dec, inc


def cont_frac(n, d, k):
    def recurse(i):
        if i > k:
            return truediv(
                n(i),
                d(i)
            )
        return add(
            d(dec(i)),
            truediv(
                n(i),
                recurse(inc(i))
            )
        )

    return truediv(
        n(1),
        recurse(2)
    )


def cont_frac_iter(n, d, k):
    def iterate(i, acc):
        if k == 0:
            return acc
        return iterate(
            dec(i),
            truediv(
                n(i),
                add(d(i), acc)
            )
        )
    return iterate(k, 0)


if __name__ == '__main__':
    from Chapter1.exercise1_35 import golden_ratio
    from Chapter1.exercise1_32 import inv

    k = 1
    while True:
        try:
            print("* k = %(k)s" % locals())
            print("(cont-frac (lambda (i) 1.0) (lambda (i) 1.0) %(k)s)" % locals())
            print(cont_frac(
                lambda i: 1.0,
                lambda i: 1.0,
                k
            ))
            k = inc(k)
        except RecursionError:
            print("RecursionError")
            break
        finally:
            print("---------------------------------------------------------------")

    print("(/ 1 (golden-ratio)))")
    print(inv(golden_ratio()))
