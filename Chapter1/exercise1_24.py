# -*- coding: utf-8 -*-
"""
Modify the timed-prime-test procedure of exercise 1.22 to use fast-prime? (the Fermat method), and test each of the 12
primes you found in that exercise. Since the Fermat test has (log n) growth, how would you expect the time to test
primes near 1,000,000 to compare with the time needed to test primes near 1000? Do your data bear this out? Can you
explain any discrepancy you find?
"""
from operator import add, le, sub

from Chapter1.exercise1_22 import report_prime, runtime
from Chapter1.exponentiation import is_even
from Chapter1.tfp_the_fermat_test import is_prime_fast

times = 20


def timed_prime_test(n):
    print()
    print(n)
    start_prime_test(n, runtime())


def start_prime_test(n, start_time):
    if is_prime_fast(n, times):
        report_prime(
            sub(runtime(), start_time)
        )


def search_for_primes(a, b):
    def process(k):
        if le(k, b):
            timed_prime_test(k)
            return process(add(k, 2))

    process(
        add(a, 1) if is_even(a)
        else
        a
    )


if __name__ == '__main__':
    for a in (1009, 1013, 1019, 10007, 10009, 10037, 100003, 100019, 100043, 1000003, 1000033, 1000037):
        search_for_primes(a, a + 1)
