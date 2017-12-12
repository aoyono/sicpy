# -*- coding: utf-8 -*-
"""
Using the results of exercises 1.16 and 1.17, devise a procedure that generates an iterative process for multiplying two
integers in terms of adding, doubling, and halving and uses a logarithmic number of steps.

Note from the book:

This algorithm, which is sometimes known as the ``Russian peasant method'' of multiplication, is ancient. Examples of
its use are found in the Rhind Papyrus, one of the two oldest mathematical documents in existence, written about 1700
B.C. (and copied from an even older document) by an Egyptian scribe named A'h-mose.
"""
from operator import eq, add, sub

from Chapter1.exercise1_17 import double, fast_multiply, halve
from Chapter1.exponentiation import is_even


def mult(a, b):
    def mult_iter(first, counter, sum):
        if eq(counter, 0):
            return sum
        if is_even(counter):
            return mult_iter(
                double(first),
                halve(counter),
                sum
            )
        return mult_iter(
            first,
            sub(counter, 1),
            add(first, sum)
        )
    return mult_iter(a, b, 0)


def run_the_magic():
    from timeit import Timer
    b, n = 10, 1000
    timer = Timer(stmt='mult(%(b)s, %(n)s)' % locals(), setup='from Chapter1.exercise1_18 import mult')
    print('(* %(b)s %(n)s)' % locals(), mult(b, n), 'Time: %s' % (timer.timeit(),), sep='\n')

    timer = Timer(stmt='fast_multiply(%(b)s, %(n)s)' % locals(), setup='from Chapter1.exercise1_18 import fast_multiply')
    print('(fast-multiply %(b)s %(n)s)' % locals(), fast_multiply(b, n), 'Time: %s' % (timer.timeit(),), sep='\n')


if __name__ == '__main__':
    run_the_magic()
