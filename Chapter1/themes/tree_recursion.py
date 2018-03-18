# -*- coding: utf-8 -*-
from operator import eq, add, sub


def fib_recursive(n):
    """Computing the n-th Fibonnaci with a tree-recursive process.

    In general, the evolved process looks like a tree [...] Notice that the branches split into two
    at each level (except at the bottom); this reflects the fact that the fib procedure calls itself twice each time it
    is invoked.
    The process uses a number of steps that grows exponentially with the input. On the other hand, the space required
    grows only linearly with the input, because we need keep track only of which nodes are above us in the tree at any
    point in the computation. In general, the number of steps required by a tree-recursive process will be proportional
    to the number of nodes in the tree, while the space required will be proportional to the maximum depth of the tree.
    """
    if eq(n, 0):
        return 0
    if eq(n, 1):
        return 1
    res1 = fib_recursive(sub(n, 1))
    res2 = fib_recursive(sub(n, 2))
    return add(res1, res2)


def fib_iterative(n):
    """Computing the n-th Fibonnaci with an iterative process"""
    def fib_iter(a, b, count):
        if eq(count, 0):
            return b
        return fib_iter(
            add(a, b),
            a,
            sub(count, 1)
        )
    return fib_iter(1, 0, n)


def run_the_magic():
    from timeit import Timer

    timer_LR = Timer(stmt='fib_recursive(5)', setup='from Chapter1.tree_recursion import fib_recursive')
    timer_LI = Timer(stmt='fib_iterative(5)', setup='from Chapter1.tree_recursion import fib_iterative')

    print('fib(5) (recursive) = {}'.format(fib_recursive(5)), 'fib(5) (iterative) = {}'.format(fib_iterative(5)),
          sep='\n')

    print('Execution times: \n\t- recursive: %s\n\t- iterative: %s' % (timer_LR.timeit(), timer_LI.timeit()))


if __name__ == '__main__':
    run_the_magic()
