import math


def half_divide_method(a: float, b: float, e: float, f: ()):
    delta = (e / 2) * 0.9
    i = 0
    while abs(b-a) > e:
        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta
        if f(x1) > f(x2):
            a = x1
        else:
            b = x2
        i += 1
    return a, b, i, (a+b)/2


