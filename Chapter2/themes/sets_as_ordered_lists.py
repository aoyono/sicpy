# -*- coding: utf-8 -*-
from Chapter2.themes.lisp_list_structured_data import car, cdr, cons, nil
from utils import let


def element_of_set(x, set):
    """Tests if element x is in set"""
    if set is nil:
        return False
    if car(set) == x:
        return True
    if car(set) > x:
        return False
    return element_of_set(x, cdr(set))


def intersection_set(set1, set2):
    """Computes the intersection of set1 and set2"""
    if set1 is nil or set2 is nil:
        return nil
    with let(car(set1), car(set2)) as (x1, x2):
        if x1 == x2:
            return cons(car(set1), intersection_set(cdr(set1), cdr(set2)))
        if x1 < x2:
            return intersection_set(cdr(set1), set2)
        if x1 > x2:
            return intersection_set(set1, cdr(set2))


# Enable importing some procedures defined in exercises as originating from the theme
from Chapter2.exercises.exercise2_61 import adjoin_set
from Chapter2.exercises.exercise2_62 import union_set
