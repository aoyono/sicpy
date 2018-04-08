# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.69
"""
from Chapter2.themes.huffman_encoding_tree import (
    adjoin_set, make_leaf_set,
    make_code_tree,
)
from Chapter2.themes.lisp_list_structured_data import (
    car, cdr, lisp_list, nil,
    cadr,
    cddr,
    cons,
    print_lisp_list,
)
from Chapter2.themes.symbolic_data import quote
from utils import let


def generate_huffman_tree(pairs):
    """Generates a huffman encoding tree from a list of symbol-frequency pairs
    """
    return successive_merge(
        make_leaf_set(pairs))


def successive_merge(leaves):
    """Successively merges leaves using Huffman encoding tree algorithm"""
    def merge(leaf, rest, result):
        """Merges leaf with the rest of the tree, storing results in result"""
        if rest is nil:
            return result
        with let(make_code_tree(leaf, car(rest))) as (partial_tree,):
            return merge(
                partial_tree,
                cdr(rest),
                partial_tree)
    return merge(car(leaves), cdr(leaves), lisp_list())


def run_the_magic():
    with let(
            lisp_list(
                lisp_list(quote('A'), 4),
                lisp_list(quote('B'), 2),
                lisp_list(quote('C'), 1),
                lisp_list(quote('D'), 1),)) as (pairs,):
        print_lisp_list(generate_huffman_tree(pairs))


if __name__ == "__main__":
    run_the_magic()

