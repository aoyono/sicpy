# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%_thm_1.46
"""
from operator import lt, sub

from Chapter1.themes.procedures_as_general_methods import tolerance
from Chapter1.themes.sqrt_newton import improve, is_good_enough


def iterative_improve_naive(good_enough, improve):
    def proceed(guess):
        if good_enough(guess):
            return guess
        return proceed(improve(guess))

    return proceed


def iterative_improve(good_enough, improve):
    return lambda guess: (
        guess
        if good_enough(guess)
        else
        iterative_improve(good_enough, improve)(improve(guess))
    )


def sqrt(x):
    return iterative_improve(
        lambda guess: is_good_enough(guess, x),
        lambda guess: improve(guess, x)
    )(1.0)


def fixed_point(f, first_guess):
    return iterative_improve(
        lambda guess: lt(abs(sub(guess, f(guess))), tolerance()),
        f
    )(first_guess)