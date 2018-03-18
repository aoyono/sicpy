# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.35
"""
from operator import add

from Chapter2.themes.hierarchical_structures import pair
from Chapter2.themes.lisp_list_structured_data import lisp_list, length
from Chapter2.sequences_as_conventional_interfaces import accumulate, enumerate_tree
from Chapter2.themes.mapping_over_lists import map
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


def run_the_magic():
    with let(lisp_list(1, lisp_list(2, lisp_list(3, 4)), 5)) as (x,):
        print('(define x (list 1 (list 2 (list 3 4)) 5))')
        print('(count-leaves x)')
        print(count_leaves(x))
        print('(count-leaves (list x x x x))')
        print(count_leaves(lisp_list(x, x, x, x)))

        import time
        start = time.time()
        count_leaves(x)
        el1 = time.time() - start
        print('First method elapsed time: %s' % (el1,))
        start = time.time()
        count_leaves2(x)
        el2 = time.time() - start
        print('Second method elapsed time: %s' % (el2,))

        print('rate:', el2/el1)

        from timeit import Timer
        cl1 = Timer(stmt='count_leaves(%(x)s)' % locals(), setup='from Chapter2.exercise2_35 import count_leaves')
        cl2 = Timer(stmt='count_leaves2(%(x)s)' % locals(), setup='from Chapter2.exercise2_35 import count_leaves2')
        t1 = cl1.timeit()
        t2 = cl2.timeit()
        print('timeit result first method: %s' % t1)
        print('timeit result second method: %s' % t2)

        print('rate:', t2 / t1)


if __name__ == '__main__':
    run_the_magic()
