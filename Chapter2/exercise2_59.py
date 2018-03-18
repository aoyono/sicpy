# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.59
"""
from Chapter2.lisp_list_structured_data import lisp_list, print_lisp_list
from Chapter2.sequences_as_conventional_interfaces import accumulate
from Chapter2.sets_as_unordered_lists import adjoin_set


def union_set(set1, set2):
    """Computes the union of set1 and set2"""
    return accumulate(adjoin_set, set2, set1)


def run_the_magic():
    s1 = lisp_list(1, 2, 3)
    s2 = lisp_list(4, 3, 6)
    print_lisp_list(union_set(s1, s2))


if __name__ == "__main__":
    run_the_magic()
