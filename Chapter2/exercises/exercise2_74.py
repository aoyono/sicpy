# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.74
"""
from Chapter2.themes.lisp_list_structured_data import car, nil, cdr
from Chapter2.themes.symbolic_data import quote
from utils import get, error, let


def get_record(name, division_file):
    return get(
        quote('get-record'),
        division_from_file(division_file)
    )(name)


def division_from_file(division_file):
    pass


def get_salary(record):
    return get(
        quote('get-salary'),
        division_from_record(record)
    )()


def division_from_record(record):
    pass


def find_employee_record(name, divisions_files):
    def iterate(rest, record):
        if record is nil:
            if rest is nil:
                error('employee record not found: {}'.format(name))
            else:
                with let(car(rest)) as (division_file,):
                    return iterate(cdr(rest), get_record(name, division_file))
        return record
    return iterate(divisions_files, nil)


def run_the_magic():
    pass


if __name__ == "__main__":
    run_the_magic()

