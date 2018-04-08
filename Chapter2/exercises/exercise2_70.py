# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.70
"""
from Chapter2.exercises.exercise2_68 import encode
from Chapter2.exercises.exercise2_69 import generate_huffman_tree
from Chapter2.themes.lisp_list_structured_data import (
    lisp_list,
    print_lisp_list, length,
)
from Chapter2.themes.symbolic_data import quote
from utils import let


def _1950s_rock_songs_lyrics_alphabet():
    return lisp_list(
                lisp_list(quote('A'), 2),
                lisp_list(quote('NA'), 16),
                lisp_list(quote('BOOM'), 1),
                lisp_list(quote('SHA'), 3),
                lisp_list(quote('GET'), 2),
                lisp_list(quote('YIP'), 9),
                lisp_list(quote('JOB'), 2),
                lisp_list(quote('WAH'), 1),)


def sample_song():
    return quote(lisp_list(
        'GET', 'A', 'JOB', 'SHA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA',
        'NA', 'GET', 'A', 'JOB', 'SHA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA',
        'NA', 'NA', 'WAH', 'YIP', 'YIP', 'YIP', 'YIP', 'YIP', 'YIP', 'YIP',
        'YIP', 'YIP', 'SHA', 'BOOM'))


def run_the_magic():
    with let(
        encode(
            sample_song(),
            generate_huffman_tree(
                _1950s_rock_songs_lyrics_alphabet()))) as (encoded_song,):
        print_lisp_list(encoded_song)
        print('Number of bits required for encoding with Huff tree: {}'.format(
            length(encoded_song)))
        print('Smallest number of bits with fixed-length code: {}'.format(
            length(sample_song()) * 3))


if __name__ == "__main__":
    run_the_magic()

