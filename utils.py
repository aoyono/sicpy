# -*- coding: utf-8 -*-
import turtle
from contextlib import contextmanager



@contextmanager
def let(*args):
    try:
        yield args
    finally:
        del args


def error(*args):
    print(*args)


board = turtle.Screen()
board.setup(width=500, height=500)
board.title('The picture language - SICP')

