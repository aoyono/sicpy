# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.73
"""
from Chapter2.themes.lisp_list_structured_data import (
    car, cdr, cadr,
    print_lisp_list,
)
from Chapter2.themes.representations_of_complex_numbers import attach_tag
from Chapter2.themes.symbolic_data import quote
from Chapter2.themes.symbolic_differentiation import (
    is_a_number, is_a_variable,
    same_variable,
    make_sum,
    make_product,
    make_exponentiation,
)
from utils import get, let, put


def deriv(exp, var):
    if is_a_number(exp):
        return 0
    if is_a_variable(exp):
        if same_variable(exp, var):
            return 1
        return 0
    return get(
        quote('deriv'),
        operator(exp),
    )(operands(exp), var)


def operator(exp):
    return car(exp)


def operands(exp):
    return cdr(exp)


# b.
def install_sum_rule():
    def deriv_sum_rule(operands, var):
        with let(car(operands), cadr(operands)) as (addend, augend):
            return make_sum(
                deriv(addend, var),
                deriv(augend, var))

    put(quote('deriv'),
        quote('+'),
        deriv_sum_rule)
    return quote('done')


def install_product_rule():
    def deriv_product_rule(operands, var):
        with let(car(operands), cadr(operands)) as (multiplier, multiplicand):
            return make_sum(
                make_product(
                    multiplier,
                    deriv(multiplicand, var)),
                make_product(
                    multiplicand,
                    deriv(multiplier, var)))

    put(quote('deriv'),
        quote('*'),
        deriv_product_rule)
    return quote('done')


# c.
def install_exponent_rule():
    def deriv_exponent_rule(operands, var):
        with let(car(operands), cadr(operands)) as (base, exponent):
            return make_product(
                make_product(
                    exponent,
                    make_exponentiation(
                        base,
                        make_sum(
                            exponent,
                            quote('-1')))),
                deriv(base, var))

    put(quote('deriv'),
        quote('**'),
        deriv_exponent_rule)
    return quote('done')


def run_the_magic():
    print("""
        a. The derivation rules have been abstracted using data-directed 
        programming, so that they can be developed in isolation of deriv.
        The predicates number? and same-variable? can't be assimilated into the
        data-directed dispatch because they are special rules (or invariants) 
        that we want to make sure are respected no matter what.
    """)

    print(install_sum_rule())
    print(install_product_rule())
    print(install_exponent_rule())
    print(deriv(
        make_sum(quote('x'), quote('3')),
        quote('x')))
    print(deriv(
        make_product(quote('x'), quote('y')),
        quote('x')))
    print_lisp_list(deriv(
        make_product(make_product(quote('x'), quote('y')), make_sum(
            quote('x'), quote('3'))),
        quote('x')))
    print_lisp_list(deriv(
        make_exponentiation(
            make_sum(quote('x'), quote('y')),
            quote('y')),
        quote('x')))

    print("""
            d. If the index were to change, we would only need to change the
            the call to `put` in the installation of rules
        """)


if __name__ == "__main__":
    run_the_magic()

