from cmath import isclose

def calc(func, a, c, precision):
    iteration_count = 0
    k = (3 - 5 ** 0.5) / 2
    x = w = v = (a + c) / 2
    fx = fw = fv = func(x)
    d = e = c - a
    precision /= 10
    while d > precision:
        g = e
        e = d
        if x != w and w != v and x != v and fx != fw and fx != fv and fw != fv:
            try:
                temp_u = parabolic_approximation(x, w, v, fx, fw, fv)
            except Exception:
                break
            if (a + precision <= temp_u <= c - precision) and (abs(temp_u - x) < g / 2):
                u = temp_u
                d = abs(u - x)
                continue

        if x < (c + a) / 2.0:
            u = x + k * (c - x)
            d = c - x
        else:
            u = x - k * (x - a)
            d = x - a
        if abs(u - x) < precision:
            u = x + sign(u - x) * precision

        fu = func(u)
        if fu <= fx:
            if u >= x:
                a = x
            else:
                c = x
            v = w
            w = x
            x = u
            fv = fw
            fw = fx
            fx = fu
        else:
            if u >= x:
                c = u
            else:
                a = u
            if fu <= fw or w == x:
                v = w
                w = u
                fv = fw
                fw = fu
            elif fu <= fv or v == x or v == w:
                v = u
                fv = fu
            iteration_count += 1
    print("Brent method: " + str(iteration_count) + " iterations")
    return (a+c)/2


def parabolic_approximation(x1, x2, x3, f1, f2, f3):
    if isclose(x1, x3) or isclose(f1, f3):
        raise Exception("Too close")
    a = ((f3 - f1) * (x2 - x1) - (f2 - f1) * (x3 - x1)) / (
                (x3 ** 2 - x1 ** 2) * (x2 - x1) - (x2 ** 2 - x1 ** 2) * (x3 - x1))
    b = (f2 - f1 - a * (x2 ** 2 - x1 ** 2)) / (x2 - x1)
    return -b / (2 * a)

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return None


