from math import sqrt

phi = (sqrt(5) + 1) / 2


def imag_sqrt(x):
    if x >= 0:
        return sqrt(x)

    else:
        return sqrt(-x) * 1j


def quadratic(a, b, c):
    root_1 = (-b + imag_sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    root_2 = (-b - imag_sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    return root_1, root_2


if __name__ == '__main__':
    print(quadratic(1, 1, -1))
