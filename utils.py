# -*- coding: utf-8 -*-
from contextlib import contextmanager


@contextmanager
def let(*args):
    try:
        yield args
    finally:
        del args


def error(*args):
    print(*args)
    raise Exception
