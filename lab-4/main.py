from array import array
from math import sin, cos, atan, pi
import numpy as np
from analysis import gilbertMatrix
import matplotlib.pyplot as plt


def jacobi_method(M, ap=1e-6, rp=1e-5):
    '''
    M - симметричная квадратичная матрица
    ap - абсолютная погрешность
    rp - относительная погрешность
    '''
    n, m = M.shape # определяем размерность матрицы
    assert n == m, 'Матрица не квадратичная'
    assert np.sum(M == M.T) != (m + 1) * (n + 1), 'Матрица не симметричная'

    def create_rotate_matrix(n, i, j, theta):
        Q = np.zeros([n, n])
        # заполняем диагональные элементы
        for k in range(n):
            if k not in [i, j]:
                Q[k, k] = 1
        Q[i, i] = cos(theta)
        Q[j, j] = cos(theta)
        Q[i, j] = sin(theta)
        Q[j, i] = -sin(theta)
        return Q

    M_updated = M
    Q_updated = np.identity(n)
    max_val = 999999  # бесконечность(нужен для первой итерации)
    max_val_old = 0
    iterations = 0
    while True:
        # критерий останова
        change = abs(max_val - max_val_old)
        if max_val < ap or change < rp: break
        max_val_old = max_val
        # находим максимальный недиагональный элемент
        max_val = np.abs(np.triu(M_updated, k=1)).max()
        # находим его индекс
        max_val_idx = np.abs(np.triu(M_updated, k=1)).argmax()
        i, j = np.unravel_index(max_val_idx, M_updated.shape)
        # критерий останова 2
        if max_val < ap or max_val < rp * max_val:
            break
        # вычисляем угол поворота матрицы
        try:
            theta = atan(2 * M_updated[i, j] / (M_updated[j, j] - M_updated[i, i])) / 2
        except:  # incase the denominator is 0
            if M_updated[i, j] >= 0:
                theta = pi / 4
            else:
                theta = -pi / 4
        # создаем матрицу поворота(Гивенса)
        Q = create_rotate_matrix(n, i, j, theta)
        iterations = iterations + n
        # обновляем Q(это будет собственные вектора)
        Q_updated = np.dot(Q_updated, Q)
        # получаем новый вектор M используя левое и првое умножениe: Q.T*M*Q
        M_updated = np.dot(np.dot(Q.T, M_updated), Q)

    # сортим индексы собственных значений
    sort_indices = M_updated.diagonal().argsort()[::-1]

    return M_updated.diagonal()[sort_indices], Q_updated.T[sort_indices], iterations

A = [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]
# using numpy
vals, vecs = np.linalg.eig(A)
print(vals)
print(vecs.T)

# using above func
vals, vecs, iterations = jacobi_method(np.array(A))
print(iterations)
print(vals)
print(vecs)


# 2
B = [[2, 1, 0], [1, 4, 1], [0, 1, 4]]
# using numpy
vals, vecs = np.linalg.eig(B)
print(vals)
print(vecs.T)

vals, vecs, iterations = jacobi_method(np.array(B))
print(iterations)
print(vals)
print(vecs)

iters = []
for k in range(2,200):
    vals, vecs, iterations = jacobi_method(gilbertMatrix(k))
    print(str(k) + " - " + str(iterations))
    iters.append(iterations)

plt.plot(range(2, 200), iters)
plt.show()