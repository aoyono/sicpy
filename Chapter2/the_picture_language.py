# -*- coding: utf-8 -*-
"""
"""
import turtle

from Chapter2.exercise2_18 import reverse
from Chapter2.exercise2_23 import for_each
from Chapter2.lisp_list_structured_data import append, cadr, car, cddr, cdr, cons, lisp_list, list_ref, nil
from utils import let

board = turtle.Screen()
board.setup(width=500, height=500, startx=0, starty=0)
board.title('The picture language - SICP')
board.setworldcoordinates(0.0, 0.0, 25, 25)


# Taken from http://wiki.drewhess.com/wiki/SICP_exercise_2.49 to be able to draw wave
def connect(vect_list):
    def iter(segment_list, remaining):
        if cdr(remaining) is nil():
            return reverse(segment_list)
        return iter(cons(make_segment(car(remaining), cadr(remaining)), segment_list), cdr(remaining))

    return iter(nil(), vect_list)


def wave(frame):
    """The primitive painter (implementation as part of exercice 2.49)"""
    return segments__painter(append(
        connect(
            lisp_list(
                make_vect(0.4, 0.0),
                make_vect(0.5, 0.33),
                make_vect(0.6, 0.0)
            )
        ), append(
            connect(
                lisp_list(
                    make_vect(0.25, 0.0),
                    make_vect(0.33, 0.5),
                    make_vect(0.3, 0.6),
                    make_vect(0.1, 0.4),
                    make_vect(0.0, 0.6),
                )
            ), append(
                connect(
                    lisp_list(
                        make_vect(0.0, 0.8),
                        make_vect(0.1, 0.6),
                        make_vect(0.33, 0.65),
                        make_vect(0.4, 0.65),
                        make_vect(0.35, 0.8),
                        make_vect(0.4, 1.0),
                    )
                ), append(
                    connect(
                        lisp_list(
                            make_vect(0.75, 0.0),
                            make_vect(0.6, 0.45),
                            make_vect(1.0, 0.15),
                        )
                    ),
                    connect(
                        lisp_list(
                            make_vect(1.0, 0.35),
                            make_vect(0.8, 0.65),
                            make_vect(0.6, 0.65),
                            make_vect(0.65, 0.8),
                            make_vect(0.6, 1.0),
                        )
                    ),
                )))))(frame)


def identity():
    """The identity painter"""


def beside(painter1, painter2):
    with let(make_vect(0.5, 0.0)) as (split_point,):
        with let(
                transform_painter(painter1, make_vect(0.0, 0.0), split_point, make_vect(0.0, 1.0)),
                transform_painter(painter2, split_point, make_vect(1.0, 0.0), make_vect(0.5, 1.0)),
        ) as (paint_left, paint_right):
            return lambda frame: (paint_left(frame), paint_right(frame))


def flip_vert(painter):
    return transform_painter(
        painter,
        make_vect(0.0, 1.0),
        make_vect(1.0, 1.0),
        make_vect(0.0, 0.0),
    )


def below2(painter1, painter2):
    with let(make_vect(0.0, 0.5)) as (split_point,):
        with let(
                transform_painter(painter2, make_vect(0.0, 0.0), make_vect(1.0, 0.0), split_point),
                transform_painter(painter1, split_point, make_vect(1.0, 0.5), make_vect(0.0, 1.0)),
        ) as (paint_bottom, paint_top):
            return lambda frame: (paint_top(frame), paint_bottom(frame))


def below(painter1, painter2):
    return rotate270(
            beside(rotate90(painter1), rotate90(painter2))
    )


def flipped_pairs(painter):
    with let(beside(painter, flip_vert(painter))) as (painter2,):
        return below(painter2, painter2)


def wave4():
    return flipped_pairs(wave)


def right_split(painter, n):
    if n == 0:
        return painter
    with let(right_split(painter, n - 1)) as (smaller,):
        return beside(painter, below(smaller, smaller))


def corner_split(painter, n):
    if n == 0:
        return painter
    with let(up_split(painter, n - 1), right_split(painter, n - 1)) as (up, right):
        with let(beside(up, up), below(right, right), corner_split(painter, n - 1)) as (top_left, bottom_right, corner):
            return beside(
                below(painter, top_left),
                below(bottom_right, corner)
            )


def square_limit(painter, n):
    with let(corner_split(painter, n)) as (quarter,):
        with let(beside(flip_horiz(quarter), quarter)) as (half,):
            return below(flip_vert(half), half)


