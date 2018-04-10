# -*- coding: utf-8 -*-
"""
"""
from math import cos, sin, sqrt
from operator import add

from Chapter1.themes.compound_procedures import square
from Chapter2.themes.lisp_list_structured_data import car, cdr, cons, lisp_list
from Chapter2.themes.mapping_over_lists import map
from Chapter2.themes.representations_of_complex_numbers import (
    attach_tag, contents, type_tag,
)
from Chapter2.themes.symbolic_data import quote
from utils import apply, atan, error, get, let, put


def install_rectangular_package():
    # Internal procedures
    def real_part(z):
        return car(z)

    def imag_part(z):
        return cdr(z)

    def make_from_real_imag(x, y):
        return cons(x, y)

    def magnitude(z):
        return sqrt(add(
            square(real_part(z)),
            square(imag_part(z))))

    def angle(z):
        return atan(imag_part(z), real_part(z))

    def make_from_mag_ang(r, a):
        return cons(r * cos(a), r * sin(a))

    # Interface to the rest of the system
    def tag(x):
        return attach_tag('rectangular', x)

    put(quote('real-part'), quote(lisp_list('rectangular')), real_part)
    put(quote('imag-part'), quote(lisp_list('rectangular')), imag_part)
    put(quote('magnitude'), quote(lisp_list('rectangular')), magnitude)
    put(quote('angle'), quote(lisp_list('rectangular')), angle)
    put(quote('make-from-real-imag'), quote('rectangular'),
        lambda x, y: tag(make_from_real_imag(x, y)))
    put(quote('make-from-mag-ang'), quote('rectangular'),
        lambda r, a: tag(make_from_mag_ang(r, a)))
    return quote('done')


def install_polar_package():
    # Internal procedures
    def real_part(z):
        return magnitude(z) * cos(angle(z))

    def imag_part(z):
        return magnitude(z) * sin(angle(z))

    def make_from_real_imag(x, y):
        return cons(
            sqrt(square(x) + square(y)),
            atan(x, y))

    def magnitude(z):
        return car(z)

    def angle(z):
        return cdr(z)

    def make_from_mag_ang(r, a):
        return cons(r, a)

    # Interface to the rest of the system
    def tag(x):
        return attach_tag('polar', x)

    put(quote('real-part'), quote(lisp_list('polar')), real_part)
    put(quote('imag-part'), quote(lisp_list('polar')), imag_part)
    put(quote('magnitude'), quote(lisp_list('polar')), magnitude)
    put(quote('angle'), quote(lisp_list('polar')), angle)
    put(quote('make-from-real-imag'), quote('polar'),
        lambda x, y: tag(make_from_real_imag(x, y)))
    put(quote('make-from-mag-ang'), quote('polar'),
        lambda r, a: tag(make_from_mag_ang(r, a)))
    return quote('done')


def apply_generic(op, *args):
    with let(map(type_tag, args)) as (type_tags,):
        with let(get(op, type_tags)) as (proc,):
            if proc:
                return apply(proc, map(contents, args))
            error('No method for these types: {} -- APPLY-GENERIC'.format(
                lisp_list(op, type_tags)))


def real_part(z):
    return apply_generic(quote('real-part'), z)


def imag_part(z):
    return apply_generic(quote('imag-part'), z)


def magnitude(z):
    return apply_generic(quote('magnitude'), z)


def angle(z):
    return apply_generic(quote('angle'), z)


def make_from_real_imag(x, y):
    return get(
        quote('make-from-real-imag'),
        quote('rectangular')
    )(x, y)


def make_from_mag_ang(r, a):
    return get(
        quote('make-from-mag-ang'),
        quote('polar')
    )(r, a)


def run_the_magic():
    pass


if __name__ == '__main__':
    run_the_magic()
