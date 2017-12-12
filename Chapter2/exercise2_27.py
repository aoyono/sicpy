# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.27
"""
from Chapter2.exercise2_18 import reverse
from Chapter2.hierarchical_structures import pair
from Chapter2.lisp_list_structured_data import append, car, cdr, lisp_list
from utils import let


def deep_reverse(x):
    def iterate(items, acc):
        if items is None:
            return acc
        with let(car(items), cdr(items)) as (head, tail):
            if pair(head):
                return iterate(
                    tail,
                    append(lisp_list(deep_reverse(head)), acc)
                )
            return iterate(
                tail,
                append(lisp_list(head), acc)
            )

    return iterate(x, lisp_list())


def run_the_magic():
    with let(lisp_list(lisp_list(1, 2), lisp_list(3, 4))) as (x,):
        print(x)
        print(reverse(x))
        print(deep_reverse(x))


if __name__ == '__main__':
    run_the_magic()
