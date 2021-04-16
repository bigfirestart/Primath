from math import sqrt


def golden_ratio(l: float, r: float, eps: float, f: ()):
    phi = (1 + sqrt(5)) / 2
    resphi = 2 - phi
    x1 = l + resphi * (r - l)
    x2 = r - resphi * (r - l)
    f1 = f(x1)
    f2 = f(x2)
    while True:
        if f1 < f2:
            r = x2
            x2 = x1
            f2 = f1
            x1 = l + resphi * (r - l)
            f1 = f(x1)
        else:
            l = x1
            x1 = x2
            f1 = f2
            x2 = r - resphi * (r - l)
            f2 = f(x2)
        if abs(r - l) > eps:
            break
    return (x1 + x2) / 2