import numpy as np
from math_util import gradient, hessian_matrix, norm, norm_gradient, normalize
import goldenSection
M = 50000
K = (3 - (5 ** 0.5)) / 2

def conjugate_method(f, x0, eps, lambda_b):
    trajectory = [x0]
    k = 0
    x_k = x0
    x_next = x0
    t = 0
    grad = grad_prev = norm_gradient(f, x_k)
    d = -norm_gradient(f, x_k)
    while k < M:
        x_k = x_next
        grad_prev = grad
        grad = gradient(f, x_k)
        if norm(grad) < eps:
            break
        grad = normalize(grad)
        k += 1
        b = lambda_b(grad, grad_prev)
        d = -grad + b * d
        f_min = lambda tmp: f(*(x_k + tmp * d))
        t = goldenSection.calc(f_min, 0., 10000000., eps)[0];
        x_next = x_k + t * d
        trajectory.append(x_next)
        if norm(x_next - x_k) < eps and abs(f(*x_next) - f(*x_k)) < eps:
            break
    return trajectory


def conjugate_gradient_method(f, x0, eps):
    return conjugate_method(
        f, x0, eps, lambda grad, grad_prev: norm(grad) ** 2 / norm(grad_prev) ** 2
    )