# -*- coding: utf-8 -*-
"""
Implementing Lisp equivalents of cons, car, and cdr.

Note 2 (https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#footnote_Temp_133):

The name cons stands for ``construct.'' The names car and cdr derive from the original implementation of Lisp on the
IBM 704. That machine had an addressing scheme that allowed one to reference the ``address'' and ``decrement'' parts of
a memory location. Car stands for ``Contents of Address part of Register'' and cdr (pronounced ``could-er'') stands for
``Contents of Decrement part of Register.''
"""
from Chapter1.exercise1_9 import inc


def cons(a, b):
    return tuple((a, b))


def car(pair):
    return pair[0]


def cdr(pair):
    return pair[1]


# In addition to these, we also give an implementation of Lisp list structure
def lisp_list(*args):
    if not args:
        return None
    return cons(args[0], lisp_list(*args[1:]))


def list_ref(items, n):
    if n == 0:
        return car(items)
    return list_ref(
        cdr(items),
        n - 1
    )


def length(items):
    if items is None:
        return 0
    return 1 + length(cdr(items))


def rlength(items):
    """Recursive implementation of length"""
    def rlength_iter(a, count):
        if a is None:
            return count
        return rlength_iter(cdr(a), inc(count))
    return rlength_iter(items, 0)


def append(list1, list2):
    if list1 is None:
        return list2
    return cons(
        car(list1),
        append(cdr(list1), list2)
    )
