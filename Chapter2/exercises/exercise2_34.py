# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.34
"""
from Chapter2.themes.lisp_list_structured_data import lisp_list
from Chapter2.sequences_as_conventional_interfaces import accumulate


def horner_eval(x, coefficient_sequence):
    return accumulate(
        lambda this_coeff, higher_term: this_coeff + x * higher_term,
        0,
        coefficient_sequence
    )


def run_the_magic():
    print('(horner-eval 2 (list 1 3 0 5 0 1))')
    print(horner_eval(2, lisp_list(1, 3, 0, 5, 0, 1)))


if __name__ == '__main__':
    run_the_magic()
