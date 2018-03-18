# -*- coding: utf-8 -*-
"""
 In general, programming languages impose restrictions on the ways in which computational elements can be manipulated.
 Elements with the fewest restrictions are said to have first-class status. Some of the ``rights and privileges'' of
 first-class elements are:

    They may be named by variables.
    They may be passed as arguments to procedures.
    They may be returned as the results of procedures.
    They may be included in data structures.

Lisp, unlike other common programming languages, awards procedures full first-class status. This poses challenges for
efficient implementation, but the resulting gain in expressive power is enormous.

Note 66:
The major implementation cost of first-class procedures is that allowing procedures to be returned as values requires
reserving storage for a procedure's free variables even while the procedure is not executing. In the Scheme
implementation we will study in section 4.1, these variables are stored in the procedure's environment.
"""
from operator import sub, truediv

from Chapter1.themes.compound_procedures import square
from Chapter1.themes.newton_method import newton_transform
from Chapter1.themes.procedures_as_general_methods import fixed_point
from Chapter1.themes.procedures_as_returned_values import average_damp


def fixed_point_of_transform(g, transform, guess):
    return fixed_point(
        transform(g),
        guess
    )


def sqrt_average_damp(x):
    return fixed_point_of_transform(
        lambda y: truediv(x, y),
        average_damp,
        1.0
    )


def sqrt_newton_transform(x):
    return fixed_point_of_transform(
        lambda y: sub(square(y), x),
        newton_transform,
        1.0
    )
