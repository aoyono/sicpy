# -*- coding: utf-8 -*-
"""
There is a clever algorithm for computing the Fibonacci numbers in a logarithmic number of steps. Recall the
transformation of the state variables a and b in the fib-iter process of section 1.2.2: a <- a + b and b <- a. Call this
transformation T, and observe that applying T over and over again n times, starting with 1 and 0, produces the pair
Fib(n + 1) and Fib(n). In other words, the Fibonacci numbers are produced by applying T^n, the nth power of the
transformation T, starting with the pair (1,0). Now consider T to be the special case of p = 0 and q = 1 in a family of
transformations T_pq, where T_pq transforms the pair (a,b) according to a <- bq + aq + ap and b <- bp + aq. Show that if
we apply such a transformation T_pq twice, the effect is the same as using a single transformation T_p'q' of the same
form, and compute p' and q' in terms of p and q. This gives us an explicit way to square these transformations, and thus
we can compute T^n using successive squaring, as in the fast-expt procedure. Put this all together to complete the
following procedure, which runs in a logarithmic number of steps:

(define (fib n)
  (fib-iter 1 0 0 1 n))
(define (fib-iter a b p q count)
  (cond ((= count 0) b)
        ((even? count)
         (fib-iter a
                   b
                   <??>      ; compute p'
                   <??>      ; compute q'
                   (/ count 2)))
        (else (fib-iter (+ (* b q) (* a q) (* a p))
                        (+ (* b p) (* a q))
                        p
                        q
                        (- count 1)))))
"""
from operator import eq, add, mul, truediv, sub

from Chapter1.compound_procedures import square
from Chapter1.exponentiation import is_even


def fib(n):
    def fib_iter(a, b, p, q, count):
        if eq(count, 0):
            return b
        if is_even(count):
            return fib_iter(
                a,
                b,
                add(square(p), square(q)),
                add(mul(2, mul(p, q)), square(q)),
                truediv(count, 2)
            )
        return fib_iter(
            add(
                add(mul(b, q), mul(a, q)),
                mul(a, p)
            ),
            add(
                mul(b, p),
                mul(a, q)
            ),
            p,
            q,
            sub(count, 1)
        )
    return fib_iter(1, 0, 0, 1, n)


if __name__ == '__main__':
    from timeit import Timer

    n = 20

    timer = Timer(stmt='fib(%(n)s)' % locals(), setup='from __main__ import fib')
    print('(fib %(n)s)' % locals(), fib(n), 'Time: %s' % (timer.timeit(),), sep='\n')

    from Chapter1.tree_recursion import fib_iterative
    timer = Timer(stmt='fib_iterative(%(n)s)' % locals(), setup='from __main__ import fib_iterative')
    print('(fib-iterative %(n)s)' % locals(), fib_iterative(n), 'Time: %s' % (timer.timeit(),), sep='\n')

    def time_generator():
        for p in range(n):
            yield Timer(stmt='fib(%(p)s)' % locals(), setup='from __main__ import fib').timeit()

    ns = [p for p in range(n + 1)]
    times_fib = [
        Timer(stmt='fib(%(p)s)' % locals(), setup='from __main__ import fib').timeit()
        for p in ns
    ]
    times_fibi = [
        Timer(stmt='fib_iterative(%(p)s)' % locals(), setup='from __main__ import fib_iterative').timeit()
        for p in ns
    ]

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.scatter(ns, times_fib, c='red', label='fib')
    ax.scatter(ns, times_fibi, c='blue', label='fib-iterative')
    ax.legend()

    plt.xlabel('n')
    plt.ylabel('mean computation time (s)')

    plt.show()
