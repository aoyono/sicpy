# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.75
"""
from math import cos, sin

from Chapter2.themes.symbolic_data import symbol_equal, quote
from utils import error


def make_from_mag_ang(r, a):
    def dispatch(op):
        if symbol_equal(op, quote('real-part')):
            return r * cos(a)
        if symbol_equal(op, quote('imag-part')):
            return r * sin(a)
        if symbol_equal(op, quote('magnitude')):
            return r
        if symbol_equal(op, quote('angle')):
            return a
        error('Unknown op: {} -- MAKE-FROM-MAG-ANG'.format(op))

    return dispatch


def run_the_magic():
    pass


if __name__ == "__main__":
    run_the_magic()

