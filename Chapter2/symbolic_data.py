# -*- coding: utf-8 -*-
"""
"""
import sympy

from Chapter2.lisp_list_structured_data import nil, car, cdr, lisp_list
from Chapter2.mapping_over_lists import map


def quote(symbols):
    """Python does not support symbolic data by design so we use sympy to emulate the behaviour"""
    if isinstance(symbols, str):
        try:
            int(symbols)
        except ValueError:
            try:
                float(symbols)
            except ValueError:
                return sympy.var(symbols)
            else:
                return sympy.RealNumber(symbols)
        else:
            return sympy.Integer(symbols)
    return map(quote, symbols)


def seq(symbol1, symbol2):
    """Tests wether or not the two symbols are equal"""
    try:
        return symbol1.name == symbol2.name
    except AttributeError:
        return False


def memq(item, x):
    if x is nil():
        return False
    elif seq(item, car(x)):
        return x
    else:
        return memq(item, cdr(x))


def run_the_magic():
    print(memq(
        quote('apple'),
        quote(lisp_list('pear', 'banana', 'prune'))
    ))

    print(memq(
        quote('apple'),
        quote(lisp_list(
            'x',
            lisp_list(
                'apple',
                'sauce',
            ),
            'y',
            'apple',
            'pear',
        ))
    ))


if __name__ == '__main__':
    run_the_magic()
