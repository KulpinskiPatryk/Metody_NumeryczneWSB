import math

import matplotlib.pyplot as plt

x1, y1, x2, y2, x3, y3 = 0, 4, 1, 2, 2.5, 2.75


def MakePlt(a, b, c):
    maks = max(x1, x2, x3)
    mini = min(x1, x2, x3)
    zakres = maks - mini
    iterable = zakres / 100
    pointsY = []
    pointsX = []
    while iterable <= zakres:
        pointsY.append(funkcjaKwadratowa(a, b, c, iterable))
        pointsX.append(iterable)
        iterable = iterable + zakres / 100
    plt.scatter([x1,x2,x3],[y1,y2,y3],color="red")
    plt.xlim(mini, maks)
    plt.plot(pointsX, pointsY)
    plt.show()


def obliczA():
    a = y1 / ((x1 - x2) * (x1 - x3)) + y2 / ((x2 - x1) * (x2 - x3)) + y3 / ((x3 - x1) * (x3 - x2))
    a = math.ceil(a)
    return a


def obliczB():
    b = y1 * (x2 + x3) / ((x1 - x2) * (x1 - x3)) + y2 * (x1 + x3) / ((x2 - x1) * (x2 - x3)) + y3 * (x1 + x2) / (
                (x3 - x1) * (x3 - x2))
    b = math.ceil(b)
    return b


def obliczC():
    c = (y1 * x2 * x3) / ((x1 - x2) * (x1 - x3)) + (y2 * x1 * x3) / ((x2 - x1) * (x2 - x3)) + (y3 * x1 * x2) / (
                (x3 - x1) * (x3 - x2))
    c = math.ceil(c)
    return c


def funkcjaKwadratowa(a, b, c, x):
    y = (a * x * x) - (b * x) + c
    return y


if __name__ == '__main__':
    MakePlt(obliczA(), obliczB(), obliczC())
