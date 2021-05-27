from math import cos, sin, exp, pi
from scipy.special import roots_legendre
from typing import Callable as Call
import matplotlib.pyplot as plt

class Integral(object):
    def __init__(self, lm: list[list[float]], n: list[int], fn: list[int]):
        self.lm = lm
        self.n = n
        self.f1 = Integral.simpson if (fn[0]) else Integral.gauss
        self.f2 = Integral.simpson if (fn[1]) else Integral.gauss

    def __call__(self, p: float) -> float:
        f = Integral.__integrated(p)

        inner = lambda x: self.f2(
            lambda val1: f(x, val1),
            self.lm[1][0],
            self.lm[1][1],
            self.n[1])
        integ = lambda: self.f1(
            inner,
            self.lm[0][0],
            self.lm[0][1],
            self.n[0])

        return integ()

    @staticmethod
    def __integrated(p: float) -> Call[[float, float], float]:
        t = lambda x, y: 2 * cos(x) / (1 - sin(x) ** 2 * cos(y) ** 2)
        return lambda x, y: 4 / pi * (1 - exp(-p * t(x, y))) * cos(x) * sin(x)

    @staticmethod
    def simpson(f: Call[[float], float], a: float, b: float,
                n: int) -> float:
        if n < 3 or n % 2 == 0:
            raise Exception("Wrong n value")

        h = (b - a) / (n - 1.0)
        x = a
        res = 0.0

        for i in range((n - 1) // 2):
            res += f(x) + 4 * f(x + h) + f(x + 2 * h)
            x += 2 * h

        return res * h / 3

    @staticmethod
    def gauss(f: Call[[float], float], a: float, b: float,
              n: int) -> float:
        def p2v(p: float, c: float, d: float) -> float:
            return (d + c) / 2 + (d - c) * p / 2

        x, w = roots_legendre(n)
        return sum([(b - a) / 2 * w[i] * f(p2v(x[i], a, b)) for i in range(n)])


def plot(fs, sc, n_mas, m_mas, first_methods, second_methods):
    plt.clf()

    plt.xlabel("Параметр t")
    plt.ylabel("Результат")
    plt.grid(which='minor', color='k', linestyle=':')
    plt.grid(which='major', color='k')

    for i in range(len(fs)):
        x, y = [], []
        j = sc[0]
        while j < sc[2]:
            x.append(j)
            y.append(fs[i](j))
            j += sc[1]

        m1 = "Г"
        m2 = "С"
        if (first_methods[i] == 1):
            m1 = "С"
            m2 = "Г"
        lbl = "N = {:}, M = {:}, ".format(n_mas[i], m_mas[i]) + m1 + " - " + m2
        plt.plot(x, y, label = lbl)

    plt.legend()
    plt.savefig('rez.png')
    plt.show()

def main():
    sc = [0.05, 0.05, 10.0]

    n_mas, m_mas = [], []
    first_methods, second_methods = [], []
    integrals = []

    end = '1'
    while end == '1':
        n_mas.append(int(input("Введите N: ")))
        m_mas.append(int(input("Введите M: ")))

        p = float(input("Введите t (параметр тау): "))

        first_methods.append(int(input("Выберите метод интегрирования для напралений (0 - Гаусс-Симпсон, 1 - Симпсон-Гаусс): ")))

        if (first_methods[0] == 1):
            second_methods.append(0)
        else:
            second_methods.append(1)

        lm = [[0, pi / 2], [0, pi / 2]]

        integrals.append(Integral(lm, [n_mas[-1], m_mas[-1]], [first_methods[-1], second_methods[-1]]))

        print("Результат = {:.7f}".format(integrals[-1](p)))

        end = input("Продолжить программу? (1 - да): ")

    plot(integrals, sc, n_mas, m_mas, first_methods, second_methods)

if __name__ == '__main__':
    main()
