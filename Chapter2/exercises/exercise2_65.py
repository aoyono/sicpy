# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.65
"""
from Chapter2.exercises.exercise2_63 import tree_to_list_2
from Chapter2.exercises.exercise2_64 import list_to_tree
from Chapter2.themes import sets_as_ordered_lists
from Chapter2.themes.lisp_list_structured_data import (nil, print_lisp_list)
from Chapter2.themes.sequences_as_conventional_interfaces import accumulate
from Chapter2.themes.sets_as_binary_trees import adjoin_set, make_tree


def union_set(s1, s2):
    """Implements the union_set operation for sets that are represented as
    (balanced) binary trees. The algorithm is theta(n)"""
    return accumulate(
        lambda x, set: list_to_tree(tree_to_list_2(adjoin_set(x, set))),
        s1,
        tree_to_list_2(s2)
    )


def intersection_set(s1, s2):
    """Implements the intersection_set operation for sets that are
    represented as (balanced) trees. This algorithm is theta(n)"""
    return list_to_tree(
        sets_as_ordered_lists.intersection_set(
            tree_to_list_2(s1),
            tree_to_list_2(s2)
        ))


def run_the_magic():
    s1 = make_tree(
        7,
        make_tree(3, -1, 5),
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
    print_lisp_list(union_set(
        list_to_tree(tree_to_list_2(s1)),
        list_to_tree(tree_to_list_2(s2))
    ))
    print_lisp_list(union_set(s1, s2))
    print_lisp_list(intersection_set(s1, s2))


if __name__ == "__main__":
    run_the_magic()
