# -*- coding: utf-8 -*-
"""
"""
from Chapter2.lisp_list_structured_data import car, cdr, cons, lisp_list


def scale_list(items, factor):
    if items is None:
        return None
    return cons(
        car(items) * factor,
        scale_list(cdr(items), factor)
    )


def map(proc, items):
    if items is None:
        return None
    return cons(
        proc(car(items)),
        map(proc, cdr(items))
    )


def scale_list_map(items, factor):
    return map(
        lambda x: x * factor,
        items
    )


if __name__ == '__main__':
    print('(scale-list (list 1 2 3 4 5) 10)')
    print(scale_list(lisp_list(1, 2, 3, 4, 5), 10))
