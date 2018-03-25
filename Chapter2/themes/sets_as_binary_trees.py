# -*- coding: utf-8 -*-
from Chapter2.themes.hierarchical_structures import pair
from Chapter2.themes.lisp_list_structured_data import (
    caddr, cadr, car,
    lisp_list, nil, print_lisp_list,
)


# Building data abstraction of a tree
def entry(tree):
    """Returns the tip of the tree"""
    if pair(tree):
        return car(tree)
    return tree


def left_branch(tree):
    """Returns the left branch of the tree"""
    return cadr(tree)


def right_branch(tree):
    """Returns the right branch of the tree"""
    return caddr(tree)


def make_tree(entry, left, right):
    """Builds a tree from its tip, the left and the right branches"""
    return lisp_list(entry, left, right)


# End of data abstraction


def element_of_set(x, set):
    """Checks if x is an element of set"""
    if set is nil:
        return False
    if x == entry(set):
        return True
    if x < entry(set):
        return element_of_set(x, left_branch(set))
    if x > entry(set):
        return element_of_set(x, right_branch(set))


def adjoin_set(x, set):
    """Adds x to set"""
    if set is nil:
        return make_tree(x, nil, nil)
    if x == entry(set):
        return set
    if x < entry(set):
        return make_tree(entry(set), adjoin_set(x, left_branch(set)),
                         right_branch(set))
    if x > entry(set):
        return make_tree(entry(set), left_branch(set),
                         adjoin_set(x, right_branch(set)))


def run_the_magic():
    s = make_tree(
        1,
        make_tree(-1, -2, 0),
        make_tree(5, 3, 9)
    )
    s1 = make_tree(
        7,
        make_tree(3, 1, 5),
        make_tree(9, nil, 11)
    )
    s2 = make_tree(
        3,
        1,
        make_tree(
            7,
            5,
            make_tree(9, nil, 11)
        )
    )
    s3 = make_tree(
        5,
        make_tree(3, 1, nil),
        make_tree(9, 7, 11)
    )
    print(element_of_set(-1, s))
    print_lisp_list(adjoin_set(5, s))
    print_lisp_list(adjoin_set(6, s))
    print_lisp_list(s1)
    print_lisp_list(s2)
    print_lisp_list(s3)


if __name__ == "__main__":
    run_the_magic()
