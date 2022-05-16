import numpy as np
import scipy

def solution(A, b):
    L, U, iterations = lu_decomposition(A)
    #Решаем L(Ux) = b
    #1) Ly = b
    y = lower_trivial_solution(L, b)
    #2) Ux = y
    x = upper_trivial_solution(U, y)
    return x, iterations

def lu_decomposition(A):
    N = A.shape[0]
    #init empty matrix
    L = scipy.sparse.__dict__["lil_matrix"]((N, N))
    U = L.copy()

    iterations = 0
    for i in range(N):

        # U
        for k in range(i, N):

            iterations += 1
            # sum(L(i, j) * U(j, k)) (j,i-1)
            sum = 0
            for j in range(i):
                sum += (L[i,j] * U[j,k])
            # U(i, k)
            U[i,k] = A[i,k] - sum

        # L
        for k in range(i, N):
            iterations += 1
            if i == k:
                L[i,i] = 1  # Главн. диагональ = 1
            else:

                # sum(L(k, j) * U(j, i)) (j,i-1)
                sum = 0
                for j in range(i):
                    sum += (L[k, j] * U[j, i])

                # L(k, i)
                L[k,i] = ((A[k,i] - sum) / U[i,i])

    return L.tocsr(), U.tocsr(), iterations


def lower_trivial_solution(A, b):
    #Ax=b, где A - нижняя треуг. матрица
    x = np.zeros(len(b))
    x[0] = b[0]

    for i in range(1, len(b)):
        x[i] = b[i] - A[i] * x

    return x


def upper_trivial_solution(A, b):
    #Ax=b, где A - верхняя треуг. матрица
    N = len(b)
    x = np.zeros(N)
    x[-1] = b[-1] / A[-1, -1]

    for i in reversed(range(N - 1)):
        x[i] = (b[i] - A[i] * x) / A[i, i]

    return x

def inverse_by_lu_decomposition(A):
    E = np.eye(A.shape[0])
    Inv = []
    for e in E:
        x = solution(A, e)
        Inv.append(x)
    return np.array(Inv).transpose()

