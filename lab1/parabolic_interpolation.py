import math as m


def parabolic_interpolation(x1: float, x3: float, e: float, function: ()):
    iter_count = 0
    length_values = []
    x2 = (x1 + x3) / 2
    f1 = function(x1)
    f2 = function(x2)
    f3 = function(x3)
    func_count = 3
    while True:
        iter_count += 1
        length_values.append(x3 - x1)
        u = x2 - 0.5 * ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f2 - f1)) / \
            ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))
        fu = function(u)
        func_count += 1
        if abs(fu - f2) < e and abs(u - x2) < e:
            return (u, fu, iter_count, func_count, length_values) if fu > f2 \
                else (x2, f2, iter_count, func_count, length_values)

        if fu < f2:
            if u >= x2:
                x1 = x2
                f1 = f2
                x2 = u
                f2 = fu
            else:
                x3 = x2
                f3 = f2
                x2 = u
                f2 = fu
        elif fu > f2:
            if u >= x2:
                x3 = u
                f3 = fu
            else:
                x1 = u
                f1 = fu
        else:
            x1, f1 = u, fu
            x2 = (x1 + x3) / 2
            f2 = function(x2)
            func_count += 1
