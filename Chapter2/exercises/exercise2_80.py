# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.80
"""
from Chapter2.exercises.exercise2_79 import equals
from Chapter2.themes.data_directed_programming_and_additivity import (
    apply_generic
)
from Chapter2.themes.generic_arithmetic_operations import (
    install_complex_package, install_rational_package,
    make_rational,
    make_complex_from_real_imag,
)
from Chapter2.themes.symbolic_data import quote
from Chapter2.themes.symbolic_differentiation import is_a_number


def eq_zero(arg):
    if is_a_number(arg):
        return equals(arg, 0)
    return apply_generic(quote('eq_zero'), arg)


def run_the_magic():
    print('(=zero? 0)')
    print(eq_zero(0))

    print('(install-complex-package)')
    print('(install-rational-package)')
    install_complex_package()
    install_rational_package()

    print('(=zero? (make-rational 1 2))')
    print(eq_zero(make_rational(1, 2)))

    print('(=zero? (make-rational 0 2))')
    print(eq_zero(make_rational(0, 2)))

    print('(=zero? (make-complex-from-real-imag 1 2))')
    print(eq_zero(make_complex_from_real_imag(1, 2)))

    print('(=zero? (make-complex-from-real-imag 0 0))')
    print(eq_zero(make_complex_from_real_imag(0, 0)))


if __name__ == "__main__":
    run_the_magic()

