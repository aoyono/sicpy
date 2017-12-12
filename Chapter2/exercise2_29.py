# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.29
"""

from Chapter2.hierarchical_structures import pair
from Chapter2.lisp_list_structured_data import car, cdr, lisp_list
from utils import let


# Mobile system
def make_mobile(left, right):
    return lisp_list(left, right)


def left_branch(mobile):
    return car(mobile)


def right_branch(mobile):
    return car(cdr(mobile))


# Branch system
def make_branch(length, structure):
    return lisp_list(length, structure)


def branch_length(branch):
    return car(branch)


def branch_structure(branch):
    return car(cdr(branch))


# Mobile and Branch systems User methods
def total_weight(mobile):
    with let(left_branch(mobile), right_branch(mobile)) as (lb, rb):
        return branch_weight(lb) + branch_weight(rb)


def is_balanced(mobile):
    with let(left_branch(mobile), right_branch(mobile)) as (left, right):
        with let(branch_structure(left), branch_structure(right)) as (left_structure, right_structure):
            if is_mobile(left_structure) and is_mobile(right_structure):
                return is_balanced(left_structure) and is_balanced(right_structure)
            return torque(left) == torque(right)


def torque(branch):
    with let(branch_structure(branch)) as (structure,):
        if is_mobile(structure):
            return total_weight(structure) * branch_length(branch)
        return structure * branch_length(branch)


def is_mobile(structure):
    """Simulates if a predicate for determining if a branch structure is a mobile"""
    return pair(structure)


def branch_weight(branch):
    with let(branch_structure(branch)) as (bs,):
        if is_mobile(bs):
            return total_weight(bs)
        return bs


def run_the_magic():
    m1 = make_mobile(
        make_branch(4, 2),
        make_branch(4, 2)
    )

    m2 = make_mobile(
        make_branch(1, 4),
        make_branch(1, m1)
    )

    print('(total-weight m1)')
    print(total_weight(m1))
    print('(total-weight m2)')
    print(total_weight(m2))

    print('(is-balanced m1)')
    print(is_balanced(m1))
    print('(is-balanced m2)')
    print(is_balanced(m2))


if __name__ == '__main__':
    run_the_magic()
