# -*- coding: utf-8 -*-
"""
"""
from Chapter2.hierarchical_structures import pair
from Chapter2.lisp_list_structured_data import car, cdr, cons, lisp_list
from Chapter2.mapping_over_lists import map


def scale_tree(tree, factor):
    if tree is None:
        return None
    if not pair(tree):
        return tree * factor
    return cons(
        scale_tree(car(tree), factor),
        scale_tree(cdr(tree), factor)
    )


def scale_tree_map(tree, factor):
    return map(
        lambda sub_tree: scale_tree_map(sub_tree, factor) if pair(sub_tree) else sub_tree * factor,
        tree
    )


if __name__ == '__main__':
    print('scale-tree (list 1 (list 2 (list 3 4) 5) (list 6 7)) 10)')
    print(scale_tree(lisp_list(1, lisp_list(2, lisp_list(3, 4), 5), lisp_list(6, 7)), 10))
    print('scale-tree-map (list 1 (list 2 (list 3 4) 5) (list 6 7)) 10)')
    print(scale_tree_map(lisp_list(1, lisp_list(2, lisp_list(3, 4), 5), lisp_list(6, 7)), 10))
