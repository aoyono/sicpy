# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.45
"""
from utils import let
from Chapter2.themes.the_picture_language import beside, below


def split(lower, upper):
    def anon(painter, n):
        if n == 0:
            return painter
        with let(split(painter, n - 1)) as (smaller,):
            return lower(painter, upper(smaller, smaller))
    return anon


def right_split(painter, n):
    return split(beside, below)(painter, n)


def up_split(painter, n):
    return split(below, beside)(painter, n)


def run_the_magic():
    pass


if __name__ == '__main__':
    run_the_magic()
