# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#%_thm_2.2
"""
from Chapter1.themes.sqrt_newton import average
from Chapter2.themes.lisp_list_structured_data import car, cdr, cons


# Start segment representation
def make_segment(a, b):
    return cons(a, b)


def start_segment(ab):
    return car(ab)


def end_segment(ab):
    return cdr(ab)

# End segment representation


# Start point representation
def make_point(x, y):
    return cons(x, y)


def x_point(a):
    return car(a)


def y_point(a):
    return cdr(a)


def print_point(p):
    print('({}, {})'.format(x_point(p), y_point(p)))
# End point representation


# Start using the two objects in another system
def midpoint_segment(ab):
    return make_point(
        average(
            x_point(start_segment(ab)),
            x_point(end_segment(ab))
        ),
        average(
            y_point(start_segment(ab)),
            y_point(end_segment(ab))
        )
    )
# End using the two objects in another system


def run_the_magic():
    a = make_point(1, 2)
    b = make_point(4, -1)
    ab = make_segment(a, b)
    midpoint = midpoint_segment(ab)
    print('(print-point a)')
    print_point(a)
    print('(print-point b)')
    print_point(b)
    print('(print-point midpoint)')
    print_point(midpoint)


if __name__ == '__main__':
    run_the_magic()
