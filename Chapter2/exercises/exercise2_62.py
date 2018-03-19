# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.62
"""
from Chapter2.exercises.exercise2_28 import fringe
from Chapter2.exercises.exercise2_61 import adjoin_set
from Chapter2.themes.lisp_list_structured_data import lisp_list, print_lisp_list
from Chapter2.themes.sequences_as_conventional_interfaces import accumulate


def union_set(set1, set2):
    """Computes the union of set1 and set2 in O(n)"""
    return accumulate(adjoin_set, set1, set2)


def run_the_magic():
    s1 = lisp_list(1, 2, 3, 6, 10, 45, 56, 77, 90, 110, 120, 140, 150)
    s2 = lisp_list(1, 5, 26, 121)
    print_lisp_list(union_set(s1, s2))

    from timeit import Timer
    t1 = Timer(stmt='union_set(%(s1)s, %(s2)s)' % locals(),
               setup='from Chapter2.exercises.exercise2_62 import union_set')
    t2 = Timer(stmt='union_set(%(s1)s, %(s2)s)' % locals(),
               setup='from Chapter2.exercises.exercise2_59 import union_set')

    time = t1.timeit()
    print('average time (ordered list): %s' % time)

    time = t2.timeit()
    print('average_time (unordered list): %s' % time)


if __name__ == "__main__":
    run_the_magic()
