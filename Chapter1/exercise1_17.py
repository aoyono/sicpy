# -*- coding: utf-8 -*-
"""
The exponentiation algorithms in this section are based on performing exponentiation by means of repeated
multiplication. In a similar way, one can perform integer multiplication by means of repeated addition. The following
multiplication procedure (in which it is assumed that our language can only add, not multiply) is analogous to the expt
procedure:

(define (* a b)
  (if (= b 0)
      0
      (+ a (* a (- b 1)))))

This algorithm takes a number of steps that is linear in b. Now suppose we include, together with addition, operations
double, which doubles an integer, and halve, which divides an (even) integer by 2. Using these, design a multiplication
procedure analogous to fast-expt that uses a logarithmic number of steps.
"""
from operator import add, sub, mul, truediv, eq

from Chapter1.exponentiation import is_even


def multiply(a, b):
    if b == 0:
        return 0
    return add(a, multiply(a, sub(b, 1)))


def double(a): return mul(2, a)


def halve(a): return truediv(a, 2)


def fast_multiply(a, b):
    if eq(b, 0):
        return 0
    if is_even(b):
        return double(
            fast_multiply(a, halve(b))
        )
    return add(a, fast_multiply(a, sub(b, 1)))


if __name__ == '__main__':
    from timeit import Timer
    b, n = 1000, 831
    timer = Timer(stmt='multiply(%(b)s, %(n)s)' % locals(), setup='from __main__ import multiply')
    print('(* %(b)s %(n)s)' % locals(), multiply(b, n), 'Time: %s' % (timer.timeit(),), sep='\n')

    timer = Timer(stmt='fast_multiply(%(b)s, %(n)s)' % locals(), setup='from __main__ import fast_multiply')
    print('(fast-multiply %(b)s %(n)s)' % locals(), fast_multiply(b, n), 'Time: %s' % (timer.timeit(),), sep='\n')
