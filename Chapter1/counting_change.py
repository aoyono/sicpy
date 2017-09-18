# -*- coding: utf-8 -*-
"""
How many different ways can we make change of $ 1.00, given half-dollars, quarters, dimes, nickels, and pennies? More
generally, can we write a procedure to compute the number of ways to change any given amount of money?

Notes from the book:

1. Count-change generates a tree-recursive process with redundancies similar to those in our first implementation of fib.
(It will take quite a while for that 292 to be computed.) On the other hand, it is not obvious how to design a better
algorithm for computing the result, and we leave this problem as a challenge. The observation that a tree-recursive
process may be highly inefficient but often easy to specify and understand has led people to propose that one could
get the best of both worlds by designing a ``smart compiler'' that could transform tree-recursive procedures into more
efficient procedures that compute the same result.

2. One approach to coping with redundant computations is to arrange matters so that we automatically construct a table
of values as they are computed. Each time we are asked to apply the procedure to some argument, we first look to see if
the value is already stored in the table, in which case we avoid performing the redundant computation. This strategy,
known as tabulation or memoization, can be implemented in a straightforward way. Tabulation can sometimes be used to
transform processes that require an exponential number of steps (such as count-change) into processes whose space and
time requirements grow linearly with the input.
"""
from operator import eq, or_, lt, add, sub
from cachetools import LRUCache, cached


def count_change(amount):
    return cc(amount, 5)


# Adding the cached decorator improves drastically the timeit execution (see note 2 in the docstring about memoization)
@cached(LRUCache(maxsize=128))
def cc(amount, kinds_of_coins):
    if eq(amount, 0):
        return 1
    if or_(lt(amount, 0), eq(kinds_of_coins, 0)):
        return 0
    return add(
        cc(amount, sub(kinds_of_coins, 1)),
        cc(
            sub(
                amount,
                first_denomination(kinds_of_coins)
            ),
            kinds_of_coins
        )
    )


def first_denomination(kinds_of_coins):
    if eq(kinds_of_coins, 1):
        return 1
    if eq(kinds_of_coins, 2):
        return 5
    if eq(kinds_of_coins, 3):
        return 10
    if eq(kinds_of_coins, 4):
        return 25
    if eq(kinds_of_coins, 5):
        return 50

if __name__ == '__main__':
    from timeit import Timer
    timer = Timer(stmt="count_change(100)", setup="from __main__ import count_change")
    print(count_change(100))
    print("This response takes average time of %s seconds to compute" % (timer.timeit(),))
