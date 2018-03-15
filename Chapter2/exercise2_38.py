# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.38
"""
from operator import add, mul, truediv

from Chapter2.lisp_list_structured_data import car, cdr, lisp_list, nil, print_lisp_list
from Chapter2.sequences_as_conventional_interfaces import accumulate as fold_right


def fold_left(op, initial, sequence):
    """Equivalent to accumulate (also known as fold_right)"""

    def iterate(result, rest):
        if rest is nil:
            return result
        return iterate(
            op(result, car(rest)),
            cdr(rest)
        )

    return iterate(initial, sequence)


def run_the_magic():
    print('(fold-right / 1 (list 1 2 3)')
    print(fold_right(truediv, 1, lisp_list(1, 2, 3)))
    print('(fold-left / 1 (list 1 2 3))')
    print(fold_left(truediv, 1, lisp_list(1, 2, 3)))
    print('(fold-right list nil (list 1 2 3))')
    print_lisp_list(fold_right(lisp_list, nil, lisp_list(1, 2, 3)))
    print('(fold-left list nil (list 1 2 3))')
    print_lisp_list(fold_left(lisp_list, nil, lisp_list(1, 2, 3)))
    print('To guarantee that fold-left and fold-right give the same result for any sequence, operator should be '
          'commutative (or independant of the order of the parameters) : (op a b) = (op b a). Examples:')
    print('(fold-right + 0 (list 1 2 3)')
    print(fold_right(add, 0, lisp_list(1, 2, 3)))
    print('(fold-left + 0 (list 1 2 3)')
    print(fold_left(add, 0, lisp_list(1, 2, 3)))
    print('(fold-right * 1 (list 1 2 3 4)')
    print(fold_right(mul, 1, lisp_list(1, 2, 3, 4)))
    print('(fold-left * 1 (list 1 2 3 4)')
    print(fold_left(mul, 1, lisp_list(1, 2, 3, 4)))


if __name__ == "__main__":
    run_the_magic()
