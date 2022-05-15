import scipy.sparse
import numpy as np
import iteration_method as im

n = 3
matrix = scipy.sparse.__dict__["lil_matrix"]((n, n))

a = np.array([[5, -1, 3], [1, -4, 2], [2, -1, 5]])
b = np.array([5, 20, 10])

for i in range(n):
    for j in range(n):
        matrix[i, j] = a[i, j]

matrix = matrix.tocsr()
print(im.seidel_method(matrix, b))