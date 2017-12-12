# -*- coding: utf-8 -*-
"""
a.  The sum procedure is only the simplest of a vast number of similar abstractions that can be captured as higher-order
procedures.[51] Write an analogous procedure called product that returns the product of the values of a function at points
over a given range. Show how to define factorial in terms of product. Also use product to compute approximations to pi
using the formula[52]

 pi   2·4·4·6·6·8·....
--- = ----------------
 4    3·3·5·5·7·7·....

([51]:
The intent of exercises 1.31-1.33 is to demonstrate the expressive power that is attained by using an appropriate
abstraction to consolidate many seemingly disparate operations. However, though accumulation and filtering are elegant
ideas, our hands are somewhat tied in using them at this point since we do not yet have data structures to provide
suitable means of combination for these abstractions. We will return to these ideas in section 2.2.3 when we show how
to use sequences as interfaces for combining filters and accumulators to build even more powerful abstractions. We will
see there how these methods really come into their own as a powerful and elegant approach to designing programs.)

([52]:
This formula was discovered by the seventeenth-century English mathematician John Wallis.)


b.  If your product procedure generates a recursive process, write one that generates an iterative process. If it
generates an iterative process, write one that generates a recursive process.
"""
from operator import add, gt, mul, sub, truediv

from Chapter1.exercise1_9 import inc
from Chapter1.procedure_as_arguments import identity
from Chapter1.compound_procedures import square


def product(term, a, next, b):
    if gt(a, b):
        return 1
    return mul(
        term(a),
        product(
            term,
            next(a),
            next,
            b
        )
    )


def product_iterative(term, a, next, b):
    def iterate(a, result):
        if gt(a, b):
            return result
        return iterate(
            next(a),
            mul(
                result,
                term(a)
            )
        )

    return iterate(a, 1)


def factorial(n):
    return product_iterative(
        identity,
        1,
        inc,
        n
    )


def inv(x): return truediv(1, x)


def pi_wallis(n):
    def term(k): return sub(
        1,
        inv(square(inc(mul(2, k))))
    )

    return mul(
        4,
        product_iterative(term, 1, inc, n)
    )


def run_the_magic():
    n = 995
    print('(factorial {})'.format(n))
    print(factorial(n))
    print('(pi-wallis %(n)s)' % locals())
    print(pi_wallis(n))


if __name__ == '__main__':
    run_the_magic()
