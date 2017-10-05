# -*- coding: utf-8 -*-
"""
Simpson's Rule is a more accurate method of numerical integration than the method illustrated above. Using Simpson's
Rule, the integral of a function f between a and b is approximated as

 h
--- [y_0 + 4·y_1 + 2·y_2 + 4·y_3 + 2·y_4 + ... + 2·y_n-2 + 4·y_n-1 + y_n]
 3


where h = (b - a)/n, for some even integer n, and y_k = f(a + kh). (Increasing n increases the accuracy of the
approximation.) Define a procedure that takes as arguments f, a, b, and n and returns the value of the integral,
computed using Simpson's Rule. Use your procedure to integrate cube between 0 and 1 (with n = 100 and n = 1000), and
compare the results to those of the integral procedure shown above.
"""
from operator import truediv, sub, add, mul, eq, mod

from Chapter1.procedure_as_arguments import generic_sum
from Chapter1.exercise1_9 import inc
from Chapter1.exercice1_8 import cube


def integral_simpson(f, a, b, n):
    def h(): return truediv(
        sub(b, a),
        n
    )

    def simpson_term(k):
        if eq(k, 0):
            return f(a)
        if eq(k, n):
            return f(b)
        if eq(mod(k, 2), 0):
            return mul(
                2,
                f(add(
                    a,
                    mul(k, h())
                ))
            )
        return mul(
            4,
            f(add(
                a,
                mul(k, h())
            ))
        )

    return mul(
        generic_sum(
            simpson_term,
            0,
            inc,
            n
        ),
        truediv(h(), 3.0)
    )


if __name__ == '__main__':
    a, b = 0, 1
    for n in (100, 1000):
        try:
            print(
                '(integral-simpson cube %(a)s %(b)s %(n)s)' % locals(),
                integral_simpson(cube, a, b, n),
                sep='\n'
            )
        except RecursionError:
            print('Recursion error for n = %(n)s' % locals())
