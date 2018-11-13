# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.78
"""
from Chapter2.themes.hierarchical_structures import pair
from Chapter2.themes.lisp_list_structured_data import car, cdr, cons
from Chapter2.themes.symbolic_data import quote
from Chapter2.themes.symbolic_differentiation import is_a_number
from utils import error


def type_tag(datum):
    if is_a_number(datum):
        return quote('scheme-number')
    if pair(datum):
        return car(datum)
    error("Bad tagged datum: {} -- TYPE-TAG".format(datum))


def contents(datum):
    if is_a_number(datum):
        return datum
    if pair(datum):
        return cdr(datum)
    error("Bad tagged datum: {} -- CONTENTS".format(datum))


def attach_tag(tag, contents):
    if is_a_number(contents):
        return contents
    return cons(tag, contents)


def run_the_magic():
    pass


if __name__ == "__main__":
    run_the_magic()

