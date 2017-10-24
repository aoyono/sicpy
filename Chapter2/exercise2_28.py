# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.28
"""
from Chapter2.hierarchical_structures import pair
from Chapter2.lisp_list_structured_data import append, car, cdr, lisp_list
from utils import let


def fringe(x):
    def iterate(items, acc):
        if items is None:
            return acc
        with let(car(items), cdr(items)) as (head, tail):
            if pair(head):
                return iterate(
                    tail,
                    append(acc, fringe(head))
                )
            return iterate(
                tail,
                append(acc, lisp_list(head))
            )

    return iterate(x, lisp_list())


if __name__ == '__main__':
    with let(lisp_list(lisp_list(1, 2), lisp_list(3, 4))) as (x,):
        print(fringe(x))
        print(fringe(lisp_list(x, x)))
