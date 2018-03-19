# -*- coding: utf-8 -*-
"""
"""
from operator import add, mul

from Chapter1.themes.compound_procedures import square
from Chapter1.exercises.exercise1_19 import fib
from Chapter2.themes.hierarchical_structures import pair
from Chapter2.themes.lisp_list_structured_data import append, car, cdr, cons, lisp_list, nil, print_lisp_list
from Chapter2.themes.mapping_over_lists import map
from utils import let


def sum_odd_squares(tree):
    if tree is nil:
        return 0
    if not pair(tree):
        if odd(tree):
            return square(tree)
        return 0
    return add(
        sum_odd_squares(car(tree)),
        sum_odd_squares(cdr(tree))
    )


def odd(integer): return not even(integer)


def even(integer): return integer % 2 == 0


def even_fibs(n):
    def next(k):
        if k > n:
            return lisp_list()
        with let(fib(k)) as (f,):
            if even(f):
                return cons(
                    f,
                    next(k + 1)
                )
            return next(k + 1)

    return next(0)


def filter(predicate, sequence):
    if sequence is nil:
        return lisp_list()
    if predicate(car(sequence)):
        return cons(
            car(sequence),
            filter(
                predicate,
                cdr(sequence)
            )
        )
    return filter(
        predicate,
        cdr(sequence)
    )


def accumulate(op, initial, sequence):
    if sequence is nil:
        return initial
    return op(
        car(sequence),
        accumulate(
            op,
            initial,
            cdr(sequence)
        )
    )


def enumerate_interval(low, high):
    if low > high:
        return lisp_list()
    return cons(
        low,
        enumerate_interval(
            low + 1,
            high
        )
    )


def enumerate_tree(tree):
    if tree is nil:
        return lisp_list()
    if not pair(tree):
        return lisp_list(tree)
    return append(
        enumerate_tree(car(tree)),
        enumerate_tree(cdr(tree))
    )


def sum_odd_squares_signal_flow(tree):
    return accumulate(
        add,
        0,
        map(
            square,
            filter(
                odd,
                enumerate_tree(tree)
            )
        )
    )


def even_fibs_signal_flow(n):
    return accumulate(
        cons,
        lisp_list(),
        filter(
            even,
            map(
                fib,
                enumerate_interval(0, n)
            )
        )
    )


def list_fib_squares(n):
    return accumulate(
        cons,
        lisp_list(),
        map(
            square,
            map(
                fib,
                enumerate_interval(0, n)
            )
        )
    )


def product_of_squares_of_odd_elements(sequence):
    return accumulate(
        mul,
        1,
        map(
            square,
            filter(
                odd,
                sequence
            )
        )
    )


def run_the_magic():
    print('(filter odd? (list 1 2 3 4 5))')
    print_lisp_list(filter(odd, lisp_list(1, 2, 3, 4, 5)))
    print('(accumulate + 0 (list 1 2 3 4 5))')
    print(accumulate(add, 0, lisp_list(1, 2, 3, 4, 5)))
    print('(accumulate * 1 (list 1 2 3 4 5))')
    print(accumulate(mul, 1, lisp_list(1, 2, 3, 4, 5)))
    print('(accumulate cons nil (list 1 2 3 4 5))')
    print_lisp_list(accumulate(cons, lisp_list(), lisp_list(1, 2, 3, 4, 5)))
    print('(enumerate-interval 2 7)')
    print_lisp_list(enumerate_interval(2, 7))
    print('(enumerate-tree (list 1 (list 2 (list 3 4)) 5))')
    print_lisp_list(enumerate_tree(lisp_list(
        1,
        lisp_list(
            2,
            lisp_list(
                3,
                4
            ),
            5
        )
    )))
    print('(list-fib-squares 10)')
    print_lisp_list(list_fib_squares(10))
    print('(product-of-squares-of-odd-elements (list 1 2 3 4 5))')
    print(product_of_squares_of_odd_elements(
        lisp_list(1, 2, 3, 4, 5)
    ))


if __name__ == '__main__':
    run_the_magic()
