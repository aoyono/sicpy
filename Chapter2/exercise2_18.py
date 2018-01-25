# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.18
"""
from Chapter2.lisp_list_structured_data import car, cdr, cons, lisp_list, print_lisp_list, nil


def reverse(l):
    def iterate(items, acc):
        if items is nil():
            return acc
        return iterate(cdr(items), cons(car(items), acc))

    return iterate(l, lisp_list())


def run_the_magic():
    print('(list 1 4 9 16 25)')
    print_lisp_list(lisp_list(1, 4, 9, 16, 25))
    print('(reverse (list 1 4 9 16 25))')
    print_lisp_list(reverse(lisp_list(1, 4, 9, 16, 25)))


if __name__ == '__main__':
    run_the_magic()
