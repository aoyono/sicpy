# -*- coding: utf-8 -*-
"""
Each of the following two procedures defines a method for adding two positive integers in terms of the procedures inc,
which increments its argument by 1, and dec, which decrements its argument by 1.

(define (+ a b)
  (if (= a 0)
      b
      (inc (+ (dec a) b))))

(define (+ a b)
  (if (= a 0)
      b
      (+ (dec a) (inc b))))

Using the substitution model, illustrate the process generated by each procedure in evaluating (+ 4 5). Are these
processes iterative or recursive?

Conclusion: It seem's to me that we can generalize like this: In a recursive procedure, if the recursivity occurs as an
intermediate step within the procedure (this is, the result of the recursive call is used to compute the final result),
then the generated process is recursive. If in the other hand the recursive call shall give the final result directly,
then we are facing a procedure generating an iterative process.
"""
from operator import add, eq, sub


def inc(a):
    return add(a, 1)


def dec(a):
    return sub(a, 1)


def add_inc_dec1(a, b, s=[]):
    """Generated process will be recursive"""
    def print_shape(a_minus_one_plus_b):
        """Print the shape of the linear recursive process of computing +"""
        import re
        nonlocal a, b

        def print_after():
            m = re.search(r'\(\+ \(dec 1\) ([0-9]+)\)', s[0])
            if m is None:
                m = re.search(r'\(inc ([0-9]+)\)', s[0])
            str2print = (
                s[0][0:m.start()]
                + str(a_minus_one_plus_b)
                + s[0][m.end():]
            )
            s[0] = str2print
            print(s[0])

        def print_before():
            base = '(inc {})'
            if not s:
                s.append(base.format('(+ (dec %s) %s)' % (a, b)))
            else:
                m = re.search(r'\(\+ \(dec ([0-9]+)\) ([0-9]+)\)', s[0])
                str2print = (
                    s[0][0:m.start()]
                    + base.format('(+ (dec %(a)s) %(b)s)' % locals())
                    + s[0][m.end():]
                )
                s[0] = str2print
            print(s[0])

        if a_minus_one_plus_b is not None:
            print_after()
        else:
            print_before()

    if eq(a, 0):
        return b
    print_shape(None)
    a_minus_one_plus_b = add_inc_dec1(dec(a), b)
    print_shape(a_minus_one_plus_b)
    return inc(a_minus_one_plus_b)


def add_inc_dec2(a, b):
    """Generated process will be iterative"""
    if eq(a, 0):
        return b
    print('(+ %s %s)' % (dec(a), inc(b)))
    return add_inc_dec2(
        dec(a),
        inc(b)
    )


def run_the_magic():
    a, b = 4, 5
    print("Illustrating the process generated by the first implementation of procedure '+' (add_inc_dec1) "
          "for evaluating (+ 4 5):", "(+ %(a)s %(b)s)" % locals(), sep='\n')
    val = add_inc_dec1(a, b)
    print(val)
    print("Illustrating the process generated by the first implementation of procedure '+' (add_inc_dec1) "
          "for evaluating (+ 4 5):", "(+ %(a)s %(b)s)" % locals(), sep='\n')
    val = add_inc_dec2(a, b)
    print(val)


if __name__ == '__main__':
    run_the_magic()
