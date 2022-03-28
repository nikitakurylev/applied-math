def calc(func, a, b, precision):
    iteration_count = 0
    phi = (5 ** 0.5 - 1) / 2
    while b - a > precision:
        x1 = a + (b - a) * phi
        x2 = b - (b - a) * phi
        y1 = func(x1)
        y2 = func(x2)
        if y1 < y2:
            a = x1
        else:
            b = x2
        iteration_count += 1
    return (a + b) / 2, iteration_count