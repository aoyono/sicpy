# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.63
"""
from Chapter2.themes.lisp_list_structured_data import (
    append, car, cdr,
    lisp_list, nil,
    print_lisp_list, cons,
)
from Chapter2.themes.sets_as_binary_trees import (entry, left_branch,
                                                  make_tree, right_branch)


def tree_to_list_1(tree):
    """Transforms tree to list algo 1.

    This procedure first puts the left branch of the tree in the
    resulting list, and then adds the elements of the right branch
    after them
    """
    if tree is nil:
        return nil
    return append(
        tree_to_list_1(left_branch(tree)),
        cons(entry(tree), tree_to_list_1(right_branch(tree)))
    )


def tree_to_list_2(tree):
    """Transforms tree to list algo 2.

    This algorithm first puts the right branch of the tree
    in the resulting list and then adds the elements of the
    left branch before them
    """
    def copy_to_list(tree, result_list):
        if tree is nil:
            return result_list
        return copy_to_list(
            left_branch(tree),
            cons(entry(tree), copy_to_list(right_branch(tree), result_list))
        )
    return copy_to_list(tree, nil)


def run_the_magic():
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
    print_lisp_list(tree_to_list_1(s1))
    print_lisp_list(tree_to_list_2(s1))
    print_lisp_list(tree_to_list_1(s2))
    print_lisp_list(tree_to_list_2(s2))
    print_lisp_list(tree_to_list_1(s3))
    print_lisp_list(tree_to_list_2(s3))

    from timeit import Timer
    for s in ('s1', 's2', 's3'):
        print('-' * 16)
        print('Performance analysis for %s' % s)
        t1 = Timer(
            stmt='tree_to_list_1(%({})s)'.format(s) % locals(),
            setup='from Chapter2.exercises.exercise2_63 import tree_to_list_1'
        )
        t2 = Timer(
            stmt='tree_to_list_2(%({})s)'.format(s) % locals(),
            setup='from Chapter2.exercises.exercise2_63 import tree_to_list_2'
        )

        time = t1.timeit()
        print('average time (tree_to_list_1): %s' % time)

        time = t2.timeit()
        print('average_time (tree_to_list_2): %s' % time)


if __name__ == "__main__":
    run_the_magic()
