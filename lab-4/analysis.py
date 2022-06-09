import scipy.sparse
import numpy as np

def analyze(a, method, k, n):
    matrix = scipy.sparse.__dict__["lil_matrix"]((n, n))

    for i in range(n):
        t1 = -sum(a[i][j] for j in range(i))
        t2 = -sum(a[i][j] for j in range(i + 1, n))
        t = t1 + t2
        for j in range(n):
            if i != j:
                matrix[i, j] = a[i, j]
            else:
                matrix[i, j] = t + pow(10.0, -k)
    x = np.arange(n)
    f = np.matmul(matrix.toarray(), x)
    result, iterations = method(matrix.tocsr(), f)
    return np.average(result - x), iterations

def conditionalMatrix(a, k, n):
    matrix = np.zeros((n, n))

    for i in range(n):
        t1 = -sum(a[i][j] for j in range(i))
        t2 = -sum(a[i][j] for j in range(i + 1, n))
        t = t1 + t2
        for j in range(i, n):
            if i != j:
                matrix[i, j] = a[i, j]
                matrix[j, i] = a[i, j]
            else:
                matrix[i, j] = t + pow(10.0, -k)
    
    return matrix

def gilbert(method, n):
    matrix = gilbertMatrix(n)

    x = np.arange(n)
    f = np.matmul(matrix.toarray(), x)
    result, iterations = method(matrix.tocsr(), f)
    return np.average(result - x), iterations

def gilbertMatrix(n):
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i, j] = 1.0 / (i + j + 1)
    return matrix
