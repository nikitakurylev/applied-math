from brent import parabolic_approximation

def calc(func, a, b, precision):
    iteration_count = 0
    while b - a > precision:
        x1 = a
        x2 = (a + b) / 2
        x3 = b
        f1 = func(x1)
        f2 = func(x2)
        f3 = func(x3)
        try:
            u = parabolic_approximation(x1, x2, x3, f1, f2, f3)
        except Exception:
            break
        if func(u) < f2:
            if u > x2:
                a = (u + x2) / 2
            else:
                b = (u + x2) / 2
        else:
            if u < x2:
                a = (u + x2) / 2
            else:
                b = (u + x2) / 2
        iteration_count += 1
    print("Parabola method: " + str(iteration_count) + " iterations")
    return (a + b) / 2
