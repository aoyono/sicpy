# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#%_thm_2.3
"""

from Chapter2.themes.lisp_list_structured_data import car, cdr, cons


def make_rect(lower_left, width, height):
    """rectangle defined as lower-left summit and width and height"""
    return cons(
        lower_left,
        cons(width, height)
    )


def width(rect):
    return car(cdr(rect))


def height(rect):
    return cdr(car(rect))


def perimeter(rect):
    return 2 * (height(rect) + width(rect))


def area(rect):
    return height(rect) * width(rect)


# second model
# def make_rect(lower_left, upper_right):
#     """rectangle defined as lower-left and upper-right summits"""
#     return cons(
#         lower_left,
#         upper_right
#     )
#
#
# def width(rect):
#     return sub(
#         x_point(cdr(rect)),
#         x_point(car(rect))
#     )
#
#
# def heigth(rect):
#     return sub(
#         y_point(cdr(rect)),
#         y_point(car(rect))
#     )
