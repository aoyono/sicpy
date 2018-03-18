# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.53
"""
from Chapter2.themes.hierarchical_structures import pair
from Chapter2.themes.lisp_list_structured_data import cadr, car, cdr, lisp_list
from Chapter2.themes.symbolic_data import memq, quote


def run_the_magic():
    print(lisp_list(
        quote('a'),
        quote('b'),
        quote('c'),
    ))

    print(lisp_list(lisp_list(quote('george'))))

    print(cdr(quote(lisp_list(
        lisp_list('x1', 'x2'),
        lisp_list('y1', 'y2'),
    ))))

    print(cadr(quote(lisp_list(
        lisp_list('x1', 'x2'),
        lisp_list('y1', 'y2'),
    ))))

    print(pair(car(quote(lisp_list(
        'a',
        'short',
        'list',
    )))))

    print(memq(
        quote('red'),
        quote(lisp_list(
            lisp_list('red', 'shoes'),
            lisp_list('blue', 'socks')
        ))
    ))

    print(memq(
        quote('red'),
        quote(lisp_list('red', 'shoes', 'blue', 'socks'))
    ))


if __name__ == '__main__':
    run_the_magic()
