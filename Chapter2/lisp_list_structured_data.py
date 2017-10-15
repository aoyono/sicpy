# -*- coding: utf-8 -*-
"""
Implementing Lisp equivalents of cons, car, and cdr.

Note 2 (https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#footnote_Temp_133):

The name cons stands for ``construct.'' The names car and cdr derive from the original implementation of Lisp on the
IBM 704. That machine had an addressing scheme that allowed one to reference the ``address'' and ``decrement'' parts of
a memory location. Car stands for ``Contents of Address part of Register'' and cdr (pronounced ``could-er'') stands for
``Contents of Decrement part of Register.''
"""


def cons(a, b):
    return tuple((a, b))


def car(pair):
    return pair[0]


def cdr(pair):
    return pair[1]
