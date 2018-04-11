# -*- coding: utf-8 -*-
"""
"""
from math import sqrt

from Chapter1.themes.compound_procedures import square
from Chapter2.themes.symbolic_data import quote, symbol_equal
from utils import atan, error


def make_from_real_imag(x, y):
    def dispatch(op):
        if symbol_equal(op, quote('real-part')):
            return x
        if symbol_equal(op, quote('imag-part')):
            return y
        if symbol_equal(op, quote('magnitude')):
            return sqrt(square(x) + square(y))
        if symbol_equal(op, quote('angle')):
            return atan(y, x)
        error('Unknown op: {} -- MAKE-FROM-REAL-IMAG'.format(op))
    return dispatch


def apply_generic(op, arg):
    return arg(op)


def run_the_magic():
    pass


if __name__ == '__main__':
    run_the_magic()

