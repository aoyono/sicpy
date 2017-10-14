# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%_thm_1.45
"""
import math
from operator import truediv, sub

from Chapter1.abstraction_and_first_class_procedure import fixed_point_of_transform
from Chapter1.exercise1_43 import repeated
from Chapter1.procedures_as_returned_values import average_damp


def damp_number(n):
    """Thank you https://github.com/qiao/sicp-solutions/blob/master/chapter1/1.45.scm"""
    return math.floor(truediv(
        math.log(n),
        math.log(2)
    ))


def nth_root(x, n):
    """Thank you https://github.com/qiao/sicp-solutions/blob/master/chapter1/1.45.scm"""
    return fixed_point_of_transform(
        lambda y: truediv(x, math.pow(y, sub(n, 1))),
        repeated(average_damp, damp_number(n)),
        1.0
    )


if __name__ == '__main__':
    x, n = math.pow(3, 9), 9
    print('(nth-root %(x)s %(n)s)' % locals())
    print(nth_root(x, n))
