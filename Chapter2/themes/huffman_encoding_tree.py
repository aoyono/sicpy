# -*- coding: utf-8 -*-
"""
"""
from Chapter2.themes.lisp_list_structured_data import (
    append, cadddr, caddr, cadr, car, cdr, cons, lisp_list, nil,
)
from Chapter2.themes.symbolic_data import quote, symbol_equal
from utils import error, let


# Representing Huffman trees

# Representing the leaf of a tree

def make_leaf(symbol, weight):
    return lisp_list(quote('leaf'), symbol, weight)


def is_leaf(obj):
    return symbol_equal(car(obj), quote('leaf'))


def symbol_leaf(x):
    return cadr(x)


def weight_leaf(x):
    return caddr(x)

# End Representing the leaf of a tree


# Representing general tree

def make_code_tree(left, right):
    return lisp_list(
        left,
        right,
        append(symbols(left), symbols(right)),
        weight(left) + weight(right))


def left_branch_tree(tree):
    return car(tree)


def right_branch_tree(tree):
    return cadr(tree)


def symbols(tree):
    if is_leaf(tree):
        return lisp_list(symbol_leaf(tree))
    return caddr(tree)


def weight(tree):
    if is_leaf(tree):
        return weight_leaf(tree)
    return cadddr(tree)

# End Representing general tree


def decode(bits, tree):
    """Decodes a Huffman tree"""
    def decode_1(bits, current_branch):
        """Decodes the current branch given the bits"""
        if bits is nil:
            return nil
        with let(choose_branch(car(bits), current_branch)) as (next_branch,):
            if is_leaf(next_branch):
                return cons(
                    symbol_leaf(next_branch),
                    decode_1(cdr(bits), tree))
            return decode_1(cdr(bits), next_branch)
    return decode_1(bits, tree)


def choose_branch(bit, tree):
    """Decide to which branch of tree to continue, based on bit"""
    if bit == 0:
        return left_branch_tree(tree)
    elif bit == 1:
        return right_branch_tree(tree)
    error('bad bit: {}'.format(choose_branch.__name__.upper()))


def adjoin_set(x, set):
    """Adds a leave to a node in Huffman tree, maintaining the order by
    weight"""
    if set is nil:
        return lisp_list(x)
    if weight(x) < weight(car(set)):
        return cons(x, set)
    return cons(
        car(set),
        adjoin_set(x, cdr(set)))


def make_leaf_set(pairs):
    """Constructs an initial ordered set of leaves ready to be merged
    according to Huffman algorithm"""
    if pairs is nil:
        return lisp_list()
    with let(car(pairs)) as (pair,):
        return adjoin_set(
            make_leaf(
                car(pair),      # symbol
                cadr(pair)),    # frequency
            make_leaf_set(cdr(pairs)))


def run_the_magic():
    pass


if __name__ == '__main__':
    run_the_magic()
