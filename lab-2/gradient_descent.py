import numdifftools as nd
from numpy import array


def vector_mod(x):
    return sum([i ** 2 for i in x]) ** 0.5

def vector_normalization(x):
    c = x.copy()
    length = vector_mod(c)
    return array([i/length for i in c])


MAX_ITERATIONS = 1000

def gradient_descent(f, x0, eps, t_0, learning_rate=1.):
    history = [x0]
    x_k = x0
    x_k1 = x0
    t_k = t_0
    iteration = 0
    alpha = learning_rate

    while iteration < MAX_ITERATIONS:
        grad = nd.Gradient(f)(x_k)
        iteration += 1
        x_k = x_k1

        if vector_mod(grad) < eps:
            break

        grad = vector_normalization(grad)

        # именно тут можно внедрить методы для использование других методов шага t_k
        # t_k = t_0 * alpha ** k
        t_k *= alpha # const т.к. alpha = 1

        # сбрасываем шаг (useless для константного шага) понадобиться для других
        if iteration % 50 == 0:
            t_k = t_0

        x_k1 = x_k - t_k * grad

        if f(x_k1) - f(x_k) >= 0:
            print("Последовательность стала возрастающей")
            break

        # метод дробления шага TODO: можно будет задать работу/не работу этого метода во время инициализции
        # while f(x_k1) - f(x_k) >= 0:
        #     t_k *= 1/2
        #     x_k1 = x_k - t_k * grad

        history.append(x_k1)

        length = vector_mod(x_k1 - x_k)
        if length < eps and abs(f(x_k) - f(x_k1)) < eps:
            print("SUCCESS")
            break
    if (iteration == MAX_ITERATIONS):
       print('Превышен лимит итераций')
    print("Iteration count: ", iteration)
    return history
