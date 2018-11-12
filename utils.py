# -*- coding: utf-8 -*-
import math
from contextlib import contextmanager


@contextmanager
def let(*args):
    try:
        yield args
    finally:
        del args


def error(*args):
    print(*args)
    raise Exception


def atan(x, y):
    """Equivalent of the Scheme atan function which takes 2 args and return the
    angle whose tangent is equal to y/x"""
    return math.atan(y/x)


DATA_DIRECTED_PROG_TABLE = {}


def put(operation, type_tag, item):
    DATA_DIRECTED_PROG_TABLE[(operation, type_tag)] = item


def get(operation, type_tag):
    return DATA_DIRECTED_PROG_TABLE.get((operation, type_tag), False)


def apply(proc, args):
    return proc(*_lisp_list_to_python_list(args))


def _lisp_list_to_python_list(l):
    def _get_tuple_element(instance, position):
        """Helper method to ensure we don't have errors while getting items
        from a tuple"""
        if isinstance(instance, tuple) and position < len(instance):
            return instance[position]
        return tuple()

    def cdr(pair):
        return _get_tuple_element(pair, 1)

    def car(pair):
        return _get_tuple_element(pair, 0)

    elt = l
    result = []
    while elt:
        result.append(car(elt))
        elt = cdr(l)
    return result
