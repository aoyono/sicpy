# -*- coding: utf-8 -*-
"""
Show that the golden ratio (section 1.2.2) is a fixed point of the transformation x |--> 1 + 1/x, and use this fact to
compute it by means of the fixed-point procedure.
"""
from operator import add, truediv

import math

from Chapter1.themes.procedures_as_general_methods import fixed_point


def golden_ratio():
    return fixed_point(
        lambda x: add(1, truediv(1, x)),
        1.0
    )


def run_the_magic():
    print("(golden-ratio)")
    print(golden_ratio())
    print("(/ (+ 1 (sqrt 5)) 2))")
    print((1 + math.sqrt(5))/2)
    print("(- (golden-ratio) (/ (+ 1 (sqrt 5)) 2)))")
    print(golden_ratio() - (1 + math.sqrt(5))/2)


if __name__ == '__main__':
    run_the_magic()