def flip_horiz(painter):
    return transform_painter(
        painter,
        make_vect(1.0, 0.0),
        make_vect(0.0, 0.0),
        make_vect(1.0, 1.0),
    )


def rotate180(painter):
    return flip_horiz(
        flip_vert(painter)
    )


def rotate270(painter):
    return transform_painter(
        painter,
        make_vect(0.0, 1.0),
        make_vect(0.0, 0.0),
        make_vect(1.0, 1.0),
    )


def up_split(painter, n):
    if n == 0:
        return painter
    with let(up_split(painter, n - 1)) as (smaller,):
        return below(painter, beside(smaller, smaller))


def square_of_four(tl, tr, bl, br):
    def anon(painter):
        with let(beside(tl(painter), tr(painter)), beside(bl(painter), br(painter))) as (top, bottom):
            return below(bottom, top)

    return anon


def flipped_pairs_sqof(painter):
    with let(square_of_four(identity, flip_vert, identity, flip_vert)) as (combine4,):
        return combine4(painter)


def square_limit_sqof(painter, n):
    with let(square_of_four(flip_horiz, identity, rotate180, flip_vert)) as (combine4,):
        return combine4(corner_split(painter, n))


def frame_coord_map(frame):
    def anon(v):
        return add_vect(
            origin_frame(frame),
            add_vect(
                scale_vect(
                    xcor_vect(v),
                    edge1_frame(frame)
                ),
                scale_vect(
                    ycor_vect(v),
                    edge2_frame(frame)
                )
            )
        )

    return anon


# Exercise 2.46

def make_vect(x, y):
    return cons(x, y)


def xcor_vect(v):
    return car(v)


def ycor_vect(v):
    return cdr(v)


def add_vect(v1, v2):
    return make_vect(
        xcor_vect(v1) + xcor_vect(v2),
        ycor_vect(v1) + ycor_vect(v2)
    )


def sub_vect(v1, v2):
    return make_vect(
        xcor_vect(v1) - xcor_vect(v2),
        ycor_vect(v1) - ycor_vect(v2)
    )


def scale_vect(factor, v):
    return make_vect(
        factor * xcor_vect(v),
        factor * ycor_vect(v)
    )


# Exercise 2.47

def make_frame1(origin, edge1, edge2):
    return lisp_list(origin, edge1, edge2)


def origin1(frame):
    return list_ref(frame, 0)


def edge11(frame):
    return list_ref(frame, 1)


def edge21(frame):
    return list_ref(frame, 2)


def make_frame2(origin, edge1, edge2):
    return cons(origin, cons(edge1, edge2))


def origin2(frame):
    return car(frame)


def edge12(frame):
    return cadr(frame)


def edge22(frame):
    return cddr(frame)


# Choosing the reference implementation
make_frame, origin_frame, edge1_frame, edge2_frame = make_frame1, origin1, edge11, edge21


def segments__painter(segment_list):
    def anon(frame):
        for_each(
            lambda segment: draw_line(
                frame_coord_map(frame)(
                    start_segment(segment)
                ),
                frame_coord_map(frame)(
                    end_segment(segment)
                )
            ),
            segment_list
        )

    return anon


def draw_line(point1, point2):
    """Draws a line on the screen between two specified points"""
    point1 = (board.xscale * point1[0], board.yscale * point1[1])
    point2 = (board.xscale * point2[0], board.yscale * point2[1])
    try:
        drawer = board.turtles()[-1]
    except IndexError:
        drawer = turtle.RawTurtle(board)
        drawer.setposition((0, 0))
        drawer.shape('circle')
    drawer.penup()
    drawer.goto(point1)
    drawer.pendown()
    drawer.goto(point2)


# Exercise 2.48

def make_segment(v1, v2):
    return cons(v1, v2)


def start_segment(segment):
    return car(segment)


def end_segment(segment):
    return cdr(segment)


# Exercise 2.49

def outline(frame):
    """
    with let(origin_frame(frame), edge1_frame(frame), edge2_frame(frame)) as (origin, edge1, edge2):
        with let(add_vect(edge1, edge2)) as (up_corner,):
            return segments__painter(
                lisp_list(
                    make_segment(origin, edge2),
                    make_segment(edge2, up_corner),
                    make_segment(up_corner, edge1),
                    make_segment(edge1, origin),
                )
            )(frame)
    """
    with let(
            make_vect(0.0, 0.0),
            make_vect(1.0, 0.0),
            make_vect(0.0, 1.0),
            make_vect(1.0, 1.0)
    ) as (origin, edge1, edge2, up_corner):
        return segments__painter(
            lisp_list(
                make_segment(origin, edge2),
                make_segment(edge2, up_corner),
                make_segment(up_corner, edge1),
                make_segment(edge1, origin),
            )
        )(frame)


