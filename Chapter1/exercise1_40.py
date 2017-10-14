# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%_thm_1.40
"""
from operator import add, mul

from Chapter1.compound_procedures import square
from Chapter1.exercice1_8 import cube
from Chapter1.newton_method import newtons_method


def cubic(a, b, c):
    return lambda x: add(
        add(
            add(
                cube(x),
                mul(
                    a,
                    square(x)
                )
            ),
            mul(b, x)
        ),
        c
    )


if __name__ == '__main__':
    a, b, c = 1, 2, 3
    print('(newtons-method (cubic %(a)s %(b)s %(c)s) 1)' % locals())
    res = newtons_method(
        cubic(a, b, c),
        1.0
    )
    print(res)
    print('((cubic %(a)s %(b)s %(c)s) %(res)s)' % locals())
    print(cubic(a, b, c)(res))
