# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.33
"""
from Chapter1.exercise1_9 import inc
from Chapter2.lisp_list_structured_data import cons, lisp_list
from Chapter2.sequences_as_conventional_interfaces import accumulate


def map(p, sequence):
    return accumulate(
        lambda x, y: cons(p(x), y),
        lisp_list(),
        sequence
    )


def append(seq1, seq2):
    return accumulate(
        cons,
        seq2,
        seq1
    )


def length(sequence):
    return accumulate(
        lambda x, y: inc(y),
        0,
        sequence
    )


if __name__ == '__main__':
    print(map(
        lambda x: x * 10,
        lisp_list(1, 2, 3, 4, 5)
    ))
    print(append(lisp_list(1, 2, 3, 4, 5), lisp_list(1, 2, 3, 4, 5)))
    print(length(lisp_list(1, 2, 3, 4, 5)))
