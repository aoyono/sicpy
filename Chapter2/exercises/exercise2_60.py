# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.60
"""
from Chapter2.themes.lisp_list_structured_data import car, cdr, cons, lisp_list, nil, print_lisp_list
from Chapter2.themes.sequences_as_conventional_interfaces import accumulate


def element_of_set(x, set):
    """Tests if x is element of set with a representation of sets that allows duplicates"""
    if set is nil:
        return False
    if x == car(set):
        return True
    return element_of_set(x, cdr(set))


def adjoin_set(x, set):
    """Adds x to set"""
    return cons(x, set)


def union_set(set1, set2):
    """Computes union of set1 and set2"""
    return accumulate(adjoin_set, set2, set1)


def intersection_set(set1, set2):
    """Computes intersection of set1 and set2"""
    if set1 is nil or set2 is nil:
        return nil
    if element_of_set(car(set1), set2):
        return cons(car(set1), intersection_set(cdr(set1), set2))
    return intersection_set(cdr(set1), set2)


def run_the_magic():
    s1 = lisp_list(2, 3, 2, 1, 3, 2, 2)
    s2 = lisp_list(1, 1, 3)
    s3 = lisp_list(1, 2, 3)
    print(element_of_set(3, s1))
    print_lisp_list(adjoin_set(4, s1))
    print_lisp_list(intersection_set(s1, s2))
    print_lisp_list(union_set(s1, s2))

    from timeit import Timer

    t1_element_of = Timer(stmt='element_of_set(3, %(s1)s)' % locals(),
                          setup='from Chapter2.exercise2_60 import element_of_set')
    t2_element_of = Timer(stmt='element_of_set(3, %(s1)s)' % locals(),
                          setup='from Chapter2.sets_as_unordered_lists import element_of_set')

    t1_adjoin = Timer(stmt='adjoin_set(4, %(s1)s)' % locals(), setup='from Chapter2.exercise2_60 import adjoin_set')
    t2_adjoin = Timer(stmt='adjoin_set(4, %(s3)s)' % locals(),
                      setup='from Chapter2.sets_as_unordered_lists import adjoin_set')

    t1_intersection = Timer(stmt='intersection_set(%(s1)s, %(s2)s)' % locals(),
                            setup='from Chapter2.exercise2_60 import intersection_set')
    t2_intersection = Timer(stmt='intersection_set(%(s1)s, %(s3)s)' % locals(),
                            setup='from Chapter2.sets_as_unordered_lists import intersection_set')

    t1_union = Timer(stmt='union_set(%(s1)s, %(s2)s)' % locals(),
                     setup='from Chapter2.exercise2_60 import union_set')
    t2_union = Timer(stmt='union_set(%(s1)s, %(s2)s)' % locals(),
                     setup='from Chapter2.exercise2_59 import union_set')

    header = '-----------Timing for *%s* operation'

    def do_timing(timer1, timer2, op_name):
        print(header % op_name)
        t1 = timer1.timeit()
        t2 = timer2.timeit()
        print('-> With duplicate: %s' % t1)
        print('-> Without duplicate: %s' % t2)

    do_timing(t1_element_of, t2_element_of, 'element_of_set')
    do_timing(t1_adjoin, t2_adjoin, 'adjoin_set')
    do_timing(t2_intersection, t2_intersection, 'intersection_set')
    do_timing(t1_union, t2_union, 'union_set')

    print('The representation using unordered list with duplicates is better suited for applications where there are '
          'many insertions in the data structure')


if __name__ == "__main__":
    run_the_magic()
