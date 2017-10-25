# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.35
"""
from operator import add

from Chapter2.hierarchical_structures import pair
from Chapter2.lisp_list_structured_data import lisp_list, cons, length
from Chapter2.sequences_as_conventional_interfaces import accumulate, enumerate_tree
from Chapter2.mapping_over_lists import map
from utils import let


def count_leaves(tree):
    return accumulate(
        lambda sub_tree, count: length(sub_tree) + count,
        0,
        map(enumerate_tree, tree)
    )


def count_leaves2(tree):
    return accumulate(
        add,
        0,
        map(
            lambda tree: count_leaves(tree) if pair(tree) else 1,
            tree
        )
    )


if __name__ == '__main__':
    with let(lisp_list(1, lisp_list(2, lisp_list(3, 4)), 5)) as (x,):
        print('(define x (list 1 (list 2 (list 3 4)) 5))')
        print('(count-leaves x)')
        print(count_leaves(x))
        print('(count-leaves (list x x))')
        print(count_leaves(lisp_list(x, x)))
