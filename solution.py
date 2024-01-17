import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def E_main(x):
    if 0 <= x <= 1:
        return 2
    elif 1 < x <= 2:
        return 6


def e(i, x):
    if x < h * (i - 1) or x > h * (i + 1):
        return 0
    if x < h * i:
        return x / h - i + 1
    return - x / h + i + 1


def e_prim(i, x):
    if x < h * (i - 1) or x > h * (i + 1):
        return 0
    if x < h * i:
        return 1 / h
    return - 1 / h


def L(i):
    return -14 * e(i, 0)  # -7 * E_main(0) * e_prim(i, 0)


def B(i, j, s, k):
    interior = quad(lambda x: E_main(x) * e_prim(i, x) * e_prim(j, x), s, k)[0]
    rest = 2*e(i, 0)*e(j, 0)  # E_main(0)*e(i, 0)*e(j, 0)
    return interior - rest


def create_Lmat(e_range):
    return np.array([L(i) for i in e_range])


def create_Bmat(e_range):
    B_matrix = np.zeros((elements_count, elements_count))
    for i in e_range:
        for j in e_range:
            if abs(i - j) <= 1:
                l = min(i, j)
                r = max(i, j)
                s = 2.*max(0, (l - 1)/elements_count)
                k = 2.*min(1, (r + 1)/elements_count)
                res = B(j, i, s, k)
                B_matrix[i][j] = res
    return B_matrix


def solve(n):
    global h
    global elements_count
    h = 2 / n
    e_range = range(0, n+1)
    elements_count = len(e_range)

    x = [h*i for i in e_range]

    B_matrix = create_Bmat(e_range)
    L_vector = create_Lmat(e_range)

    y = np.linalg.solve(B_matrix, L_vector) + 3
    plt.plot(x, y)
    plt.show()
    return x, y


solve(1000)
