# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#%_thm_2.6
Church numerals
"""


def zero():
    return lambda f: lambda x: x


def add_1(n):
    return lambda f: lambda x: f(n(f)(x))


def one():
    """Given by the result of evaluating (add-1 zero) using the substitution model"""
    return lambda f: lambda x: f(x)


def two():
    """Given by the result of evaluating (add-1 one) using the substitution model"""
    return lambda f: lambda x: f(f(x))


def add(m, n):
    """Adding m and n is applying m times a procedure f to the result of applying n times f to its input"""
    return lambda f: lambda x: m(f)(
        n(f)(x)
    )


def run_the_magic():
    def greet(name):
        print('Hello %(name)s' % locals())
        return name

    print('Result of adding one and one, greeting a guy named Paul')
    add(one(), one())(greet)('Paul')
    print('Result of greeting two times a guy named Paul')
    two()(greet)('Paul')


if __name__ == '__main__':
    run_the_magic()
