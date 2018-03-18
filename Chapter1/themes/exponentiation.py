# -*- coding: utf-8 -*-
"""
"""
from operator import eq, mod, mul, sub, truediv

from cachetools import LRUCache, cached

from Chapter1.themes.compound_procedures import square


@cached(LRUCache(maxsize=128))
def naive_exp(b, n):
    if n == 0:
        return 1
    return mul(b, naive_exp(b, sub(n, 1)))


@cached(LRUCache(maxsize=128))
def linear_recursive_exp(b, n):
    def exp_iter(base, counter, product):
        if counter == 0:
            return product
        return exp_iter(base, sub(counter, 1), mul(base, product))

    return exp_iter(b, n, 1)


def is_even(n):
    return eq(mod(n, 2), 0)


@cached(LRUCache(maxsize=128))
def fast_expt(b, n):
    if eq(n, 0):
        return 1
    if is_even(n):
        return square(
            fast_expt(b, truediv(n, 2))
        )
    return mul(
        b,
        fast_expt(b, sub(n, 1))
    )


def run_the_magic():
    from timeit import Timer
    b, n = 2, 300
    timer_naive = Timer(stmt='naive_exp(%(b)s, %(n)s)' % locals(),
                        setup='from Chapter1.exponentiation import naive_exp')
    timer_iter = Timer(
        stmt='linear_recursive_exp(%(b)s, %(n)s)' % locals(),
        setup='from Chapter1.exponentiation import linear_recursive_exp'
    )
    timer_fast = Timer(stmt='fast_expt(%(b)s, %(n)s)' % locals(), setup='from Chapter1.exponentiation import fast_expt')
    print('(naive_exp %(b)s %(n)s)' % locals(), naive_exp(b, n), 'Time: %s' % (timer_naive.timeit(),), sep='\n')
    print('(linear_recursive_exp %(b)s %(n)s)' % locals(), linear_recursive_exp(b, n),
          'Time: %s' % (timer_iter.timeit(),), sep='\n')
    print('(fast_exp %(b)s %(n)s)' % locals(), fast_expt(b, n), 'Time: %s' % (timer_fast.timeit(),), sep='\n')


if __name__ == '__main__':
    run_the_magic()
