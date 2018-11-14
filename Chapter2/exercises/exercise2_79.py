# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.79
"""
# Use the install_complex_package of exercise 2_77 as this handles the double-
# tagging of complex numbers
from Chapter2.exercises.exercise2_77 import install_complex_package
from Chapter2.themes.data_directed_programming_and_additivity import (
    apply_generic
)
from Chapter2.themes.generic_arithmetic_operations import (
    make_complex_from_real_imag, install_rational_package,
    make_complex_from_mag_ang,
    make_rational,
)
from Chapter2.themes.symbolic_data import quote
from Chapter2.themes.symbolic_differentiation import is_a_number


def equals(x, y):
    if is_a_number(x):
        return is_a_number(y) and x == y
    return apply_generic(quote('equals'), x, y)


def run_the_magic():
    print('(equ? 1 2)')
    print(equals(1, 2))

    print('(equ? 1 1)')
    print(equals(1, 1))

    print('(install-complex-package)')
    print('(install-rational-package)')
    install_complex_package()
    install_rational_package()

    print('(equ? (make-rational 1 2) '
          '(make-rational 1 2))')
    print(equals(
        make_rational(1, 2),
        make_rational(1, 2)
    ))

    print('(equ? (make-rational 1 3) '
          '(make-rational 1 2))')
    print(equals(
        make_rational(1, 3),
        make_rational(1, 2)
    ))

    print('(equ? (make-complex-from-real-imag 1 2) '
          '(make-complex-from-real-imag 1 2))')
    print(equals(
        make_complex_from_real_imag(1, 2),
        make_complex_from_real_imag(1, 2)
    ))

    print('(equ? (make-complex-from-real-imag 1 2) '
          '(make-complex-from-mag-ang 1 2))')
    print(equals(
        make_complex_from_real_imag(1, 2),
        make_complex_from_mag_ang(1, 2)
    ))


if __name__ == "__main__":
    run_the_magic()

