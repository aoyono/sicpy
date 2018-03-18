# -*- coding: utf-8 -*-
"""
"""
from operator import gt, eq, mod, add

from Chapter1.themes.compound_procedures import square


def divides(a, b):
    return eq(mod(b, a), 0)


def smallest_divisor(n):
    def find_divisor(n, test_divisor):
        if gt(square(test_divisor), n):
            return n
        if divides(test_divisor, n):
            return test_divisor
        return find_divisor(
            n,
            add(test_divisor, 1)
        )
    return find_divisor(n, 2)


def is_prime(n):
    return eq(n, smallest_divisor(n))


def run_the_magic():
    n = 17
    print(
        '(prime? %(n)s)' % locals(),
        is_prime(n),
        sep='\n',
    )


if __name__ == '__main__':
    run_the_magic()
