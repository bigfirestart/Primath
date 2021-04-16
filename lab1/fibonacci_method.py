from math import sin, cos, sqrt, exp, log10, pow, pi


class fibonacci_searcher:

    def __init__(self, func):
        self.func = func

    def find_local_min(self, left, right, length, eps):
        fibonacci_list = [1, 1]

        index = 1
        while fibonacci_list[index] < (right - left) / length:
            index += 1
            fibonacci_list.append(fibonacci_list[index - 1] + fibonacci_list[index - 2])

        n = len(fibonacci_list) - 1
        lambda_ = left + fibonacci_list[n - 2] / fibonacci_list[n] * (right - left)
        mu_ = left + fibonacci_list[n - 1] / fibonacci_list[n] * (right - left)

        f_lambda = self.func(lambda_)
        f_mu = self.func(mu_)

        for k in range(1, n):
            if f_lambda > f_mu:
                left = lambda_
                lambda_ = mu_
                f_lambda = f_mu
                if k == n - 2:
                    mu_ = left + (0.5 + eps) * (right - left)
                else:
                    mu_ = left + fibonacci_list[n - k] / fibonacci_list[n - k + 1] * (right - left)
                f_mu = self.func(mu_)
            else:
                right = mu_
                mu_ = lambda_
                f_mu = f_lambda
                if k == n - 2:
                    lambda_ = left + (0.5 - eps) * (right - left)
                else:
                    lambda_ = left + fibonacci_list[n - k - 1] / fibonacci_list[n - k + 1] * (right - left)
                f_lambda = self.func(lambda_)

        return (right + left) / 2


searcher = fibonacci_searcher(lambda x: eval("exp(sin(x)) * (x ** 2)"))
print(searcher.find_local_min(-5, 2.5, 0.001, 0.01))
