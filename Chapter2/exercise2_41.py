# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.41
"""
from operator import add

from Chapter2.lisp_list_structured_data import caddr, cadr, car, lisp_list, print_lisp_list
from Chapter2.mapping_over_lists import map
from Chapter2.nested_mappings import flatmap, unique_pairs
from Chapter2.sequences_as_conventional_interfaces import enumerate_interval, filter


def ordered_triples_sum_equals(n, s):
    """find all ordered triples of distinct positive integers i, j, and k less than or equal to a given integer n that
    sum to a given integer s.
    """
    return filter(
        lambda triple: triple_sum_equals(triple, s),
        unique_triples(n)
    )


def triple_sum_equals(triple, number):
    """Test if the sum of elements of the triple equals to number"""
    return add(car(triple), add(cadr(triple), caddr(triple))) == number


def unique_triples(n):
    return flatmap(
        lambda i: map(
            lambda pair: lisp_list(i, car(pair), cadr(pair)),
            unique_pairs(i - 1)
        ),
        enumerate_interval(1, n)
    )


def run_the_magic():
    n, s = 19, 50
    print('(unique-triples %(n)s)' % locals())
    print_lisp_list(unique_triples(n))
    print('(triples-sum-equals %(n)s, %(s)s)' % locals())
    print_lisp_list(ordered_triples_sum_equals(n, s))


if __name__ == "__main__":
    run_the_magic()
