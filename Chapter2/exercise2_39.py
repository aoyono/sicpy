# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.39
"""
from Chapter2.exercise2_38 import fold_left
from Chapter2.lisp_list_structured_data import cons, lisp_list, nil, print_lisp_list
from Chapter2.sequences_as_conventional_interfaces import accumulate as fold_right


def reverse1(sequence):
    return fold_right(
        lambda x, y: lisp_list(y, x),
        nil,
        sequence
    )


def reverse2(sequence):
    return fold_left(
        lambda x, y: lisp_list(y, x),
        nil,
        sequence
    )


def run_the_magic():
    print('(reverse-fr (list 1 2 3))')
    print_lisp_list(reverse1(lisp_list(1, 2, 3)))
    print('(reverse-fl (list 1 2 3))')
    print_lisp_list(reverse2(lisp_list(1, 2, 3)))


if __name__ == "__main__":
    run_the_magic()
