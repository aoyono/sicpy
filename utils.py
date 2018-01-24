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

