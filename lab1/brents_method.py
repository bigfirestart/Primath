import math as m


def brents_method(a: float, c: float, e: float, function: ()):
    u = 0
    iter_count = 0
    length_values = []
    K = (3 - m.sqrt(5)) / 2
    x = w = v = (a + c) / 2
    fx = fw = fv = function(x)
    func_count = 1
    d = t = c - a
    while True:
        iter_count += 1
        length_values.append(c - a)
        g = t
        t = d
        acc = True
        if x != w != v and fx != fw != fv:
            u = x - 0.5 * ((x - v) ** 2 * (fx - fw) - (x - w) ** 2 * (fx - fv)) / \
                ((x - v) * (fx - fw) - (x - w) * (fx - fv))
            if a + e <= u <= c - e and abs(u - x) * e < g / 2:
                d = abs(u - x)
                acc = False

        if acc:
            if x < (c - a) / 2:
                u = x + K * (c - x)
                d = c - x
            else:
                u = x - K * (x - a)
                d = x - a
            if abs(u - x) < e:
                u = x + (-1 if u - x < 0 else 1) * e

        fu = function(u)
        func_count += 1
        if abs(fu - fx) <= e:
            return (u, fu, iter_count, func_count, length_values) if fu > fx \
                else (x, fx, iter_count, func_count, length_values)

        if fu <= fx:
            if u >= x:
                a = x
            else:
                c = x
            v = w
            w = x
            x = u
            fv = fw
            fw = fx
            fx = fu
        else:
            if u >= x:
                c = u
            else:
                a = u
            if fu <= fw and w == x:
                v = w
                w = u
                fv = fw
                fw = fu
            elif fu <= fv and v == x and v == w:
                v = u
                fv = fu

