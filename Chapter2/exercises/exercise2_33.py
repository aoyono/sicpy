# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.33
"""
from Chapter1.exercises.exercise1_9 import inc
from Chapter2.themes.lisp_list_structured_data import cons, lisp_list, print_lisp_list
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


def run_the_magic():
    print_lisp_list(map(
        lambda x: x * 10,
        lisp_list(1, 2, 3, 4, 5)
    ))
    print_lisp_list(append(lisp_list(1, 2, 3, 4, 5), lisp_list(1, 2, 3, 4, 5)))
    print(length(lisp_list(1, 2, 3, 4, 5)))


if __name__ == '__main__':
    run_the_magic()
