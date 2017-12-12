# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.25
"""
from Chapter2.lisp_list_structured_data import car, cdr, lisp_list
from utils import let

def run_the_magic():
    with let(lisp_list(1, 3, lisp_list(5, 7), 9), lisp_list(lisp_list(7)),
             lisp_list(1, lisp_list(2, lisp_list(3, lisp_list(4, lisp_list(5, lisp_list(6, 7))))))) as (x, y, z):
        assert 7 == car(cdr(car(cdr(cdr(x)))))
        assert 7 == car(car(y))
        assert 7 == car(cdr(car(cdr(car(cdr(car(cdr(car(cdr(car(cdr(z))))))))))))


if __name__ == '__main__':
    run_the_magic()
