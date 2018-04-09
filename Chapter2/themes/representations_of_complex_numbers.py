# -*- coding: utf-8 -*-
"""
"""
from math import sqrt, cos, sin
from operator import add

from Chapter1.themes.compound_procedures import square
from Chapter2.themes.hierarchical_structures import pair
from Chapter2.themes.lisp_list_structured_data import car, cdr, cons
from Chapter2.themes.symbolic_data import quote, symbol_equal
from utils import atan, error


def add_complex(z1, z2):
    return make_from_real_imag(
        real_part(z1) + real_part(z2),
        imag_part(z1) + imag_part(z2))


def sub_complex(z1, z2):
    return make_from_real_imag(
        real_part(z1) - real_part(z2),
        imag_part(z1) - imag_part(z2))


def mul_complex(z1, z2):
    return make_from_mag_ang(
        magnitude(z1) * magnitude(z2),
        angle(z1) + angle(z2))


def div_complex(z1, z2):
    return make_from_mag_ang(
        magnitude(z1) / magnitude(z2),
        angle(z1) - angle(z2))


# Representation of complex number in the 'rectangular form'
def real_part_rectangular(z):
    return car(z)


def imag_part_rectangular(z):
    return cdr(z)


def magnitude_rectangular(z):
    return sqrt(add(
        square(real_part_rectangular(z)),
        square(imag_part_rectangular(z))))


def angle_rectangular(z):
    return atan(imag_part_rectangular(z), real_part_rectangular(z))


def make_from_real_imag_rectangular(x, y):
    return attach_tag(
        quote('rectangular'),
        cons(x, y))


def make_from_mag_ang_rectangular(r, a):
    return attach_tag(
        quote('rectangular'),
        cons(r * cos(a), r * sin(a)))


# Representation of complex numbers in 'polar form'
def real_part_polar(z):
    return magnitude_polar(z) * cos(angle_polar(z))


def imag_part_polar(z):
    return magnitude_polar(z) * sin(angle_polar(z))


def magnitude_polar(z):
    return car(z)


def angle_polar(z):
    return cdr(z)


def make_from_real_imag_polar(x, y):
    return attach_tag(
        quote('polar'),
        cons(sqrt(square(x) + square(y)), atan(x, y)))


def make_from_mag_ang_polar(r, a):
    return attach_tag(
        quote('polar'),
        cons(r, a))


# Generic selectors

def real_part(z):
    if is_rectangular(z):
        return real_part_rectangular(contents(z))
    if is_polar(z):
        return real_part_polar(contents(z))
    error('Unknown type: {} -- REAL-PART'.format(z))


def imag_part(z):
    if is_rectangular(z):
        return imag_part_rectangular(contents(z))
    if is_polar(z):
        return imag_part_polar(contents(z))
    error('Unknown type: {} -- IMAG-PART'.format(z))


def magnitude(z):
    if is_rectangular(z):
        return magnitude_rectangular(contents(z))
    if is_polar(z):
        return magnitude_polar(contents(z))
    error('Unknown type: {} -- MAGNITUDE'.format(z))


def angle(z):
    if is_rectangular(z):
        return angle_rectangular(contents(z))
    if is_polar(z):
        return angle_polar(contents(z))
    error('Unknown type: {} -- ANGLE'.format(z))


def make_from_real_imag(x, y):
    return make_from_real_imag_rectangular(x, y)


def make_from_mag_ang(r, a):
    return make_from_mag_ang_polar(r, a)


# Tagged data manipulation procedures

def attach_tag(tag, contents):
    return cons(tag, contents)


def type_tag(datum):
    if pair(datum):
        return car(datum)
    error("Bad tagged datum: {} -- TYPE-TAG".format(datum))


def contents(datum):
    if pair(datum):
        return cdr(datum)
    error("Bad tagged datum: {} -- CONTENTS".format(datum))


def is_rectangular(z):
    return symbol_equal(type_tag(z), quote('rectangular'))


def is_polar(z):
    return symbol_equal(type_tag(z), quote('polar'))


def run_the_magic():
    pass


if __name__ == '__main__':
    run_the_magic()

