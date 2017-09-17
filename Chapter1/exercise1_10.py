# -*- coding: utf-8 -*-
"""
The following procedure computes a mathematical function called Ackermann's function.

(define (A x y)
  (cond ((= y 0) 0)
        ((= x 0) (* 2 y))
        ((= y 1) 2)
        (else (A (- x 1)
                 (A x (- y 1))))))

What are the values of the following expressions?

(A 1 10)

(A 2 4)

(A 3 3)

Consider the following procedures, where A is the procedure defined above:

(define (f n) (A 0 n))

(define (g n) (A 1 n))

(define (h n) (A 2 n))

(define (k n) (* 5 n n))

Give concise mathematical definitions for the functions computed by the procedures f, g, and h for positive integer
values of n. For example, (k n) computes 5n².
"""
from operator import eq, mul, sub


def ackermann(x, y):
    if eq(y, 0):
        return 0
    elif eq(x, 0):
        return mul(2, y)
    elif eq(y, 1):
        return 2
    else:
        return ackermann(
            sub(x, 1),
            ackermann(
                x,
                sub(y, 1)
            )
        )


def f(n):
    """f(n) = 2n"""
    return ackermann(0, n)


def g(n):
    """g(n) = 2^n"""
    return ackermann(1, n)


def h(n):
    return ackermann(2, n)


if __name__ == '__main__':
    print("(A 1 10)", ackermann(1, 10), sep='\n')
    print("(A 2 4)", ackermann(2, 4), sep='\n')
    print("(A 3 3)", ackermann(3, 3), sep='\n')

    print('---------------------------------------------------------------')
    for func in (f, g, h):
        # Limiting tests to up to 4. Note that CPython isn't optimized for tail-recursion, as it is not an exclusively
        # functional language (see the answer here:
        # https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
        for i in range(5):
            print("({f.__name__} {i})".format(f=func, i=i), func(i), sep='\n')
        print('---------------------------------------------------------------')
    print(ackermann(3, 1))