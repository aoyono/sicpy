from operator import add, lt, sub, truediv

from Chapter1.themes.compound_procedures import square
from Chapter1.themes.lisp_conditionals import lisp_abs


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


def sqrt_unified(x):
    """A version of sqrt embedding its intermediate steps: block structure
    """

    def is_good_enough(guess, x):
        return lt(
            lisp_abs(sub(square(guess), x)),
            0.001
        )

    def average(x, y):
        return truediv(
            add(x, y),
            2
        )

    def improve(guess, x):
        return average(
            guess,
            truediv(x, guess)
        )

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

    return sqrt_iter(1.0, x)


def sqrt_unified_ls(x):
    """A version of sqrt embedding its intermediate steps and not passing x as a parameter to steps: lexical scoping
    """

    def is_good_enough(guess):
        return lt(
            lisp_abs(sub(square(guess), x)),
            0.001
        )

    def average(x, y):
        return truediv(
            add(x, y),
            2
        )

    def improve(guess):
        return average(
            guess,
            truediv(x, guess)
        )

    def sqrt_iter(guess):
        """/!\ RecursionError rqised when using lisp_if"""
        if is_good_enough(guess):
            return guess
        return sqrt_iter(improve(guess))
        # return lisp_if(
        #     is_good_enough(guess, x),
        #     guess,
        #     sqrt_iter(improve(guess, x), x)
        # )

    return sqrt_iter(1.0)


def run_the_magic():
    print('(sqrt 9) : %s\n(sqrt (+ 100 37)) : %s\n(sqrt (+ (sqrt 2) (sqrt 3))) : %s\n(square (sqrt 1000)) : %s\n' % (
        sqrt(9),
        sqrt(add(100, 37)),
        sqrt(add(sqrt(2), sqrt(3))),
        square(sqrt(1000))
    ))
    print(
        "With internal block structure:",
        "(square (sqrt_unified 1000)) : {}".format(square(sqrt_unified(1000)),),
        "(square (sqrt_unified_ls 1000)) : {}".format(square(sqrt_unified_ls(1000)),),
        sep='\n',
    )


if __name__ == '__main__':
    run_the_magic()
