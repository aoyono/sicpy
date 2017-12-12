# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.19
"""
from cachetools import LRUCache, cached

from Chapter2.lisp_list_structured_data import car, cdr, length, lisp_list


def us_coins(): return lisp_list(50, 25, 10, 5, 1)


def uk_coins(): return lisp_list(100, 50, 20, 10, 5, 2, 1, 0.5)


@cached(LRUCache(maxsize=128))
def cc(amount, coin_values):
    if amount == 0:
        return 1
    if amount < 0 or no_more(coin_values):
        return 0
    return (cc(
        amount,
        except_first_denomination(coin_values)) + cc(
        amount - first_denomination(coin_values),
        coin_values
    ))


def no_more(coin_values):
    return length(coin_values) == 0


def except_first_denomination(coin_values):
    return cdr(coin_values)


def first_denomination(coin_values):
    return car(coin_values)


def run_the_magic():
    print('(cc 100 us-coins)')
    print(cc(100, us_coins()))


if __name__ == '__main__':
    run_the_magic()
