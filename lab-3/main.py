import scipy.sparse
import numpy as np
import iteration_method as im
import lu_decomposition as lu

n = 3
matrix = scipy.sparse.__dict__["lil_matrix"]((n, n))

a = np.array([[5, -1, 3],
              [1, -4, 2],
              [2, -1, 5]])
b = np.array([5, 20, 10])

for i in range(n):
    for j in range(n):
        matrix[i, j] = a[i, j]

matrix = matrix.tocsr()
print(im.seidel_method(matrix, b))
print((lu.lu_decomposition(matrix)[0]).toarray())
print((lu.lu_decomposition(matrix)[1]).toarray())
print((lu.lu_decomposition(matrix)[0]*lu.lu_decomposition(matrix)[1]).toarray())
print(lu.solution(matrix, b))
print(lu.inverse_by_lu_decomposition(matrix))
