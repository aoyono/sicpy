# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-4.html#%_toc_%_sec_2.1.4

We aggregate here the exercises from 2.7 up to 2.16
"""
from Chapter2.themes.lisp_list_structured_data import car, cdr, cons
from utils import error, let


def add_interval(x, y):
    return make_interval(
        lower_bound(x) + lower_bound(y),
        upper_bound(x) + upper_bound(y)
    )


def mul_interval(x, y):
    with let(
                    lower_bound(x) * lower_bound(y),
                    lower_bound(x) * upper_bound(y),
                    upper_bound(x) * lower_bound(y),
                    upper_bound(x) * upper_bound(y)
    ) as (p1, p2, p3, p4):
        return make_interval(
            min(p1, p2, p3, p4),
            max(p1, p2, p3, p4)
        )


def div_interval(x, y):
    if width(y) == 0:
        error('Division by interval that spans 0 is an error')
        raise ZeroDivisionError
    return mul_interval(
        x,
        make_interval(
            1.0 / upper_bound(y),
            1.0 / lower_bound(y)
        )
    )


# Exercise2.7
def make_interval(a, b):
    return cons(a, b)


def lower_bound(x):
    return min(
        car(x),
        cdr(x)
    )


def upper_bound(x):
    return max(
        car(x),
        cdr(x)
    )


# Exercise2.8
def sub_interval(x, y):
    return add_interval(
        x,
        make_interval(
            - lower_bound(y),
            - upper_bound(y)
        )
    )


# Exercise2.9
def width(x):
    """Defining width by its trivial definition"""
    return (upper_bound(x) - lower_bound(x)) / 2


def width2(x):
    """Defining width by the development of its trivial definition using definition of max function for real numbers.
    See https://fr.wikipedia.org/wiki/Extremum#Exemples
    """
    return abs(car(x) - cdr(x)) / 2


def show_that_width_x_plus_y_is_a_function_of_widths_of_x_and_y():
    """Showing that width(x + y) is a function of width(x) and width(y).
    Use second definition of width, and the fact that:
    car(x + y) = lower_bound(x) + lower_bound(y)
    cdr(x + y) = upper_bound(x) + upper_bound(y)
    """
    with let(make_interval(3, 2), make_interval(-1, 9)) as (x, y):
        with let(width(add_interval(x, y)), width2(add_interval(x, y))) as (w1, w2):
            assert w1 == w2  # Shows the equivalence between the 2 defs of width
            assert w1 == width(x) + width(y)


# Exercise2.10 -> see function div_interval


# Exercise2.11
def mul_interval2(x, y):
    pass

# End Exercise2.11


def make_center_width(c, w):
    return make_interval(
        c - w,
        c + w
    )


def center(i):
    return (lower_bound(i) + upper_bound(i)) / 2


# Exercise2.12
def make_center_percent(c, p):
    with let(c * p / 100) as (w,):
        return make_center_width(c, w)


def percent(i):
    with let(width(i), center(i)) as (w, c):
        return 100 * w / c


# Exercise2.13
# End Exercice2.13


def par1(r1, r2):
    """Computes equivalent resistance of parallel resistors with R1R2/(R1 + R2)"""
    return div_interval(
        mul_interval(r1, r2),
        add_interval(r1, r2)
    )


def par2(r1, r2):
    """Computes equivalent resistance of parallel resistors with 1/(1/R1 + 1/R2)"""
    with let(make_interval(1, 1)) as (one,):
        return div_interval(
            one,
            add_interval(
                div_interval(one, r1),
                div_interval(one, r2)
            )
        )


# Exercise2.14
def demonstrate_that_lem_is_rigth():
    with let(make_interval(4.95, 5.05), make_interval(9.99, 10.01)) as (r1, r2):
        assert par1(r1, r2) != par2(r1, r2)
        print(par1(r1, r2))
        print(par2(r1, r2))
    print('-------------------------------------------------------------------')

    with let(make_center_width(5, 0.05), make_center_width(10, 0.01)) as (A, B):
        print(div_interval(A, A))
        print(div_interval(A, B))
        print(par1(A, B))
        print(par2(A, B))
        assert par1(A, B) != par2(A, B)
    print('-------------------------------------------------------------------')

    with let(make_center_percent(5, 0.01), make_center_percent(10, 0.01)) as (A, B):
        print(div_interval(A, A))
        print(div_interval(A, B))
        print(par1(A, B))
        print(par2(A, B))
        assert par1(A, B) != par2(A, B)
# End Exercise2.14


# Exercise2.15
"""
Approximation errors that come with uncertain numbers grow when they are repeated in an algebraic relation.
Thus minimising such repetitions may produce results with lesser approx. errors
"""
# End Exercise2.15


# Exercise2.16
"""
See https://en.wikipedia.org/wiki/Interval_arithmetic#Dependency_problem
"""
# End Exercise2.16


def run_the_magic():
    show_that_width_x_plus_y_is_a_function_of_widths_of_x_and_y()
    demonstrate_that_lem_is_rigth()


if __name__ == '__main__':
    run_the_magic()
