# -*- coding: utf-8 -*-
"""
One variant of the Fermat test that cannot be fooled is called the Miller-Rabin test (Miller 1976; Rabin 1980). This
starts from an alternate form of Fermat's Little Theorem, which states that if n is a prime number and a is any positive
integer less than n, then a raised to the (n - 1)st power is congruent to 1 modulo n. To test the primality of a number
n by the Miller-Rabin test, we pick a random number a<n and raise a to the (n - 1)st power modulo n using the expmod
procedure. However, whenever we perform the squaring step in expmod, we check to see if we have discovered a
``nontrivial square root of 1 modulo n,'' that is, a number not equal to 1 or n - 1 whose square is equal to 1 modulo n.
It is possible to prove that if such a nontrivial square root of 1 exists, then n is not prime. It is also possible to
prove that if n is an odd number that is not prime, then, for at least half the numbers a<n, computing a^(n-1) in this
way will reveal a nontrivial square root of 1 modulo n. (This is why the Miller-Rabin test cannot be fooled.) Modify the
expmod procedure to signal if it discovers a nontrivial square root of 1, and use this to implement the Miller-Rabin
test with a procedure analogous to fermat-test. Check your procedure by testing various known primes and non-primes.
Hint: One convenient way to make expmod signal is to have it return 0.
"""
import random
from operator import eq, mod, mul, sub, truediv

from Chapter1.compound_procedures import square
from Chapter1.exponentiation import is_even


def expmod(base, exp, m):
    if eq(exp, 0):
        return 1
    if is_even(exp):
        trivial = expmod(base, truediv(exp, 2), m)
        sqr = square(trivial)
        if not eq(trivial, 1) and not eq(trivial, sub(m, 1)) and eq(mod(sqr, m), 1):
            return 0
        return mod(
            sqr,
            m
        )
    return mod(
        mul(
            base,
            expmod(base, sub(exp, 1), m)
        ),
        m
    )


def miller_rabin_test(n):
    def try_it(a):
        return eq(
            expmod(a, sub(n, 1), n),
            1
        )

    return try_it(
        random.randint(1, sub(n, 1))
    )


def run_the_magic():
    carmichael_numbers = [
        561,
        1105,
        1729,
        2465,
        2821,
        6601,
    ]

    for n in carmichael_numbers:
        print(miller_rabin_test(n))

    for a in (1009, 1013, 1019, 10007, 10009, 10037, 100003, 100019, 100043, 1000003, 1000033, 1000037):
        print(miller_rabin_test(a))

    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 37):
        print(miller_rabin_test(a))


if __name__ == '__main__':
    run_the_magic()