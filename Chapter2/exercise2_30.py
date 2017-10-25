# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.30
"""
from Chapter1.compound_procedures import square
from Chapter2.hierarchical_structures import pair
from Chapter2.lisp_list_structured_data import car, cdr, cons, lisp_list
from Chapter2.mapping_over_lists import map


def square_tree(tree):
    if tree is None:
        return None
    if not pair(tree):
        return square(tree)
    return cons(
        square_tree(car(tree)),
        square_tree(cdr(tree))
    )


def square_tree_map(tree):
    return map(
        lambda sub_tree: square_tree_map(sub_tree) if pair(sub_tree) else square(sub_tree),
        tree
    )


if __name__ == '__main__':
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
    print('(square-tree-map (list 1 (list 2 (list 3 4) 5) (list 6 7))')
    print(
        square_tree_map(
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
