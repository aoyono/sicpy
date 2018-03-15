# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.36
"""
from operator import add

from Chapter2.lisp_list_structured_data import car, cdr, cons, lisp_list, nil, print_lisp_list
from Chapter2.mapping_over_lists import map
from Chapter2.sequences_as_conventional_interfaces import accumulate
from utils import let


def accumulate_n(op, init, seqs):
    if car(seqs) is nil:
        return lisp_list()
    return cons(
        accumulate(op, init, map(car, seqs)),
        accumulate_n(op, init, map(cdr, seqs))
    )


def run_the_magic():
    with let(lisp_list(lisp_list(1, 2, 3), lisp_list(4, 5, 6), lisp_list(7, 8, 9), lisp_list(10, 11, 12))) as (s,):
        print('(define s (list (list 1 2 3) (list 4 5 6) (list 7 8 9) (list 10 11 12)))')
        print_lisp_list(s)
        print('(accumulate-n + 0 s)')
        print_lisp_list(accumulate_n(add, 0, s))


if __name__ == '__main__':
    run_the_magic()
