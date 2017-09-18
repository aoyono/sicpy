# -*- coding: utf-8 -*-
"""
The following pattern of numbers is called Pascal's triangle.
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1
       ...
The numbers at the edge of the triangle are all 1, and each number inside the triangle is the sum of the two numbers
above it. Write a procedure that computes elements of Pascal's triangle by means of a recursive process.
"""
from operator import sub


def pascal_triangle_recursive(line, column):
    if any(val == 0 for val in (line, column)):
        return 'line and column should be strictly positive'
    if column > line:
        return 'column should be at most equal to line'
    if line == 1:
        return 1
    if column == 1:
        return 1
    if line == column:
        return 1
    return pascal_triangle_recursive(sub(line, 1), column) + pascal_triangle_recursive(sub(line, 1), sub(column, 1))


if __name__ == '__main__':
    line, column = 1, 3
    print(
        '(pascal-recursive %(line)s %(column)s)' % locals(),
        pascal_triangle_recursive(line, column),
        sep='\n',
    )
