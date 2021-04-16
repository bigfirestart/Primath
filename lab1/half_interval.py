import math


def half_divide_method(a: float, b: float, e: float, f: ()):
    c = (a+b)/2
    while abs(b-a) > e:
        c = (a + b) / 2
        if f(a)-f(c) < 0:
            b = c
        else:
            a = c
    return c


