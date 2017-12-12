# -*- coding: utf-8 -*-
"""
You can obtain an even more general version of accumulate (exercise 1.32) by introducing the notion of a filter on the
terms to be combined. That is, combine only those terms derived from values in the range that satisfy a specified
condition. The resulting filtered-accumulate abstraction takes the same arguments as accumulate, together with an
additional predicate of one argument that specifies the filter. Write filtered-accumulate as a procedure. Show how to
express the following using filtered-accumulate:

a. the sum of the squares of the prime numbers in the interval a to b (assuming that you have a prime? predicate already
written)

b. the product of all the positive integers less than n that are relatively prime to n (i.e., all positive
integers i < n such that GCD(i,n) = 1).
"""
from operator import add, and_, eq, gt, lt, mul

from Chapter1.compound_procedures import square
from Chapter1.exercise1_9 import inc
from Chapter1.great_common_divisor import gcd
from Chapter1.procedure_as_arguments import identity
from Chapter1.tfp_searching_for_divisors import is_prime


def filtered_accumulate_rec_it(combiner, null_value, term, a, next, b, filter_predicate):
    if gt(a, b):
        return null_value
    if filter_predicate(a):
        return combiner(
            term(a),
            filtered_accumulate(combiner, null_value, term, next(a), next, b, filter_predicate)
        )
    return filtered_accumulate_rec_it(combiner, null_value, term, next(a), next, b, filter_predicate)


def filtered_accumulate(combiner, null_value, term, a, next, b, filter_predicate):
    def iterate(a, result):
        if gt(a, b):
            return result
        if filter_predicate(a):
            return iterate(
                next(a),
                combiner(
                    result,
                    term(a)
                )
            )
        return iterate(
            next(a),
            result
        )

    return iterate(a, null_value)


# Applications

def sum_square_primes(a, b):
    return filtered_accumulate(add, 0, square, a, inc, b, is_prime)


def product_relatively_prime(n):
    def is_relatively_prime(k): return and_(
        lt(k, n),
        eq(gcd(k, n), 1)
    )

    return filtered_accumulate(mul, 1, identity, 1, inc, n, is_relatively_prime)


# Applications


def run_the_magic():
    a, b, n = 0, 2, 5
    print('(sum-square-primes %(a)s %(b)s)' % locals())
    print(sum_square_primes(a, b))
    print('(product-relative-primes %(n)s)' % locals())
    print(product_relatively_prime(n))


if __name__ == '__main__':
    run_the_magic()
