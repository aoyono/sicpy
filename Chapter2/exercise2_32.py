# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.32
"""
from Chapter2.lisp_list_structured_data import lisp_list, cdr, append, car, cons
from Chapter2.mapping_over_lists import map
from utils import let


def subsets(s):
    if s is None:
        return lisp_list()
    with let(subsets(cdr(s))) as (rest,):
        return append(
            rest,
            tuple((None,None)) if rest is None else
            map(
                lambda x: append(lisp_list(car(s)), x),
                rest
            )
        )

def run_the_magic():
    print(subsets(lisp_list(1, 2, 3)))


if __name__ == '__main__':
    run_the_magic()
