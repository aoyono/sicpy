# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.17
"""
from Chapter2.themes.lisp_list_structured_data import car, cdr, lisp_list


def last_pair(l):
    if cdr(l) is None:
        return car(l),  # Simulates the fact that we don't really include None in a pair
    return last_pair(cdr(l))


def run_the_magic():
    print('(last-pair (list 23 72 149 34))')
    print(
        last_pair(
            lisp_list(23, 72, 149, 34)
        )
    )


if __name__ == '__main__':
    run_the_magic()
