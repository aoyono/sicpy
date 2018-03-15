# -*- coding: utf-8 -*-
"""
"""
from Chapter2.lisp_list_structured_data import car, cdr, cons, lisp_list, nil, print_lisp_list


def scale_list(items, factor):
    if items is nil:
        return lisp_list()
    return cons(
        car(items) * factor,
        scale_list(cdr(items), factor)
    )


def map(proc, items):
    if items is nil:
        return lisp_list()
    return cons(
        proc(car(items)),
        map(proc, cdr(items))
    )


def scale_list_map(items, factor):
    return map(
        lambda x: x * factor,
        items
    )


def run_the_magic():
    print('(scale-list (list 1 2 3 4 5) 10)')
    print_lisp_list(scale_list(lisp_list(1, 2, 3, 4, 5), 10))


if __name__ == '__main__':
    run_the_magic()
