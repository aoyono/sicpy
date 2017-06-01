# coding: utf-8


class LispSyntaxError(Exception):
    pass


def lisp_if(predicate, consequent, alternative):
    return predicate and consequent or alternative


def lisp_cond(*pred_cons_pairs, _else=None):
    def test(arguments):
        if not arguments:
            return False
        predicate, consequent = arguments[0]
        return predicate and consequent or test(arguments[1:])

    try:
        res = test(pred_cons_pairs)
        if res:
            return res
        if _else is not None:
            return _else
        raise LispSyntaxError('Undefined behavior for cond')
    except (ValueError, TypeError):
        raise LispSyntaxError('Bad arguments for Lisp cond')


if __name__ == '__main__':
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
