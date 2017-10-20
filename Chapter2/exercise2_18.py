# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.18
"""
from Chapter2.lisp_list_structured_data import car, cdr, cons, lisp_list


def reverse(l):
    def iterate(items, acc):
        if items is None:
            return acc
        return iterate(cdr(items), cons(car(items), acc))

    return iterate(l, lisp_list())


if __name__ == '__main__':
    print(lisp_list(1, 4, 9, 16, 25))
    print(reverse(lisp_list(1, 4, 9, 16, 25)))
