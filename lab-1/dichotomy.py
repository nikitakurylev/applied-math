def calc(func, a, b, precision):
    while b - a > precision:
        middle = (a + b) / 2
        x1 = middle - precision / 3
        x2 = middle + precision / 3
        f1 = func(x1)
        f2 = func(x2)
        if f1 > f2:
            a = x1
        else:
            b = x2
    return (a + b) / 2