def X(frame):
    """
    with let(origin_frame(frame), edge1_frame(frame), edge2_frame(frame)) as (origin, edge1, edge2):
        with let(add_vect(edge1, edge2)) as (up_corner,):
            return segments__painter(
                lisp_list(
                    make_segment(edge1, edge2),
                    make_segment(origin, up_corner)
                )
            )(frame)
    """
    with let(
            make_vect(0.0, 0.0),
            make_vect(1.0, 0.0),
            make_vect(0.0, 1.0),
            make_vect(1.0, 1.0)
    ) as (origin, edge1, edge2, up_corner):
        return segments__painter(
            lisp_list(
                make_segment(edge1, edge2),
                make_segment(origin, up_corner)
            )
        )(frame)


def diamond(frame):
    """
    with let(origin_frame(frame), edge1_frame(frame), edge2_frame(frame)) as (origin, edge1, edge2):
        return segments__painter(
            lisp_list(
                make_segment(scale_vect(0.5, edge2), add_vect(edge2, scale_vect(0.5, edge1))),
                make_segment(add_vect(edge2, scale_vect(0.5, edge1)), add_vect(edge1, scale_vect(0.5, edge2))),
                make_segment(add_vect(edge1, scale_vect(0.5, edge2)), scale_vect(0.5, edge1)),
                make_segment(scale_vect(0.5, edge1), scale_vect(0.5, edge2))
            )
        )(frame)
    """
    with let(
            make_vect(0.0, 0.0),
            make_vect(1.0, 0.0),
            make_vect(0.0, 1.0),
    ) as (origin, edge1, edge2):
        return segments__painter(
            lisp_list(
                make_segment(scale_vect(0.5, edge2), add_vect(edge2, scale_vect(0.5, edge1))),
                make_segment(add_vect(edge2, scale_vect(0.5, edge1)), add_vect(edge1, scale_vect(0.5, edge2))),
                make_segment(add_vect(edge1, scale_vect(0.5, edge2)), scale_vect(0.5, edge1)),
                make_segment(scale_vect(0.5, edge1), scale_vect(0.5, edge2))
            )
        )(frame)


# EOE

def edges(frame):
    with let(make_vect(0.0, 0.0), make_vect(1.0, 0.0), make_vect(0.0, 1.0)) as (origin, edge1, edge2):
        return segments__painter(lisp_list(
            make_segment(origin, edge1),
            make_segment(origin, edge2)
        ))(frame)


def transform_painter(painter, origin, corner1, corner2):
    def anonfunc(frame):
        with let(frame_coord_map(frame)) as (m,):
            with let(m(origin)) as (new_origin,):
                return painter(
                    make_frame(
                        new_origin,
                        sub_vect(m(corner1), new_origin),
                        sub_vect(m(corner2), new_origin)
                    )
                )

    return anonfunc


def shrink_to_upper_right(painter):
    return transform_painter(
        painter,
        make_vect(0.5, 0.5),
        make_vect(1.0, 0.4),
        make_vect(0.5, 1.0),
    )


def rotate90(painter):
    return transform_painter(
        painter,
        make_vect(1.0, 0.0),
        make_vect(1.0, 1.0),
        make_vect(0.0, 0.0),
    )


def squash_inwards(painter):
    return transform_painter(
        painter,
        make_vect(0.0, 0.0),
        make_vect(0.65, 0.35),
        make_vect(0.35, 0.65),
    )


def run_the_magic():
    with let(make_frame(make_vect(0, 0), make_vect(0, 1), make_vect(1, 0))) as (a_frame,):
        assert frame_coord_map(a_frame)(make_vect(0, 0)) == origin_frame(a_frame)
    f = make_frame(
        cons(0.0, 0.0),
        make_vect(1.0, 0.0),
        make_vect(0.0, 1.0)
    )
    edges(f)
    below(diamond, wave)(f)
    below2(diamond, wave)(f)
    # beside(diamond, wave)(f)
    # below(wave, flip_vert(wave))(f)
    # wave(f)
    # below2(wave, flip_vert(wave))(f)
    board.mainloop()


if __name__ == '__main__':
    run_the_magic()
