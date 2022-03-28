def calc(func, a, b, precision):
    iteration_count = 0
    phi = (1 + (5 ** 0.5)) / 2
    while abs(a - b) > precision:
        x1 = b - (b - a) / phi
        x2 = a + (b - a) / phi
        y1 = func(x1)
        y2 = func(x2)
        if y1 >= y2:
            a = x1
        else:
            b = x2
        iteration_count += 1
    print("Golden section method: " + str(iteration_count) + " iterations")
    return (a + b) / 2