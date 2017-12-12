# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%_thm_1.41
"""
from Chapter1.exercise1_9 import inc


def double(proc):
    return lambda x: proc(proc(x))


def run_the_magic():
    print(
        '((double inc) 1)',
        double(inc)(1),
        sep='\n'
    )
    print(
        '(((double (double double)) inc) 5)',
        double(double(double))(inc)(5),
        sep='\n'
    )


if __name__ == '__main__':
    run_the_magic()
