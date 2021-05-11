import math


def half_divide_method(a: float, b: float, e: float, f: ()):
    delta = (e / 2) * 0.9
    iter_count = 0
    func_count = 0
    length_values = [b - a]
    while abs(b - a) > e:
        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta
        if f(x1) > f(x2):
            a = x1
        else:
            b = x2
        iter_count += 1
        func_count += 2
        length_values.append(b - a)
    return (a+b)/2, f((a+b)/2), iter_count, func_count + 1, length_values


