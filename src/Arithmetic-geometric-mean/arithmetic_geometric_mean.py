# calculate Arithmetric Geometric Mean
import numpy as np
import matplotlib.pyplot as plt

class ArithmeticGeometricMean():
    """calculate

    Attributes:
        a_init (float): initialized value of a
        b_init (float): initialized value of b
        eps (float): stop value

    """

    def __init__(self, a_init, b_init, t_init, iteration=10):

        self.iteration = iteration
        self.a = np.zeros(self.iteration + 1)
        self.a[0] = a_init
        self.b = np.zeros(self.iteration + 1)
        self.b[0] = b_init
        self.t = np.zeros(self.iteration)
        self.t[0] = t_init

    def fit(self):
        """calculate mean
        """

        for i in range(self.iteration):
            self._calc_a(i)
            self._calc_b(i)

        for j in range(self.iteration - 1):
            self._calc_t(j)

        return self.a, self.b

    def _calc_a(self, n):
        """calculate a

        Params:
            n (int): the number of step
        """

        self.a[n + 1] = (self.a[n] + self.b[n]) / 2.0

    def _calc_b(self, n):
        """calculate b

        Params:
            n (int): the number of step
        """

        self.b[n + 1] = np.sqrt(self.a[n] * self.b[n])

    def _calc_t(self, n):
        """calculate t

        Params:
            n (int): the number of step
        """

        self.t[n + 1] = self.t[n] - self._calc_p(n) * (self.a[n] - self.a[n + 1]) ** 2

    def _calc_p(self, n):
        """calculate p

        Params:
            n (int): the number of step
        """

        return 2**n

    def show_result(self):
        """show result of calculation by graph
        """

        x = np.arange(self.iteration + 1)
        plt.plot(x, self.a)
        plt.plot(x, self.b)
        plt.show()

    def estimate_pi(self):
        """estimate pi
        """

        return (self.a[-1] + self.b[-1]) ** 2 / (4 * self.t[-1])
