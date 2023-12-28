# Metody Numeryczne Euler
import matplotlib.pyplot as plt


def f(x0, y0, a, b, type_function):
    if type_function == "1":
        return a * x0 + b * y0
    elif type_function == "2":
        return a * x0 - b * y0
    elif type_function == "3":
        return a * x0 * b * y0
    elif type_function == "4":
        return (a * x0) / (b * y0)


def euler_method(x0, y0, h, n, type_function, a, b):
    x_table = []
    y_table = []
    for i in range(int(n)):
        y0 = y0 + h * f(x0, y0, a, b, type_function)
        x0 = x0 + h
        x_table.append(x0)
        y_table.append(y0)
    return x_table, y_table


def euler_method_improved(x0, y0, h, n, type_function, a, b):
    x_table = []
    y_table = []
    for i in range(int(n)):
        m = y0 + h * f(x0, y0, a, b, type_function)
        y0 = y0 + m * h
        x0 = x0 + h
        x_table.append(x0)
        y_table.append(y0)
    return x_table, y_table


def interfejs():
    print("Podaj wartości do obliczenia algorytmem Eulera")
    x0 = input("Podaj x0 : ")
    y0 = input("Podaj y0 : ")
    h = input("Podaj odległość kroku : ")
    n = input("Podaj ilość kroków : ")
    type = input("Algorytm podstawowy(p) czy ulepszony(u) ? : ")
    print("Wybierz postać Funkcji : ")
    print("(1) F(x,y) = a*x + b*y")
    print("(2) F(x,y) = a*x - b*y")
    print("(3) F(x,y) = a*x * b*y")
    print("(4) F(x,y) = a*x / b*y")
    type_function = input("Wybór (1,2,3,4) : ")
    a = 0
    b = 0
    while a == 0:
        a = int(input("Podaj stałą a różną od 0 do funkcji : "))
    while b == 0:
        b = int(input("Podaj stałą b różną od 0 do funkcji : "))
    return float(x0), float(y0), float(h), int(n), type, type_function, a, b


if __name__ == '__main__':
    calculated_x = []
    calculated_y = []
    x0, y0, h, n, type, type_function, a, b = interfejs()
    if type == 'p':
        calculated_x, calcualted_y = euler_method(x0, y0, h, n, type_function, a, b)
    if type == 'u':
        calculated_x, calcualted_y = euler_method_improved(x0, y0, h, n, type_function, a, b)
    plt.scatter(calculated_x, calcualted_y, color="red")
    plt.plot(calculated_x, calcualted_y)
    plt.show()
