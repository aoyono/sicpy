# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.66
"""
import random
from itertools import repeat

from Chapter2.exercises.exercise2_63 import tree_to_list_2
from Chapter2.exercises.exercise2_64 import list_to_tree
from Chapter2.themes.lisp_list_structured_data import car, lisp_list, nil, cdr
from Chapter2.themes.sets_as_binary_trees import (
    element_of_set, make_tree,
    entry,
    left_branch,
    right_branch,
)
from Chapter2.themes.mapping_over_trees import map
from utils import repeatfunc, let


def lookup(given_key, set_of_records):
    """Lookup a given_key in records, where records are implemented as binary
    tree sets"""
    if set_of_records is nil:
        return nil
    with let(entry(set_of_records)) as (top_node,):
        with let(key(top_node)) as (top_node_key,):
            if given_key == top_node_key:
                return top_node
            if given_key < top_node_key:
                return lookup(given_key, left_branch(set_of_records))
            if given_key > top_node_key:
                return lookup(given_key, right_branch(set_of_records))


def key(record):
    """Retrieve the key that uniquely identifies the record (we implement a
    record as a Python dict object. See the body of run_the_magic)"""
    return record['key']


def run_the_magic():
    records = make_tree(
        {'key': 5, 'value': 'item1'},
        make_tree(
            {'key': 2, 'value': 'item2'},
            make_tree(
                {'key': 1, 'value': 'item3'},
                {'key': 0, 'value': 'item9'},
                nil
            ),
            {'key': 3, 'value': 'item6'},
        ),
        make_tree(
            {'key': 40, 'value': 'item134'},
            {'key': 6, 'value': 'item43'},
            make_tree(
                {'key': 78, 'value': 'item97'},
                {'key': 60, 'value': 'item10'},
                {'key': 80, 'value': 'item120'},
            ),
        )
    )

    def get_given_key(records_as_list):
        """Utility function to get keys from the records"""
        if records_as_list is nil:
            return
        yield car(records_as_list)
        yield from get_given_key(cdr(records_as_list))

    for given_key in get_given_key(map(key, tree_to_list_2(records))):
        print('Looking for key: {}  -->  '.format(given_key), end='')
        print(lookup(given_key, list_to_tree(tree_to_list_2(records))))


if __name__ == "__main__":
    run_the_magic()

