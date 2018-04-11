# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.76
"""


def run_the_magic():
    print("""
        In case we add new types to a system with generic operations:
            1. in explicit design style, we would need to create a new predicate
            for each type, a new constructor and modify the generic operators
            2. in data-directed design style, we would need to modify an install
            procedure
            3. in message-passing design style, we would need to modify the
            dispatch procedure internal to the data constructor
            
        In case we add new operators:
            1. in explicit: modify almost everything
            2. in data-directed: modify the install package
            3. in message-passing: a new constructor with a dispatch function
            
        Data-directed is better when we must often add types.
        Message-passing is better when we must often add operations.
    """)


if __name__ == "__main__":
    run_the_magic()

