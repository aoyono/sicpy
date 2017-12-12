# -*- coding: utf-8 -*-
"""
Use the smallest-divisor procedure to find the smallest divisor of each of the following numbers: 199, 1999, 19999.
"""
from Chapter1.tfp_searching_for_divisors import smallest_divisor


def run_the_magic():
    for n in (199, 1999, 19999):
        print(
            '(smallest-divisor %(n)s)' % locals(),
            smallest_divisor(n),
            sep='\n',
        )


if __name__ == '__main__':
    run_the_magic()
