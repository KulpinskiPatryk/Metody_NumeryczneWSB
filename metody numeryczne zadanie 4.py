# Metody Numeryczne Rungego-Kutty 4 rzędu

def f(x0, y0, a, b, type_function):
    if type_function == "1":
        return a * x0 + b * y0
    elif type_function == "2":
        return a * x0 - b * y0
    elif type_function == "3":
        return a * x0 * b * y0
    elif type_function == "4":
        return (a * x0) / (b * y0)


def runge_kutta_method(x0, y0, h, n, type_function, a, b):
    for i in range(1, int(n) + 1):
        m1 = h * f(x0, y0, a, b, type_function)
        m2 = h * f(x0 + 0.5 * h, y0 + 0.5 * m1, a, b, type_function)
        m3 = h * f(x0 + 0.5 * h, y0 + 0.5 * m2, a, b, type_function)
        m4 = h * f(x0 + h, y0 + m3, a, b, type_function)
        y0 = y0 + (1/6)*(m1 + 2 * m2 + 2 * m3 + m4)
        x0 = x0 + h
    yi = y0
    xi = x0
    return xi, yi


def interfejs():
    print("Podaj wartości do obliczenia algorytmem Rungego-Kutty")
    x0 = input("Podaj x0 : ")
    y0 = input("Podaj y0 : ")
    h = input("Podaj odległość kroku : ")
    n = input("Podaj ilość kroków : ")
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
    return float(x0), float(y0), float(h), int(n), type_function, a, b


if __name__ == '__main__':
    x0, y0, h, n, type_function, a, b = interfejs()
    xi, yi = runge_kutta_method(x0, y0, h, n, type_function, a, b)
    print("Przy podanym y0, x0, kroku i ilośći korków wartość xi : " + str(xi) + " yi : " + str(yi))

