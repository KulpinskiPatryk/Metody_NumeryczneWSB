import math
import numpy as np
import matplotlib.pyplot as plt


def linear_approx(x_inputs, y_inputs):
    n = len(x_inputs)
    xy = [x_inputs[i] * y_inputs[i] for i in range(n)]
    xx = [x_inputs[i] ** 2 for i in range(n)]

    p0 = (sum(xy) - sum(x_inputs) * sum(y_inputs) / n) / (sum(xx) - sum(x_inputs) ** 2 / n)
    p1 = (sum(y_inputs) - p0 * sum(x_inputs)) / n

    return np.array([p0, p1])


def log_approx(x_inputs, y_inputs):
    n = len(x_inputs)

    logX = [math.log(xi) for xi in x_inputs]
    logX2 = [logXi * logXi for logXi in logX]
    yLogX = [y_inputs[i] * logX[i] for i in range(n)]

    sum_logX = round(sum(logX), 3)
    sum_y = round(sum(y_inputs), 3)
    sum_logX2 = round(sum(logX2), 3)
    sum_yLogX = round(sum(yLogX), 3)

    # Wyznaczenie parametrów A i B
    B = (n * sum_yLogX - sum_y * sum_logX) / (n * sum_logX2 - sum_logX ** 2)
    A = (sum_y - B * sum_logX) / n

    return np.array([round(A, 3), round(B, 3)])

def exp_approx(x_inputs, y_inputs):
    n = len(x_inputs)

    logY = [math.log(yi) for yi in y_inputs]

    sum_x = sum(x_inputs)
    sum_logY = sum(logY)  # Usunięto zaokrąglenie
    sum_x2 = sum(xi**2 for xi in x_inputs)
    sum_xlogY = sum(x_inputs[i]*logY[i] for i in range(n))  # Usunięto zaokrąglenie

    # Obliczanie parametrów a i b
    b = (n * sum_xlogY - sum_x * sum_logY) / (n * sum_x2 - sum_x ** 2)
    ln_a = (sum_logY - b * sum_x) / n

    # Powrót do parametrów a i b aproksymacji eksponencjalnej
    a = math.exp(ln_a)

    return a, b

if __name__ == '__main__':

    fig, axs = plt.subplots(3)

    #Zad 1
    x_points = np.array([])
    y_points = np.array([])
    x_inputs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y_inputs = np.array([10, 18, 22, 27, 36, 49, 56, 64, 70, 78])

    params = linear_approx(x_inputs, y_inputs)

    step = 0.01
    for x in np.arange(x_inputs.min(), x_inputs.max() + step, step):
        x_points = np.append(x_points, x)
        y_points = np.append(y_points, [params[0] + params[1] * x])  # linear function

    axs[0].plot(x_points, y_points)

    # Zad 2
    x_points = np.array([])
    y_points = np.array([])
    x_inputs = np.array([1, 2, 3, 4, 5, 6])
    y_inputs = np.array([0.03, 0.3, 0.45, 0.6, 0.7, 0.8])

    params = log_approx(x_inputs, y_inputs)

    step = 0.01
    for x in np.arange(0.01, x_inputs.max() + step, step):
        x_points = np.append(x_points, x)
        y_points = np.append(y_points, [params[1] * math.log(x) + params[0]])

    axs[1].plot(x_points, y_points)

    # Zad 3
    x_points = np.array([])
    y_points = np.array([])
    x_inputs = np.array([0, 60, 120, 180, 240, 300])
    y_inputs = np.array([100, 90, 80, 72, 65, 58])

    a, b = exp_approx(x_inputs, y_inputs)
    for x in np.arange(x_inputs.min(), x_inputs.max(), step):
        x_points = np.append(x_points, x)
        y_points = np.append(y_points, a * math.exp(b*x))
    axs[2].plot(x_points, y_points)

    plt.show()
