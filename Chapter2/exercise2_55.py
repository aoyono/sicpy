# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.55
"""
from Chapter2.lisp_list_structured_data import car, lisp_list
from Chapter2.symbolic_data import quote


def run_the_magic():
    """The code below is self explanatory for why the result is quote"""
    print(car(quote(lisp_list(
        'quote',
        'abracadabra'
    ))))


if __name__ == "__main__":
    run_the_magic()

