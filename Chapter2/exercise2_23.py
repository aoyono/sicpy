# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.23
"""
from Chapter2.lisp_list_structured_data import car, cdr, length, lisp_list
from utils import let


def for_each(func, items):
    if items is None:
        return None
    with let(func(car(items))):
        for_each(func, cdr(items))


if __name__ == '__main__':
    print('(for-each (lambda (x) (newline) (display x)) (list 57 321 88))')
    for_each(lambda x: print(x), lisp_list(57, 321, 88))
