# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.21
"""
from Chapter1.compound_procedures import square
from Chapter2.lisp_list_structured_data import car, cdr, cons, lisp_list
from Chapter2.mapping_over_lists import map


def square_list(items):
    if items is None:
        return None
    return cons(
        square(car(items)),
        square_list(cdr(items))
    )


def square_list_map(items):
    return map(
        square,
        items
    )


if __name__ == '__main__':
    print('(square-list (list 1 2 3 4))')
    print(square_list(lisp_list(1, 2, 3, 4)))
    print('(square-list (list 1 2 3 4))')
    print(square_list_map(lisp_list(1, 2, 3, 4)))
