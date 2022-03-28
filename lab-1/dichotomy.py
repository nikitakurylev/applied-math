def calc(func, a, b, precision):
    iteration_count = 0
    while b - a > precision:
        middle = (a + b) / 2
        x1 = middle - precision / 3
        x2 = middle + precision / 3
        f1 = func(x1)
        f2 = func(x2)
        if f1 > f2:
            a = x1
        elif f1 < f2:
            b = x2
        else:
            a = x1
            b = x2
        iteration_count += 1
    print("Dichotomy method: " + str(iteration_count) + " iterations")
    return (a + b) / 2
