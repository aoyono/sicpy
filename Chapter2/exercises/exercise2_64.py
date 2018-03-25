# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.64
"""
from operator import floordiv

from Chapter2.themes.lisp_list_structured_data import (
    car, cdr, cons, length,
    lisp_list, nil,
    print_lisp_list,
)
from Chapter2.themes.sets_as_binary_trees import make_tree
from utils import let


def list_to_tree(elements):
    """Converts an ordered list to a balanced binary tree.

    For example, list_to_tree of (1 3 5 7 9 11) will produce the following
    balanced tree:
                                    5
                                   / \
                                  /   \
                                 1     9
                                  \   / \
                                  3  7  11
    """
    return car(partial_tree(elements, length(elements)))


def partial_tree(elts, n):
    """Creates a pair whose car is the balanced tree containing at most n
    elements from elts and cdr is the elements of elts not included in the tree.

    A balanced tree is a tree with one top level node, with left and right
    branches having the same number of levels of nodes. Therefore the first
    thing partial_tree does is computing the size of each part of the
    expected resulting tree (which is the half of the requested size of the
    expected result).
    After that, it computes the balanced tree of the left side using all the
    original list of elements. Then, the first element of the elements that
    did not managed to attach themselves to the left side is used as the root
    node of the future right size that it will now compute."""
    if n == 0:
        return cons(nil, elts)
    with let(floordiv(n - 1, 2)) as (left_size, ):
        with let(partial_tree(elts, left_size)) as (left_result, ):
            with let(car(left_result), cdr(left_result),
                     n - (left_size + 1)) as (left_tree, non_left_elts,
                                              right_size):
                with let(
                        car(non_left_elts),
                        partial_tree(cdr(non_left_elts),
                                     right_size)) as (this_entry,
                                                      right_result):
                    with let(car(right_result),
                             cdr(right_result)) as (right_tree,
                                                    remaining_elts):
                        return cons(
                            make_tree(this_entry, left_tree, right_tree),
                            remaining_elts)


def run_the_magic():
    s = lisp_list(1, 3, 5, 7, 9, 11)
    print_lisp_list(list_to_tree(s))


if __name__ == "__main__":
    run_the_magic()
