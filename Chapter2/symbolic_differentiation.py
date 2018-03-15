# -*- coding: utf-8 -*-
"""
"""
import sympy

from Chapter2.hierarchical_structures import pair
from Chapter2.lisp_list_structured_data import caddr, cadr, car, lisp_list, print_lisp_list
from Chapter2.symbolic_data import quote, seq
from utils import error, let


def is_symbol(s):
    return isinstance(s, sympy.Symbol)


def is_a_variable(e):
    return is_symbol(e)


def same_variable(v1, v2):
    return is_a_variable(v1) and is_a_variable(v2) and seq(v1, v2)


def is_a_sum(e):
    return pair(e) and seq(car(e), quote('+'))


def addend(e):
    return cadr(e)


def augend(e):
    return caddr(e)


def make_sum(a1, a2):
    if eq_number(a1, 0):
        return a2
    if eq_number(a2, 0):
        return a1
    if is_a_number(a1) and is_a_number(a2):
        return a1 + a2
    return lisp_list(
        quote('+'),
        a1,
        a2
    )


def is_a_product(e):
    return pair(e) and seq(car(e), quote('*'))


def multiplier(e):
    return cadr(e)


def multiplicand(e):
    return caddr(e)


def make_product(m1, m2):
    if eq_number(m1, 0) or eq_number(m2, 0):
        return 0
    if eq_number(m1, 1):
        return m2
    if eq_number(m2, 1):
        return m1
    if is_a_number(m1) and is_a_number(m2):
        return m1 * m2
    return lisp_list(
        quote('*'),
        m1,
        m2
    )


def is_a_number(e):
    try:
        return isinstance(e, int) or isinstance(e, float) or e.is_number
    except AttributeError:
        return False


def eq_number(exp, num):
    return is_a_number(exp) and exp == num


def deriv(exp, var):
    if is_a_number(exp):
        return 0
    if is_a_variable(exp):
        if same_variable(exp, var):
            return 1
        return 0
    if is_a_sum(exp):
        return make_sum(
            deriv(addend(exp), var),
            deriv(augend(exp), var),
        )
    # From exercise 2.56
    if is_exponentiation(exp):
        with let(exponent(exp), base(exp)) as (expo, baz):
            return make_product(
                make_product(
                    expo,
                    make_exponentiation(
                        baz,
                        make_sum(
                            expo,
                            quote('-1')
                        )
                    )
                ),
                deriv(baz, var)
            )
    if is_a_product(exp):
        return make_sum(
            make_product(
                multiplier(exp),
                deriv(multiplicand(exp), var)
            ),
            make_product(
                deriv(multiplier(exp), var),
                multiplicand(exp)
            )
        )
    error("unknown expression type -- DERIV", exp)


# Exercise 2.56

def is_exponentiation(expr):
    return pair(expr) and seq(car(expr), quote('**'))


def base(expr):
    return cadr(expr)


def exponent(expr):
    return caddr(expr)


def make_exponentiation(base, exponent):
    if eq_number(exponent, 0):
        return 1
    if eq_number(exponent, 1):
        return base
    return lisp_list(
        quote('**'),
        base,
        exponent
    )


def run_the_magic():
    print(deriv(
        make_sum(quote('x'), quote('3')),
        quote('x')
    ))

    print(deriv(
        make_product(quote('x'), quote('y')),
        quote('x')
    ))

    print_lisp_list(deriv(
        make_product(make_product(quote('x'), quote('y')), make_sum(quote('x'), quote('3'))),
        quote('x')
    ))

    # Testing exercise 2.56
    print_lisp_list(deriv(
        make_exponentiation(
            make_sum(quote('x'), quote('y')),
            quote('y')
        ),
        quote('x')
    ))


if __name__ == '__main__':
    run_the_magic()
