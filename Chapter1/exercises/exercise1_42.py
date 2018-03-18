# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%_thm_1.42
"""
from Chapter1.themes.compound_procedures import square
from Chapter1.exercises.exercise1_9 import inc


def compose(f, g):
    return lambda x: f(g(x))


def run_the_magic():
    f, g, x = square, inc, 6
    print('((compose %s %s) %s)' % (f.__name__, g.__name__, x))
    print(compose(f, g)(x))


if __name__ == '__main__':
    run_the_magic()
