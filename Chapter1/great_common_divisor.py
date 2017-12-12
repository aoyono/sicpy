# -*- coding: utf-8 -*-
"""
"""
from operator import eq, mod


def gcd(a, b):
    if eq(b, 0):
        return a
    return gcd(
        b,
        mod(a, b)
    )


def run_the_magic():
    from timeit import Timer
    a, b = 206, 40
    print(
        '(gcd %(a)s %(b)s)' % locals(),
        gcd(a, b),
        sep='\n',
    )
    timer = Timer(
        stmt='gcd(%(a)s, %(b)s)' % locals(),
        setup='from Chapter1.great_common_divisor import gcd'
    )
    print('Mean execution time: %s' %(timer.timeit(),))


if __name__ == '__main__':
    run_the_magic()
