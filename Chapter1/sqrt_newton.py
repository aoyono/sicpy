from operator import add, truediv, lt, sub

from Chapter1.compound_procedures import square
from Chapter1.lisp_conditionals import lisp_abs


def sqrt_iter(guess, x):
    """/!\ RecursionError rqised when using lisp_if"""
    if is_good_enough(guess, x):
        return guess
    return sqrt_iter(improve(guess, x), x)
    # return lisp_if(
    #     is_good_enough(guess, x),
    #     guess,
    #     sqrt_iter(improve(guess, x), x)
    # )


def improve(guess, x):
    return average(
        guess,
        truediv(x, guess)
    )


def average(x, y):
    return truediv(
        add(x, y),
        2
    )


def is_good_enough(guess, x):
    return lt(
        lisp_abs(sub(square(guess), x)),
        0.001
    )


def sqrt(x):
    return sqrt_iter(1.0, x)


if __name__ == '__main__':
    print('%s\n%s\n%s\n%s\n' %
          (sqrt(9),
           sqrt(add(100, 37)),
           sqrt(add(sqrt(2), sqrt(3))),
           square(sqrt(1000)))
          )
