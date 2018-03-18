# -*- coding: utf-8 -*-
"""
Implementing Lisp equivalents of cons, car, and cdr.

Note 2 (https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#footnote_Temp_133):

The name cons stands for ``construct.'' The names car and cdr derive from the original implementation of Lisp on the
IBM 704. That machine had an addressing scheme that allowed one to reference the ``address'' and ``decrement'' parts of
a memory location. Car stands for ``Contents of Address part of Register'' and cdr (pronounced ``could-er'') stands for
``Contents of Decrement part of Register.''
"""
from operator import add

from Chapter1.exercises.exercise1_9 import inc

nil = tuple()


def cons(a, b):
    return tuple((a, b))


def _get_tuple_element(instance, position):
    """Helper method to ensure we don't have errors while getting items from a tuple"""
    if isinstance(instance, tuple) and position < len(instance):
        return instance[position]


def car(pair):
    return _get_tuple_element(pair, 0)


def cdr(pair):
    return _get_tuple_element(pair, 1)


# In addition to these, we also give an implementation of Lisp list structure
def lisp_list(*args):
    if not args:
        return nil
    return cons(args[0], lisp_list(*args[1:]))


def list_ref(items, n):
    if n == 0:
        return car(items)
    return list_ref(
        cdr(items),
        n - 1
    )


def cadr(pair):
    """alias for car(cdr(pair))"""
    return _get_tuple_element(cdr(pair), 0)


def caddr(pair):
    """alias for car(cdr(cdr(pair)))"""
    return cadr(cdr(pair))


def cddr(pair):
    """alias for cdr(cdr(pair))"""
    return cdr(cdr(pair))


def length(items):
    if items is nil:
        return 0
    return 1 + length(cdr(items))


def rlength(items):
    """Recursive implementation of length"""

    def rlength_iter(a, count):
        if a is nil:
            return count
        return rlength_iter(cdr(a), inc(count))

    return rlength_iter(items, 0)


def append(list1, list2):
    if list1 is nil:
        return list2
    return cons(
        car(list1),
        append(cdr(list1), list2)
    )


def repr_lisp_list(l):
    """A function that helps representing our implementation of lisp lists"""

    def reverse(l):
        """We can't import reverse from exercise2_18 as itself imports from this module"""

        def iterate(items, acc):
            if items is nil:
                return acc
            return iterate(cdr(items), cons(car(items), acc))

        return iterate(l, lisp_list())

    def accumulate(op, initial, sequence):
        """We can't import accumulate from sequences_as_conventional_interfaces as itself imports from this module"""
        if sequence is nil:
            return initial
        return op(
            car(sequence),
            accumulate(
                op,
                initial,
                cdr(sequence)
            )
        )

    def pair(x):
        """Can't import this from hierarchical_structures as itself imports this module"""
        return isinstance(x, tuple)

    return add(
        '(',
        add(
            accumulate(
                lambda i, s: s + ' ' + (repr_lisp_list(i) if pair(i) else str(i) if i is not None else ''),
                '',
                reverse(l)
            ),
            ')'
        )
    )


def print_lisp_list(l):
    print(repr_lisp_list(l))
