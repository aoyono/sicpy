# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.26
"""
from Chapter2.lisp_list_structured_data import append, cons, lisp_list
from utils import let

if __name__ == '__main__':
    with let(lisp_list(1, 2, 3), lisp_list(4, 5, 6)) as (x, y):
        print(append(x, y))
        print(cons(x, y))
        print(lisp_list(x, y))
