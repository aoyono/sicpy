# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.17
"""
from Chapter2.lisp_list_structured_data import car, cdr, lisp_list


def last_pair(l):
    if cdr(l) is None:
        return car(l),  # Simulates the fact that we don't really include None in a pair
    return last_pair(cdr(l))


if __name__ == '__main__':
    print('(last-pair (list 23 72 149 34))')
    print(
        last_pair(
            lisp_list(23, 72, 149, 34)
        )
    )
