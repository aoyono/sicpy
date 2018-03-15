# -*- coding: utf-8 -*-
"""
"""
from operator import add

from Chapter1.tfp_searching_for_divisors import is_prime
from Chapter2.lisp_list_structured_data import append, cadr, car, cons, lisp_list, nil, print_lisp_list
from Chapter2.mapping_over_lists import map
from Chapter2.sequences_as_conventional_interfaces import accumulate, enumerate_interval, filter


def flatmap(proc, seq):
    return accumulate(append, nil, map(proc, seq))


def sum_is_prime(pair):
    return is_prime(add(car(pair), cadr(pair)))


def make_pair_sum(pair):
    return lisp_list(
        car(pair),
        cadr(pair),
        add(car(pair), cadr(pair))
    )


def prime_sum_pairs(n):
    """Generate the sequence of all ordered pairs of positive integers less than or equal to n whom sum is prime"""
    return map(
        make_pair_sum,
        filter(sum_is_prime, unique_pairs(n))
    )


def unique_pairs(n):
    """Generate the sequence of pairs of ordered positive integers (from exercise 2.40"""
    return flatmap(
        lambda i: map(
            lambda j: lisp_list(i, j),
            enumerate_interval(1, i - 1)
        ),
        enumerate_interval(1, n)
    )


def permutations(s):
    """Compute all the permutations of a set S.
    Note: In Python (which may not be optimised for tail-recursion), this function works up to a set of 6 elements. From
    7 elements, it raises a RecursionError
    """
    if s is nil:  # If the set is empty
        return lisp_list(nil)  # Return the sequence containing empty set
    return flatmap(
        lambda x: map(
            lambda p: cons(x, p),
            permutations(
                remove(x, s)
            )
        ),
        s
    )


def remove(item, sequence):
    return filter(
        lambda x: not x == item,
        sequence
    )


def run_the_magic():
    # Generate the sequence of all ordered pairs of positive integers less than or equal to n
    n = 6
    print('(prime-sum-pairs %(n)s)' % locals())
    print_lisp_list(prime_sum_pairs(n))
    print('(permutations (list 1 2 3))')
    print_lisp_list(permutations(lisp_list(1, 2, 3, 4, 5, 6)))
    print('(unique-pairs %(n)s)' % locals())
    print_lisp_list(unique_pairs(n))


if __name__ == '__main__':
    run_the_magic()
