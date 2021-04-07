from lab1.brents_method import brents_method
from lab1.parabolic_interpolation import parabolic_interpolation

if __name__ == '__main__':
    print(parabolic_interpolation(-5.2, 2.2, 0.005))
    print(brents_method(-5.2, 2.2, 0.005))
