# -*- coding: utf-8 -*-
"""
Alyssa P. Hacker complains that we went to a lot of extra work in writing expmod. After all, she says, since we already
know how to compute exponentials, we could have simply written

(define (expmod base exp m)
  (remainder (fast-expt base exp) m))

Is she correct? Would this procedure serve as well for our fast prime tester? Explain.
"""
import random
from operator import eq, mod, sub

from Chapter1.exponentiation import fast_expt


def expmod(base, exp, m):
    return mod(
        fast_expt(base, exp),
        m
    )


def fermat_test(n):

    def try_it(a):
        return eq(
            expmod(a, n, n),
            a
        )

    return try_it(
        random.randint(1, sub(n, 1))
    )


def is_prime_fast(n, times):
    # print('%(times)s times left' % locals())
    if eq(times, 0):
        return True
    if fermat_test(n):
        return is_prime_fast(
            n,
            sub(times, 1)
        )
    return False


if __name__ == '__main__':
    n, times = 139, 10
    for n in (1009, 1013, 1019, 10007, 10009, 10037, 100003, 100019, 100043, 1000003, 1000033, 1000037):
        print(
            '(fast-prime? %(n)s %(times)s)' % locals(),
            is_prime_fast(n, times),
            sep='\n',
        )

    from Chapter1.tfp_the_fermat_test import is_prime_fast
    for n in (1009, 1013, 1019, 10007, 10009, 10037, 100003, 100019, 100043, 1000003, 1000033, 1000037):
        print(
            '(fast-prime? %(n)s %(times)s)' % locals(),
            is_prime_fast(n, times),
            sep='\n',
        )
