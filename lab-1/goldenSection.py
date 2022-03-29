def calc(func, a, b, precision):
    iteration_count = 0
    phi = 2 - (5 ** 0.5 + 1) / 2
    x1 = (a + phi *(b - a))
    x2 = b - phi * (b - a)
    f1 = func(x1)
    f2 = func(x2)
    while True:
        print("yes")
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + phi * (b - a)
            f1 = func(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - phi * (b - a)
            f2 = func(x2)
        #     b = x2
        iteration_count += 1
        if abs(b - a) < precision:
            break
    return (a + b) / 2, iteration_count