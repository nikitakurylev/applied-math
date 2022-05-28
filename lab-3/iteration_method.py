import numpy as np


def get_prod_and_diag(csr, vec1, vec2, index_row):
    start_idx = csr.indptr[index_row]
    end_idx = len(csr.data)
    if index_row + 1 < csr.shape[0]:
        end_idx = csr.indptr[index_row + 1]

    curr_vec = vec1
    product = 0
    diag_value = 0
    for i in range(start_idx, end_idx):
        index_column = csr.indices[i]
        val = csr.data[i]

        if index_column >= index_row:
            curr_vec = vec2

        if index_column == index_row:
            diag_value = val
            continue

        product += val * curr_vec[index_column]

    return product, diag_value


def seidel_method(A, b, eps = 2e-3, max_iter = 20000):
    n = A.shape[0]
    x = b

    iterations = 0
    for stage in range(max_iter):
        current_x = np.zeros(n)

        iterations += 1
        for i in range(n):
            product, diag_value = get_prod_and_diag(A, current_x, x, i)
            current_x[i] = (b[i] - product) / diag_value

        tmp_mat = np.matmul(A.toarray(), current_x)
        is_enough = True
        for i in range(len(tmp_mat)):
            if abs(tmp_mat[i] - b[i]) > eps:
                is_enough = False
        if is_enough:
            break
        # if np.allclose(x, current_x, rtol=eps):
        #     break

        x = current_x
    return x, iterations
