# -*- coding: utf-8 -*-
"""
Most Lisp implementations include a primitive called runtime that returns an integer that specifies the amount of time
the system has been running (measured, for example, in microseconds). The following timed-prime-test procedure, when
called with an integer n, prints n and checks to see if n is prime. If n is prime, the procedure prints three asterisks
followed by the amount of time used in performing the test.

(define (timed-prime-test n)
  (newline)
  (display n)
  (start-prime-test n (runtime)))
(define (start-prime-test n start-time)
  (if (prime? n)
      (report-prime (- (runtime) start-time))))
(define (report-prime elapsed-time)
  (display " *** ")
  (display elapsed-time))

Using this procedure, write a procedure search-for-primes that checks the primality of consecutive odd integers in a
specified range. Use your procedure to find the three smallest primes larger than 1000; larger than 10,000; larger than
100,000; larger than 1,000,000. Note the time needed to test each prime. Since the testing algorithm has order of growth
of theta(sqrt(n)), you should expect that testing for primes around 10,000 should take about sart(10) times as long as
testing for primes around 1000. Do your timing data bear this out? How well do the data for 100,000 and 1,000,000
support the sqrt(n) prediction? Is your result compatible with the notion that programs on your machine run in time
proportional to the number of steps required for the computation?


Found Primes:
    - larger than 1000 : 1009, 1013, 1019
    - larger than 10000: 10007, 10009, 10037
    - larger than 100000: 100003, 100019, 100043
    - larger than 1000000: Recursion Error
"""
from operator import add, gt, sub, le

from Chapter1.exponentiation import is_even
from Chapter1.tfp_searching_for_divisors import is_prime


counter = 0


def runtime():
    import time
    return time.time()


def timed_prime_test(n):
    print()
    print(n)
    start_prime_test(n, runtime())


def start_prime_test(n, start_time):
    if is_prime(n):
        global counter
        counter += 1
        report_prime(
            sub(runtime(), start_time)
        )


def report_prime(elapsed_time):
    print(" *** ")
    print(elapsed_time)


def search_for_primes(a, b):
    def process(k):
        global counter
        if counter == 3:
            counter = 0
            return
        if le(k, b):
            timed_prime_test(k)
            return process(add(k, 2))

    process(
        add(a, 1) if is_even(a)
        else
        a
    )


if __name__ == '__main__':
    b = 100000000000000000
    for a in (1000, 10000, 100000, 1000000):
        try:
            search_for_primes(a, b)
        except RecursionError:
            continue
