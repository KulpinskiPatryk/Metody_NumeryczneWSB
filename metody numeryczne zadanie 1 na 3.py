import math

import matplotlib.pyplot as plt

x1, y1, x2, y2, x3, y3 = 0, 4, 1, 2, 2.5, 2.75


def calculate_points_x():
    n = 100
    intervals = (max(x1, x2, x3) - min(x1, x2, x3)) / n
    flag = min(x1, x2, x3)
    calc_x = []
    for a in range(n + 1):
        calc_x.append(flag)
        flag += intervals
    return calc_x


def calcualte_points_y(a):
    calc_y = []
    for i in a:
        calc_y.append(basic_lagrange_algoritm(i))
    return calc_y


def basic_lagrange_algoritm(x):
    a = y1 / ((x1 - x2) * (x1 - x3)) + y2 / ((x2 - x1) * (x2 - x3)) + y3 / ((x3 - x1) * (x3 - x2))
    a = math.ceil(a)
    b = y1 * (x2 + x3) / ((x1 - x2) * (x1 - x3)) + y2 * (x1 + x3) / ((x2 - x1) * (x2 - x3)) + y3 * (x1 + x2) / (
            (x3 - x1) * (x3 - x2))
    b = math.ceil(b)
    c = (y1 * x2 * x3) / ((x1 - x2) * (x1 - x3)) + (y2 * x1 * x3) / ((x2 - x1) * (x2 - x3)) + (y3 * x1 * x2) / (
            (x3 - x1) * (x3 - x2))
    c = math.ceil(c)
    y = (a * x * x) - (b * x) + c
    return y


if __name__ == '__main__':
    calucalted_x = calculate_points_x()
    calcualted_y = calcualte_points_y(calucalted_x)
    plt.scatter([x1, x2, x3], [y1, y2, y3], color="red")
    plt.plot(calucalted_x, calcualted_y)
    plt.show()
