# -*- coding: utf-8 -*-
"""
"""
from operator import add

from Chapter2.lisp_list_structured_data import car, cdr, cons, lisp_list, length
from utils import let


def count_leaves(x):
    if x is None:
        return 0
    if not pair(x):
        return 1
    return add(
        count_leaves(car(x)),
        count_leaves(cdr(x))
    )


def pair(x):
    """Simulates Scheme primitive predicate pair? to determine whether a variable is a pair or not"""
    return isinstance(x, tuple)


def run_the_magic():
    with let(cons(lisp_list(1, 2), lisp_list(3, 4))) as (x,):
        print('(length x)')
        print(length(x))
        print('(count-leaves x)')
        print(count_leaves(x))
        print('(list x x)')
        print(lisp_list(x, x))
        print('(length (list x x))')
        print(length(lisp_list(x, x)))
        print('(count-leaves (list x x))')
        print(count_leaves(lisp_list(x, x)))


if __name__ == '__main__':
    run_the_magic()
