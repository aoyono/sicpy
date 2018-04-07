# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.67
"""
from Chapter2.themes.huffman_encoding_tree import (
    make_code_tree, make_leaf,
    decode,
)
from Chapter2.themes.lisp_list_structured_data import lisp_list, print_lisp_list
from Chapter2.themes.symbolic_data import quote
from Chapter2.themes.mapping_over_lists import map


def sample_tree():
    return make_code_tree(
        make_leaf(quote('A'), 4),
        make_code_tree(
            make_leaf(quote('B'), 2),
            make_code_tree(
                make_leaf(quote('D'), 1),
                make_leaf(quote('C'), 1))))


def sample_message():
    return map(lambda bit: int(bit), lisp_list(*'0110010101110'))


def run_the_magic():
    print_lisp_list(
        decode(
            sample_message(),
            sample_tree()
        )
    )


if __name__ == "__main__":
    run_the_magic()

