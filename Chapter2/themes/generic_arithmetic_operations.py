# -*- coding: utf-8 -*-
"""
"""
from Chapter1.themes.great_common_divisor import gcd
from Chapter2.themes.data_directed_programming_and_additivity import (
    apply_generic, install_polar_package,
    install_rectangular_package,
)
from Chapter2.themes.lisp_list_structured_data import car, cdr, cons, lisp_list
from Chapter2.themes.data_directed_programming_and_additivity import (
    angle, attach_tag, imag_part, magnitude, real_part,
)
from Chapter2.themes.symbolic_data import quote
from utils import get, let, put


def add(x, y):
    return apply_generic(quote('add'), x, y)


def sub(x, y):
    return apply_generic(quote('sub'), x, y)


def mul(x, y):
    return apply_generic(quote('mul'), x, y)


def div(x, y):
    return apply_generic(quote('div'), x, y)


def install_scheme_number_package():
    def tag(x):
        return attach_tag(quote('scheme-number'), x)

    put(quote('add'),
        quote(lisp_list('scheme-number', 'scheme-number')),
        lambda x, y: tag(x + y))
    put(quote('sub'),
        quote(lisp_list('scheme-number', 'scheme-number')),
        lambda x, y: tag(x - y))
    put(quote('mul'),
        quote(lisp_list('scheme-number', 'scheme-number')),
        lambda x, y: tag(x * y))
    put(quote('div'),
        quote(lisp_list('scheme-number', 'scheme-number')),
        lambda x, y: tag(x / y))
    put(quote('make'),
        quote('scheme-number'),
        lambda x: tag(x))
    return quote('done')


def make_scheme_number(n):
    return get(quote('make'), quote('scheme-number'))(n)


def install_rational_package():
    # Internal procedures
    def numer(x):
        return car(x)

    def denom(x):
        return cdr(x)

    def make_rat(num, den):
        """The IF block comes from exercise 2.1"""
        with let(gcd(num, den)) as (g,):
            if num * den < 0:
                return cons(
                    - abs(num) // g,
                    abs(den) // g)
            return cons(
                abs(num) // g,
                abs(den) // g)

    def add_rat(x, y):
        return make_rat(
            numer(x) * denom(x) + numer(y) * denom(y),
            denom(x) * denom(y))

    def sub_rat(x, y):
        return make_rat(
            numer(x) * denom(x) - numer(y) * denom(y),
            denom(x) * denom(y))

    def mul_rat(x, y):
        return make_rat(
            numer(x) * numer(y),
            denom(x) * denom(y))

    def div_rat(x, y):
        return make_rat(
            numer(x) * denom(y),
            denom(x) * numer(y))

    # From exercise 2.79
    def equal_rat(x, y):
        return numer(x) * denom(y) == numer(y) * denom(x)

    # From exercise 2.80
    def eq_zero(x):
        return numer(x) == 0

    # interface to the rest of the system
    def tag(x):
        return attach_tag(quote('rational'), x)

    put(quote('add'),
        quote(lisp_list('rational', 'rational')),
        lambda x, y: tag(add_rat(x, y)))
    put(quote('sub'),
        quote(lisp_list('rational', 'rational')),
        lambda x, y: tag(sub_rat(x, y)))
    put(quote('mul'),
        quote(lisp_list('rational', 'rational')),
        lambda x, y: tag(mul_rat(x, y)))
    put(quote('div'),
        quote(lisp_list('rational', 'rational')),
        lambda x, y: tag(div_rat(x, y)))
    # From exercise 2.79
    put(quote('equals'),
        quote(lisp_list('rational', 'rational')),
        equal_rat)
    # From exercise 2.80
    put(quote('eq_zero'),
        quote(lisp_list('rational')),
        eq_zero)

    put(quote('make'),
        quote('rational'),
        lambda n, d: tag(make_rat(n, d)))
    return quote('done')


def make_rational(n, d):
    return get(quote('make'), quote('rational'))(n, d)


def install_complex_package():
    # Imported procedures from rectangular and polar packages
    def make_from_real_imag(x, y):
        return get(quote('make-from-real-imag'), quote('rectangular'))(x, y)

    def make_from_mag_ang(r, a):
        return get(quote('make-from-mag-ang'), quote('polar'))(r, a)

    # Internal procedures
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

    # From exercise 2.79
    def equals(z1, z2):
        return (real_part(z1) == real_part(z2)
                and imag_part(z1) == imag_part(z2))

    # From exercise 2.80
    def eq_zero(z):
        return equals(z, make_from_real_imag(0, 0))

    # Interface to the rest of the system
    def tag(z):
        return attach_tag(quote('complex'), z)

    put(quote('add'),
        quote(lisp_list('complex', 'complex')),
        lambda z1, z2: tag(add_complex(z1, z2)))
    put(quote('sub'),
        quote(lisp_list('complex', 'complex')),
        lambda z1, z2: tag(sub_complex(z1, z2)))
    put(quote('mul'),
        quote(lisp_list('complex', 'complex')),
        lambda z1, z2: tag(mul_complex(z1, z2)))
    put(quote('div'),
        quote(lisp_list('complex', 'complex')),
        lambda z1, z2: tag(div_complex(z1, z2)))
    # From exercise 2.79
    put(quote('equals'),
        quote(lisp_list('complex', 'complex')),
        equals)
    # From exercise 2.80
    put(quote('eq_zero'),
        quote(lisp_list('complex')),
        eq_zero)

    # install polar and rectangular representations
    # this is necessary as we retrieve some methods for these representations
    # in the internal methods defined here
    install_polar_package()
    install_rectangular_package()

    put(quote('make-from-real-imag'),
        quote('complex'),
        lambda x, y: tag(make_from_real_imag(x, y)))
    put(quote('make-from-mag-ang'),
        quote('complex'),
        lambda r, a: tag(make_from_mag_ang(r, a)))
    return quote('done')


def make_complex_from_real_imag(x, y):
    return get(quote('make-from-real-imag'),
               quote('complex'))(x, y)


def make_complex_from_mag_ang(r, a):
    return get(quote('make-from-mag-ang'),
               quote('complex'))(r, a)


def run_the_magic():
    pass


if __name__ == '__main__':
    run_the_magic()
