# -*- coding: utf-8 -*-
"""Representing sets as unordered lists"""
from Chapter2.themes.lisp_list_structured_data import car, cdr, cons, nil, lisp_list, print_lisp_list


def element_of_set(x, set):
    """Test if an item x is element of set"""
    if set is nil:
        return False
    if x == car(set):
        return True
    return element_of_set(x, cdr(set))


def adjoin_set(x, set):
    """Add x to the elements of set"""
    if element_of_set(x, set):
        return set
    return cons(x, set)


def intersection_set(set1, set2):
    """Compute the intersection of set1 with set2"""
    if set1 is nil or set2 is nil:
        return nil
    if element_of_set(car(set1), set2):
        return cons(car(set1), intersection_set(cdr(set1), set2))
    return intersection_set(cdr(set1), set2)


def run_the_magic():
    s1 = lisp_list(1, 2, 3)
    s2 = lisp_list(4, 3, 6)
    print(element_of_set(2, s1))
    print(element_of_set(2, s2))
    print_lisp_list(adjoin_set(5, s1))
    print_lisp_list(adjoin_set(3, s1))
    print_lisp_list(intersection_set(s1, s2))
    print_lisp_list(intersection_set(nil, s2))


if __name__ == '__main__':
    run_the_magic()

