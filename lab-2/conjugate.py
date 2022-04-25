import numpy as np
import numdifftools as nd
from gradient_descent import vector_mod, vector_normalization
#from math_util import norm_gradient
import goldenSection
M = 50000
K = (3 - (5 ** 0.5)) / 2

def conjugate_method(f, x0, eps, lambda_b):
    trajectory = [x0]
    k = 0
    x_k = x0
    x_next = x0
    t = 0
    grad = grad_prev = vector_normalization(nd.Gradient(f)(x_k))
    d = -grad
    while k < M:
        x_k = x_next
        grad_prev = grad
        grad = nd.Gradient(f)(x_k)
        if vector_mod(grad) < eps:
            break
        grad = vector_normalization(grad)
        k += 1
        b = lambda_b(grad, grad_prev)
        d = -grad + b * d
        f_min = lambda tmp: f((x_k + tmp * d))
        t = goldenSection.calc(f_min, 0., 10000000., eps)[0]
        x_next = x_k + t * d
        trajectory.append(x_next)
        if vector_mod(x_next - x_k) < eps and abs(f(x_next) - f(x_k)) < eps:
            break
    print("Iteration count: ", k)
    print(trajectory[k - 1])
    return trajectory


def conjugate_gradient_method(f, x0, eps):
    return conjugate_method(
        f, x0, eps, lambda grad, grad_prev: vector_mod(grad) ** 2 / vector_mod(grad_prev) ** 2
    )