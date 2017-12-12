# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.31
"""
from Chapter1.compound_procedures import square
from Chapter2.hierarchical_structures import pair
from Chapter2.lisp_list_structured_data import lisp_list
from Chapter2.mapping_over_lists import map


def tree_map(func, tree):
    return map(
        lambda sub_tree: tree_map(func, sub_tree) if pair(sub_tree) else func(sub_tree),
        tree
    )


def square_tree(tree):
    return tree_map(square, tree)


def run_the_magic():
    print('(square-tree (list 1 (list 2 (list 3 4) 5) (list 6 7))')
    print(
        square_tree(
            lisp_list(
                1,
                lisp_list(
                    2,
                    lisp_list(
                        3,
                        4
                    ),
                    5
                ),
                lisp_list(
                    6,
                    7
                )
            )
        )
    )


if __name__ == '__main__':
    run_the_magic()
