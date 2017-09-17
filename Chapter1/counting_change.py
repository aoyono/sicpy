# -*- coding: utf-8 -*-
"""
How many different ways can we make change of $ 1.00, given half-dollars, quarters, dimes, nickels, and pennies? More
generally, can we write a procedure to compute the number of ways to change any given amount of money?
"""
from operator import eq, or_, lt, add, sub


def count_change(amount):
    return cc(amount, 5)


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
    print(count_change(100))