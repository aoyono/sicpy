# -*- coding: utf-8 -*-
"""
Observe that our model of evaluation allows for combinations whose operators are compound expressions.
Use this observation to describe the behavior of the following procedure:

(define (a-plus-abs-b a b)
  ((if (> b 0) + -) a b))
"""
from operator import add, sub, gt

from Chapter1.lisp_conditionals import lisp_if


def a_plus_abs_b(a, b):
    '''procedures can be returned as results of conditionals
    '''
    return lisp_if(gt(b, 0), add, sub)(a, b)
    # return (add if gt(b, 0) else sub)(a, b)


if __name__ == '__main__':
    print(a_plus_abs_b(3, -6))
