import numdifftools as nd
from numpy import array
import goldenSection,fibonacci

def vector_mod(x):
    return sum([i ** 2 for i in x]) ** 0.5


def vector_normalization(x):
    c = x.copy()
    length = vector_mod(c)

    return array([i / length for i in c])


MAX_ITERATIONS = 10000


def const_step(t_k, t_0, x_k1, x_k, grad, f, eps):
    x_k1 = x_k - t_k * grad
    print(x_k1)
    return t_k, t_0, x_k1, x_k


def splitting_method(t_k, t_0, x_k1, x_k, grad, f, eps):
    x_k1 = x_k - t_k * grad
    while (f(x_k1) - f(x_k) > 0):
        t_k *= 0.5
        x_k1 = x_k - t_k * grad


    return t_k, t_0, x_k1, x_k



def golden_section(t_k,t_0,x_k1,x_k,grad,f, eps):
    f_find = lambda l: f((x_k - l * grad))
    min_arg,_ = goldenSection.calc(f_find, 0., 5., eps)
    t_k = min_arg

    x_k1 = x_k - t_k * grad

    return t_k, t_0, x_k1, x_k

def fibonacci_method(t_k,t_0,x_k1,x_k,grad,f, eps):
    f_find = lambda l: f((x_k - l * grad))
    min_arg, _ = fibonacci.calc(f_find, 0., 5., eps)
    t_k = min_arg

    x_k1 = x_k - t_k * grad

    return t_k, t_0, x_k1, x_k

def gradient_descent(f, x0, eps, t_0, method):
    history = [x0]
    x_k = x0
    x_k1 = x0
    t_k = t_0
    iteration = 0
    #alpha = learning_rate

    while iteration < MAX_ITERATIONS:
        grad = nd.Gradient(f)(x_k)
        iteration += 1
        x_k = x_k1

        if vector_mod(grad) < eps:
            break

        grad = vector_normalization(grad)

        # именно тут можно внедрить методы для использование других методов шага t_k
        t_k, t_0, x_k1, x_k = method(t_k, t_0, x_k1, x_k, grad, f, eps)

        # сбрасываем шаг у метода
        if iteration % 100 == 0:
            t_k = t_0

        history.append(x_k1)
        if f(x_k1) - f(x_k) >= 0:
            print("Последовательность стала возрастающей, либо неизменяющейся")
            break



        length = vector_mod(x_k1 - x_k)
        if length < eps and abs(f(x_k) - f(x_k1)) < eps:
            print("SUCCESS")
            break
    if (iteration == MAX_ITERATIONS):
        print('Превышен лимит итераций')
    print("Iteration count: ", iteration)
    return history
