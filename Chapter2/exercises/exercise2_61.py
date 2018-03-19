# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.61
"""
from Chapter2.themes.lisp_list_structured_data import car, cdr, cons, lisp_list, print_lisp_list, nil


def adjoin_set(x, set):
    """Adds the element x to the set"""
    if set is nil:
        return cons(x, set)
    if x == car(set):
        return set
    if x < car(set):
        return cons(x, set)
    return cons(car(set), adjoin_set(x, cdr(set)))


def run_the_magic():
    s = lisp_list(1, 2, 3, 25)
    print_lisp_list(adjoin_set(4, s))
    print_lisp_list(adjoin_set(0, s))


if __name__ == "__main__":
    run_the_magic()
