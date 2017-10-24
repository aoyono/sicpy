# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.24
"""
from Chapter2.lisp_list_structured_data import length, lisp_list
from utils import let

if __name__ == '__main__':
    with let(lisp_list(1, lisp_list(2, lisp_list(3, 4)))) as (x,):
        print(x)
        print(length(x))

    """
                 (1 (2 (3 4)))
                        ·
                       / \
                      1   ·
                         / \
                        2   ·
                           / \
                          3   4
    """
