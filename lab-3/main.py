import scipy.sparse
import numpy as np
import iteration_method as im
import lu_decomposition as lu
import analysis as an

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

a = np.random.randint(-4, 0, (n, n))

print("diagonal")
print("seidel")
for k in range(0, 100):
    print(an.analyze(a, im.seidel_method, k, 3))

print("lu")
for k in range(0, 100):
    print(an.analyze(a, lu.solution, k, 3))

print("gilbert")
print("seidel")
print(an.gilbert(im.seidel_method, 100))

print("lu")
print(an.gilbert(lu.solution, 100))
