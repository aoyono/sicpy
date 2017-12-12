# -*- coding: utf-8 -*-
"""
The smallest-divisor procedure shown at the start of this section does lots of needless testing: After it checks to see
if the number is divisible by 2 there is no point in checking to see if it is divisible by any larger even numbers. This
suggests that the values used for test-divisor should not be 2, 3, 4, 5, 6, ..., but rather 2, 3, 5, 7, 9, .... To
implement this change, define a procedure next that returns 3 if its input is equal to 2 and otherwise returns its input
plus 2. Modify the smallest-divisor procedure to use (next test-divisor) instead of (+ test-divisor 1). With
timed-prime-test incorporating this modified version of smallest-divisor, run the test for each of the 12 primes found
in exercise 1.22. Since this modification halves the number of test steps, you should expect it to run about twice as
fast. Is this expectation confirmed? If not, what is the observed ratio of the speeds of the two algorithms, and how do
you explain the fact that it is different from 2?

Here we succeed in finding the three first prime greater than 1000000: 1000003, 1000033, 1000037
"""
from operator import add, eq, gt, le, sub

from Chapter1.compound_procedures import square
from Chapter1.exercise1_22 import report_prime, runtime
from Chapter1.exponentiation import is_even
from Chapter1.tfp_searching_for_divisors import divides

counter = 0


def modified_smallest_divisor(n):
    def next(n):
        if eq(n, 2):
            return 3
        return add(n, 2)

    def find_divisor(n, test_divisor):
        if gt(square(test_divisor), n):
            return n
        if divides(test_divisor, n):
            return test_divisor
        return find_divisor(
            n,
            next(test_divisor)
        )

    return find_divisor(n, 2)


def modified_is_prime(n):
    return eq(n, modified_smallest_divisor(n))


def modified_timed_prime_test(n):
    print()
    print(n)
    modified_start_prime_test(n, runtime())


def modified_start_prime_test(n, start_time):
    if modified_is_prime(n):
        global counter
        counter += 1
        report_prime(
            sub(runtime(), start_time)
        )


def modified_search_for_primes(a, b):
    def process(k):
        global counter
        if counter == 3:
            counter = 0
            return
        if le(k, b):
            modified_timed_prime_test(k)
            return process(add(k, 2))

    process(
        add(a, 1) if is_even(a)
        else
        a
    )


def run_the_magic():
    for a in (1009, 1013, 1019, 10007, 10009, 10037, 100003, 100019, 100043, 1000003, 1000033, 1000037):
        modified_search_for_primes(a, a + 1)


if __name__ == '__main__':
    run_the_magic()
