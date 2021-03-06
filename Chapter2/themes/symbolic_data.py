# -*- coding: utf-8 -*-
"""
"""
import sympy

from Chapter2.themes.lisp_list_structured_data import car, cdr, lisp_list, nil
from Chapter2.themes.mapping_over_lists import map


def quote(symbols):
    """Python does not support symbolic data by design so we use sympy to
    emulate the behaviour"""
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


def symbol_equal(symbol1, symbol2):
    """Tests wether or not the two symbols are equal"""
    try:
        return symbol1.name == symbol2.name
    except AttributeError:
        return False


def memq(item, x):
    if x is nil:
        return False
    elif symbol_equal(item, car(x)):
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
