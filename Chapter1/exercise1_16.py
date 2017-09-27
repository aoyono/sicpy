# -*- coding: utf-8 -*-
"""
Design a procedure that evolves an iterative exponentiation process that uses successive squaring and uses a logarithmic
number of steps, as does fast-expt. (Hint: Using the observation that (b^n/2)^2 = (b^2)^n/2, keep, along with
the exponent n and the base b, an additional state variable a, and define the state transformation in such a way that
the product ab^n is unchanged from state to state. At the beginning of the process a is taken to be 1, and the answer
is given by the value of a at the end of the process. In general, the technique of defining an invariant quantity that
remains unchanged from state to state is a powerful way to think about the design of iterative algorithms.)
"""
from operator import eq, sub, mul, truediv

from Chapter1.compound_procedures import square
from Chapter1.exponentiation import is_even


def expt(b, n):
    """Thanks to https://github.com/qiao/sicp-solutions/blob/master/chapter1/1.16.scm"""
    def expt_iter(base, counter, a):
        if eq(counter, 0):
            return a
        if is_even(counter):
            return expt_iter(
                square(base),
                truediv(counter, 2),
                a
            )
        return expt_iter(
            base,
            sub(counter, 1),
            mul(base, a)
        )
    return expt_iter(b, n, 1)


if __name__ == '__main__':
    from timeit import Timer
    b, n = 2, 20000
    timer = Timer(stmt='expt(%(b)s, %(n)s)' % locals(), setup='from __main__ import expt')
    print('(expt %(b)s %(n)s)' % locals(), expt(b, n), 'Time: %s' % (timer.timeit(),), sep='\n')

    from Chapter1.exponentiation import fast_expt
    timer = Timer(stmt='fast_expt(%(b)s, %(n)s)' % locals(), setup='from Chapter1.exponentiation import fast_expt')
    print('(fast-expt %(b)s %(n)s)' % locals(), fast_expt(b, n), 'Time: %s' % (timer.timeit(),), sep='\n')
