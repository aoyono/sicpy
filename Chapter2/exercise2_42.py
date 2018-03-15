# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.42
"""
from Chapter2.lisp_list_structured_data import (
    append, cadr, car, cdr, lisp_list, list_ref, nil, print_lisp_list, rlength,
)
from Chapter2.mapping_over_lists import map
from Chapter2.nested_mappings import flatmap
from Chapter2.sequences_as_conventional_interfaces import enumerate_interval, filter
from utils import let


def queens(board_size):
    def queen_cols(k):
        if k == 0:
            return lisp_list(empty_board())
        return filter(
            lambda positions: is_safe(k, positions),
            flatmap(
                lambda rest_of_queens: map(
                    lambda new_row: adjoin_position(new_row, k, rest_of_queens),
                    enumerate_interval(1, board_size)
                ),
                queen_cols(k - 1)
            )
        )

    return queen_cols(board_size)


def empty_board():
    return nil


def is_safe(col, positions):
    def is_safe_pair(p1, p2):
        with let(car(p1), cadr(p1), car(p2), cadr(p2)) as (r1, c1, r2, c2):
            return not (
                    r1 == r2 or
                    r1 - c1 == r2 - c2 or
                    r1 + c1 == r2 + c2
            )

    return all_n(
        col - 1,
        lambda p: is_safe_pair(p, last(positions)),
        positions
    )


def adjoin_position(row, col, rest_of_queens):
    return append(
        rest_of_queens,
        lisp_list(lisp_list(row, col))
    )


def all_n(n, pred, items):
    def iterate(i, items):
        if i == n:
            return True
        if pred(car(items)):
            return iterate(i + 1, cdr(items))
        return False

    return iterate(0, items)


def last(positions):
    return list_ref(positions, rlength(positions) - 1)


def run_the_magic():
    board_size = 6
    print_lisp_list(queens(board_size))


if __name__ == "__main__":
    run_the_magic()
