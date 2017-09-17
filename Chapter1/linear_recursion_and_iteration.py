# -*- coding: utf-8 -*-
from operator import add, eq, gt, mul, sub


def factorial_recursive(n, s=[]):
    """Linear recursive process for computing factorials.

    The substitution model reveals a shape of expansion followed by contraction. [...] The expansion occurs as the
    process builds up a chain of deferred operations (in this case, a chain of multiplications). The contraction occurs
    as the operations are actually performed. This type of process, characterized by a chain of deferred operations, is
    called a recursive process. Carrying out this process requires that the interpreter keep track of the operations to
    be performed later on. In the computation of n!, the length of the chain of deferred multiplications, and hence the
    amount of information needed to keep track of it, grows linearly with n (is proportional to n), just like the number
    of steps. Such a process is called a linear recursive process.
    """
    if eq(n, 1):
        return 1    # Start to shrink
    print_shape(n, None, s)
    fact_n_minus_one = factorial_recursive(sub(n, 1))   # building the chain of deferred operations (expansion)
    print_shape(n, fact_n_minus_one, s)
    return mul(n, fact_n_minus_one)     # shrinking continue here


def print_shape(n, fact_n_minus_one, s):
    """Print the shape of the linear recursive process of computing factorial"""
    import re

    def print_after():
        m = re.search(r'\(factorial 1\)', s[0])
        if m is None:
            m = re.search(r'\(\* ([0-9]+) ([0-9]+)\)', s[0])
        str2print = (
            s[0][0:m.start()]
            + str(fact_n_minus_one)
            + s[0][m.end():]
        )
        s[0] = str2print
        print(s[0])

    def print_before():
        base = '(* {} {})'
        if not s:
            s.append(base.format(n, '(factorial %s)' % (sub(n, 1),)))
        else:
            m = re.search(r'\(factorial ([0-9]+)\)', s[0])
            str2print = (
                s[0][0:m.start()]
                + base.format(n, '(factorial %s)' % (sub(n, 1),))
                + s[0][m.end():]
            )
            s[0] = str2print
        print(s[0])
    if fact_n_minus_one is not None:
        print_after()
    else:
        print_before()


def factorial_iterative(n):
    """Linear iterative process for computing factorials.

    In general, an iterative process is one whose state can be summarized by a fixed number of state variables, together
    with a fixed rule that describes how the state variables should be updated as the process moves from state to state
    and an (optional) end test that specifies conditions under which the process should terminate. In computing n!, the
    number of steps required grows linearly with n. Such a process is called a linear iterative process.
    """
    def fact_iter(product, counter, max_count):
        if gt(counter, max_count):      # Monitor the state of the process
            print('(fact-iter %(product)s %(counter)s %(max_count)s)' % locals())
            return product
        print('(fact-iter %(product)s %(counter)s %(max_count)s)' % locals())
        return fact_iter(
            mul(counter, product),  # Evolve the state of the process
            add(counter, 1),
            max_count
        )
    return fact_iter(1, 1, n)


if __name__ == '__main__':
    n = 5
    print('linear-recursive process:', '(factorial {})'.format(n), sep='\n', )
    result = factorial_recursive(n)
    print('{}'.format(result))
    print('linear-iterative process:', '(factorial {})'.format(n), sep='\n')
    result = factorial_iterative(n)
    print('{}'.format(result))
