# -*- coding: utf-8 -*-
"""
Demonstrate that the Carmichael numbers listed in footnote 47 really do fool the Fermat test. That is, write a procedure
that takes an integer n and tests whether a^n is congruent to a modulo n for every a<n, and try your procedure on the
given Carmichael numbers.
"""
from operator import eq, sub

from Chapter1.tfp_the_fermat_test import expmod


def fools_fermat_test(n):
    """Lisp-like iteration"""
    def try_it(a):
        return eq(
            expmod(a, n, n),
            a
        )

    if eq(n, 1):
        return True
    if try_it(sub(n, 1)):
        return fools_fermat_test(sub(n, 2))
    return False


def fools_fermat_test2(n):
    """Python-like iteration. This avoids to exceed Python recursion limit"""
    for p in range(1, n):
        if not expmod(p, n, n) == p:
            return False
    return True


def run_the_magic():
    carmichael_numbers = [
        561,
        1105,
        1729,
        2465,
        2821,
        6601,
    ]

    for n in carmichael_numbers:
        try:
            print(fools_fermat_test(n))
        except RecursionError:
            print(fools_fermat_test2(n))


if __name__ == '__main__':
    run_the_magic()
