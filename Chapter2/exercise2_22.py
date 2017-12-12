# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.22
"""
from Chapter1.compound_procedures import square
from Chapter2.lisp_list_structured_data import car, cdr, cons, lisp_list, nil


def square_list(items):
    """This produces the response in the reverse order because in the iteration process we walk the items list and the
    final result list in opposite ways: while answer list grows, things list shrinks"""

    def iter(things, answer):
        if things is nil():
            return answer
        return iter(
            cdr(things),
            cons(
                square(car(things)),
                answer
            )
        )

    return iter(items, nil())


def square_list2(items):
    def iter(things, answer):
        if things is nil():
            return answer
        return iter(
            cdr(things),
            cons(
                answer,
                square(car(things))
            )
        )

    return iter(items, nil())


def run_the_magic():
    print('(square-list (list 1 2 3 4))')
    print(square_list(lisp_list(1, 2, 3, 4)))
    print('(square-list (list 1 2 3 4))')
    print(square_list2(lisp_list(1, 2, 3, 4)))


if __name__ == '__main__':
    run_the_magic()
