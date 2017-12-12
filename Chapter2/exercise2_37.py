# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.37
"""
from operator import add, mul

from Chapter2.exercise2_36 import accumulate_n
from Chapter2.lisp_list_structured_data import cons, lisp_list, print_lisp_list
from Chapter2.sequences_as_conventional_interfaces import accumulate, map
from utils import let


def map_n(op, init, *seqs):
    return map(
        lambda l: accumulate(op, init, l),
        accumulate_n(
            cons,
            lisp_list(),
            lisp_list(*seqs)
        )
    )


def dot_product(v, w):
    return accumulate(
        add,
        0,
        map_n(mul, 1, v, w)
    )


def matrix_dot_vector(m, v):
    return map(
        lambda row: dot_product(v, row),
        m
    )


def transpose(mat):
    return accumulate_n(
        cons,
        lisp_list(),
        mat
    )


def matrix_dot_matrix(m, n):
    with let(transpose(n)) as (cols,):
        return map(
            lambda row: matrix_dot_vector(cols, row),
            m
        )


def run_the_magic():
    with let(
            lisp_list(
                lisp_list(1, 2, 3),
                lisp_list(4, 5, 6),
                lisp_list(6, 7, 8),
            ),
            lisp_list(
                lisp_list(1, 0, 0),
                lisp_list(0, 8, 0),
                lisp_list(0, 0, 1),
            )
    ) as (m, n):
        print('(define m (list (list 1 2 3) (list 4 5 6) (list 6 7 8))')
        print_lisp_list(m)
        print('(define n (list (list 1 0 0) (list 0 1 0) (list 0 0 1))')
        print_lisp_list(n)
        print('(matrix-*-matrix m n)')
        print_lisp_list(matrix_dot_matrix(m, n))


if __name__ == '__main__':
    run_the_magic()
