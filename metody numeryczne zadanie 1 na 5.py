import matplotlib.pyplot as plt

x = [-2, -1, 1, 3, 4, 5, 7, 11]
y = [9, 4, 0, 4, 9, 16, 20, 5]


def make_points():
    n = 100
    intervals = (max(x) - min(x)) / n
    flag = min(x)
    val_x = []
    for a in range(n+1):
        val_x.append(flag)
        flag += intervals
    return val_x


def lagrange_algorithm(val_x):
    suma = 0
    for i in range(len(x)):
        base = y[i]
        for j in range(len(x)):
            if i != j:
                base = base * (val_x - x[j]) / (x[i] - x[j])
        suma = suma + base
    return suma


def list_of_lagrange_y(a):
    calc_y = []
    for i in a:
        calc_y.append(lagrange_algorithm(i))
    return calc_y


if __name__ == '__main__':
    calculated_x = make_points()
    calcualted_y = list_of_lagrange_y(calculated_x)
    plt.scatter(x, y, color='red')
    plt.plot(calculated_x, calcualted_y)
    plt.show()
