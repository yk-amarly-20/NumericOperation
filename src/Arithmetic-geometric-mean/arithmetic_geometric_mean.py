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

    def __init__(self, a_init, b_init, eps=0.001, verbose=False, iteration=10000):

        self.eps = eps
        self.verbose = verbose
        self.iteration = iteration

        self.a = np.zeros(self.iteration + 2)
        self.a[0] = a_init
        self.b = np.zeros(self.iteration + 2)
        self.b[0] = b_init

    def fit(self):
        """calculate mean
        """

        for i in range(self.iteration):
            self._calc_a(i)
            self._calc_b(i)

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

    def show_result(self):
        """show result of calculation by graph
        """

        plt.plot()
