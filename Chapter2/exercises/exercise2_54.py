# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.54
"""
from Chapter2.themes.hierarchical_structures import pair
from Chapter2.themes.lisp_list_structured_data import car, cdr, lisp_list, nil
from Chapter2.themes.symbolic_data import quote, seq


def list_equal(l1, l2):
    """list_equal naively thinks that if l1 and l2 are not lists, they will be symbols"""
    if pair(l1) and pair(l2):
        if l1 is nil and l2 is nil:
            return True
        return list_equal(car(l1), car(l2)) and list_equal(cdr(l1), cdr(l2))
    return seq(l1, l2)


def run_the_magic():
    print(list_equal(
        quote(lisp_list('this', 'is', 'a', 'list')),
        quote(lisp_list('this', 'is', 'a', 'list'))
    ))

    print(list_equal(
        quote(lisp_list('this', 'is', 'a', 'list')),
        quote(lisp_list('this', lisp_list('is', 'a'), 'list'))
    ))


if __name__ == "__main__":
    run_the_magic()
