from brents_method import brents_method
from parabolic_interpolation import parabolic_interpolation
from half_interval import half_divide_method
from golden_ratio import golden_ratio
from fibonacci_method import fibonacci_method
import math as m


def f(x):
    return m.exp(m.sin(x)) * x ** 2


if __name__ == '__main__':
    a = -5.0
    b = 2.5
    e = 0.005
    eps = 0.01
    print(half_divide_method(a=a, b=b, e=e, f=f))
    print(golden_ratio(l=a, r=b, eps=e, f=f))
    print(parabolic_interpolation(x1=a, x3=b, e=e, function=f))
    print(brents_method(a=a, c=b, e=e, function=f))
    print(fibonacci_method(left=a, right=b, length=e, eps=eps, func=f))
