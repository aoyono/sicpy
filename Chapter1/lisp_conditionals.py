# -*- coding: utf-8 -*-
from operator import lt


class LispSyntaxError(Exception):
    pass


def lisp_if(predicate, consequent, alternative):
    return predicate and consequent or alternative


def lisp_cond(*pred_cons_pairs, _else=None):
    if not pred_cons_pairs[0]:
        if _else is not None:
            return _else
        raise LispSyntaxError('Undefined behavior for cond')
    try:
        predicate, consequent = pred_cons_pairs[0]
    except (ValueError, TypeError):
        raise LispSyntaxError('Bad arguments for Lisp cond')
    if predicate:
        return consequent
    return lisp_cond(pred_cons_pairs[1:], _else=_else)


def lisp_abs(x):
    return lisp_cond((lt(x, 0), -x), _else=x)


def run_the_magic():
    print(
        lisp_if(
            1 > 2,
            '1 is greater than 2',
            '1 is lesser than 2'
        )
    )

    print(
        lisp_cond(
            (1 > 2, '1 is greater than 2'),
            _else='1 is lesser than 2'
        )
    )

    print(
        lisp_abs(-5)
    )


if __name__ == '__main__':
    run_the_magic()
