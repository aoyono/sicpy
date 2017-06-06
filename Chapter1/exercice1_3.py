# -*- coding: utf-8 -*-
"""
Define a procedure that takes three numbers as arguments and returns
the sum of the squares of the two larger numbers.
"""
from Chapter1.compound_procedures import sum_of_squares


def sum_of_squares_of_two_larger(number1, number2, number3):
    return sum_of_squares(
        *two_larger(number1, number2, number3)
    )


def two_larger(number1, number2, number3):
    return sorted((number1, number2, number3))[1:]


if __name__ == '__main__':
    print('The sum of squares of the two larger between (5, 13, 27): %s'
          % (sum_of_squares_of_two_larger(5, 13, 27),))
