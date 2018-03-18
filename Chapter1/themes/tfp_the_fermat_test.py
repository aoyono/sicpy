# -*- coding: utf-8 -*-
"""
Fermat's Little Theorem:
If n is a prime number and a is any positive integer less than n, then a raised to the nth power is congruent to a
modulo n.
"""
import random
from operator import eq, mod, truediv, sub, mul

from Chapter1.themes.compound_procedures import square
from Chapter1.themes.exponentiation import is_even


def expmod(base, exp, m):
    """Computes the remainder of base^exp modulo m

    Note 46 from the book:
    The reduction steps in the cases where the exponent e is greater than 1 are based on the fact that, for any integers
    x, y, and m, we can find the remainder of x times y modulo m by computing separately the remainders of x modulo m
    and y modulo m, multiplying these, and then taking the remainder of the result modulo m. For instance, in the case
    where e is even, we compute the remainder of b^e/2 modulo m, square this, and take the remainder modulo m. This
    technique is useful because it means we can perform our computation without ever having to deal with numbers much
    larger than m.
    """
    if eq(exp, 0):
        return 1
    if is_even(exp):
        return mod(
            square(expmod(base, truediv(exp, 2), m)),
            m
        )
    return mod(
        mul(
            base,
            expmod(base, sub(exp, 1), m)
        ),
        m
    )


def fermat_test(n):
    """Probabilistic methods:

    The Fermat test differs in character from most familiar algorithms, in which one computes an answer that is
    guaranteed to be correct. Here, the answer obtained is only probably correct. More precisely, if n ever fails the
    Fermat test, we can be certain that n is not prime. But the fact that n passes the test, while an extremely strong
    indication, is still not a guarantee that n is prime. What we would like to say is that for any number n, if we
    perform the test enough times and find that n always passes the test, then the probability of error in our primality
    test can be made as small as we like.
    Unfortunately, this assertion is not quite correct. There do exist numbers that fool the Fermat test: numbers n that
    are not prime and yet have the property that an is congruent to a modulo n for all integers a < n. Such numbers are
    extremely rare, so the Fermat test is quite reliable in practice.47 There are variations of the Fermat test that
    cannot be fooled. In these tests, as with the Fermat method, one tests the primality of an integer n by choosing a
    random integer a<n and checking some condition that depends upon n and a. (See exercise 1.28 for an example of such
    a test.) On the other hand, in contrast to the Fermat test, one can prove that, for any n, the condition does not
    hold for most of the integers a<n unless n is prime. Thus, if n passes the test for some random choice of a, the
    chances are better than even that n is prime. If n passes the test for two random choices of a, the chances are
    better than 3 out of 4 that n is prime. By running the test with more and more randomly chosen values of a we can
    make the probability of error as small as we like.
    The existence of tests for which one can prove that the chance of error becomes arbitrarily small has sparked
    interest in algorithms of this type, which have come to be known as probabilistic algorithms. There is a great deal
    of research activity in this area, and probabilistic algorithms have been fruitfully applied to many fields.

    Note 48:
    One of the most striking applications of probabilistic prime testing has been to the field of cryptography. Although
    it is now computationally infeasible to factor an arbitrary 200-digit number, the primality of such a number can be
    checked in a few seconds with the Fermat test. This fact forms the basis of a technique for constructing
    ``unbreakable codes'' suggested by Rivest, Shamir, and Adleman (1977). The resulting RSA algorithm has become a
    widely used technique for enhancing the security of electronic communications. Because of this and related
    developments, the study of prime numbers, once considered the epitome of a topic in ``pure'' mathematics to be
    studied only for its own sake, now turns out to have important practical applications to cryptography, electronic
    funds transfer, and information retrieval."""
    def try_it(a):
        return eq(
            expmod(a, n, n),
            a
        )
    return try_it(
        random.randint(1, sub(n, 1))
    )


def is_prime_fast(n, times):
    # print('%(times)s times left' % locals())
    if eq(times, 0):
        return True
    if fermat_test(n):
        return is_prime_fast(
            n,
            sub(times, 1)
        )
    return False


def run_the_magic():
    n, times = 139, 10
    print(
        '(fast-prime? %(n)s %(times)s)' % locals(),
        is_prime_fast(n, times),
        sep='\n',
    )


if __name__ == '__main__':
    run_the_magic()
