# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.71
"""


def run_the_magic():
    print("""
        For a Huffman tree for an alphabet of n symbols with the relative
        frequencies growing from 1 to 2^(n-1), we need 1 bit to encode the most
        frequent symbol and n-1 bits to encode the least frequent
    """)


if __name__ == "__main__":
    run_the_magic()

