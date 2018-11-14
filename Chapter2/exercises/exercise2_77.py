# -*- coding: utf-8 -*-
"""
https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_thm_2.77
"""
from Chapter2.exercises.exercise2_78 import contents
from Chapter2.themes.data_directed_programming_and_additivity import (
    angle, attach_tag, imag_part, install_rectangular_package, magnitude,
    real_part, install_polar_package,
)
from Chapter2.themes.generic_arithmetic_operations import (
    make_complex_from_real_imag
)
from Chapter2.themes.lisp_list_structured_data import lisp_list
from Chapter2.themes.symbolic_data import quote
from utils import get, let, put


def install_complex_package():
    # Imported procedures from rectangular and polar packages
    def make_from_real_imag(x, y):
        return get(
            quote('make-from-real-imag'),
            quote('rectangular'))(x, y)

    def make_from_mag_ang(r, a):
        return get(quote('make-from-mag-ang'), quote('polar'))(r, a)

    # Internal procedures
    def add_complex(z1, z2):
        return make_from_real_imag(
            real_part(z1) + real_part(z2),
            imag_part(z1) + imag_part(z2))

    def sub_complex(z1, z2):
        return make_from_real_imag(
            real_part(z1) - real_part(z2),
            imag_part(z1) - imag_part(z2))

    def mul_complex(z1, z2):
        return make_from_mag_ang(
            magnitude(z1) * magnitude(z2),
            angle(z1) + angle(z2))

    def div_complex(z1, z2):
        return make_from_mag_ang(
            magnitude(z1) / magnitude(z2),
            angle(z1) - angle(z2))

    # From exercise 2.79
    def equals(z1, z2):
        return (real_part(z1) == real_part(z2)
                and imag_part(z1) == imag_part(z2))

    # Interface to the rest of the system
    def tag(z):
        return attach_tag(quote('complex'), z)

    put(quote('add'),
        quote(lisp_list('complex', 'complex')),
        lambda z1, z2: tag(add_complex(z1, z2)))
    put(quote('sub'),
        quote(lisp_list('complex', 'complex')),
        lambda z1, z2: tag(sub_complex(z1, z2)))
    put(quote('mul'),
        quote(lisp_list('complex', 'complex')),
        lambda z1, z2: tag(mul_complex(z1, z2)))
    put(quote('div'),
        quote(lisp_list('complex', 'complex')),
        lambda z1, z2: tag(div_complex(z1, z2)))

    put(quote('make-from-real-imag'),
        quote('complex'),
        lambda x, y: tag(make_from_real_imag(x, y)))
    put(quote('make-from-mag-ang'),
        quote('complex'),
        lambda r, a: tag(make_from_mag_ang(r, a)))

    # install polar and rectangular representations
    # this is necessary as we retrieve some methods for these representations
    # in the internal methods defined here
    install_polar_package()
    install_rectangular_package()

    put(quote('real-part'),
        quote(lisp_list('complex')),
        real_part)
    put(quote('imag-part'),
        quote(lisp_list('complex')),
        imag_part)
    put(quote('magnitude'),
        quote(lisp_list('complex')),
        magnitude)
    put(quote('angle'),
        quote(lisp_list('complex')),
        angle)

    # From exercise 2.79
    put(quote('equals'),
        quote(lisp_list('complex', 'complex')),
        equals)
    return quote('done')


def run_the_magic():
    print("""
        Procedure calls chain when calling (magnitude z):
        (magnitude z) => (apply-generic 'magnitude z)
        (apply-generic 'magnitude z) => (apply magnitude '((contents z)))
        (apply magnitude '((contents z))) => (magnitude (contents z))
        (magnitude (contents z)) => (apply-generic 'magnitude (contents z))
        (apply-generic 'magnitude (contents z)) => (apply magnitude '((
        contents (contents z))))
        (apply magnitude '((contents (contents z)))) => (magnitude (contents
        (contents z))
        The last magnitude procedure is the one defined in the installation
        procedure of rectangular package
    """)
    install_rectangular_package()
    install_complex_package()
    with let(make_complex_from_real_imag(3, 4)) as (z,):
        print(
            '(install-rectangular-package)\n(install-complex-package)\n(let ((z'
            ' (make-complex-from-real-imag 3 4)))\n\t(magnitude z))',
            magnitude(z),
            sep='\n')


if __name__ == "__main__":
    run_the_magic()
