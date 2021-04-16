from brents_method import brents_method
from parabolic_interpolation import parabolic_interpolation
from half_interval import half_divide_method
import math as m


def f(x):
    return m.exp(m.sin(x)) * x ** 2


if __name__ == '__main__':
    a = -5.2
    b = 2.2
    e = 0.005
    print(half_divide_method(a=a, b=b, e=e, f=f))
    print(parabolic_interpolation(x1=a, x3=b, e=e, function=f))
    print(brents_method(a=a, c=b, e=e, function=f))
