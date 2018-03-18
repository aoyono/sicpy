# -*- coding: utf-8 -*-
"""
A function f is defined by the rule that f(n) = n if n<3 and f(n) = f(n - 1) + 2f(n - 2) + 3f(n - 3) if n> 3. Write a
procedure that computes f by means of a recursive process. Write a procedure that computes f by means of an iterative
process.
"""
from operator import lt, sub, add, mul


def f_recursive(n):
    if lt(n, 3):
        return n
    r1 = f_recursive(sub(n, 1))
    r2 = f_recursive(sub(n, 2))
    r3 = f_recursive(sub(n, 3))
    return add(
        add(r1, mul(2, r2)),
        mul(3, r3)
    )


def f_iterative(n):
    def f_iter(a, b, c, count):
        if count == 0:
            return c
        return f_iter(
            add(
                add(a, mul(2, b)),
                mul(3, c)
            ),
            a,
            b,
            sub(count, 1),
        )
    return f_iter(2, 1, 0, n)


def run_the_magic():
    N = 5
    from timeit import Timer
    for n in range(N + 1):
        print('n = %(n)s' % locals())
        print('(f-recursive %(n)s)' % locals(), f_recursive(n), sep='\n')
        print('(f-iterative %(n)s)' % locals(), f_iterative(n), sep='\n')

        timer_rec = Timer(stmt="f_recursive(%(n)s)" % locals(), setup="from Chapter1.exercise1_11 import f_recursive")
        timer_iter = Timer(stmt="f_iterative(%(n)s)" % locals(), setup="from Chapter1.exercise1_11 import f_iterative")
        print(
            'Mean execution time:',
            '\t-(f-recursive %(n)s): {}'.format(timer_rec.timeit()) % locals(),
            '\t-(f-iterative %(n)s): {}'.format(timer_iter.timeit()) % locals(),
            sep='\n',
        )
        print('-' * 20)


if __name__ == '__main__':
    run_the_magic()
