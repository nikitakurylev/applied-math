def calc(func, a, b, precision):
    while b - a > precision:
        x1 = a
        x2 = (a + b) / 2
        x3 = b
        f1 = func(x1)
        f2 = func(x2)
        f3 = func(x3)
        u = x2 - ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f2 - f1))/(2 * (x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))
        if func(u) < f2:
            b = (x2 + x3) / 2
        else:
            a = (x2 + x1) / 2
    return (a + b) / 2
