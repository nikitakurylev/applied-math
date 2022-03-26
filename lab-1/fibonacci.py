import math
def fib(n):
    x1 = (1 + (5 ** 0.5)) / 2
    x2 = (1 - (5 ** 0.5)) / 2
    return math.floor((x1 ** n - x2 ** n) / (5 ** 0.5))

def findMinFib(a,b, precision):
    l = 0
    r = 100
    while(r - l > 1):
        m = (r + l) // 2
        if (b - a) / fib(m) < precision:
            r = m
        else:
            l = m
        return r

def calc(func, a, b, precision):
    n = findMinFib(a, b, precision)
    lambd = a + (fib(n - 2) / fib(n)) * (b - a)
    u = a + (fib(n - 1) / fib(n)) * (b - a)
    k = 1
    e = precision
    while k < n - 2:
        if func(lambd) > func(u):
            a = lambd
            lambd = u
            u = a + (fib(n - k - 1) / fib(n - k)) * (b - a)
            if k == n - 2:
                u = lambd + e
                if func(lambd) > func(u):
                    a = lambd
                else:
                    b = u
            else:
                k += 1
        else:
            b = u
            u = lambd
            lambd = a + (fib(n - k - 2) / fib(n - k)) * (b - a)
            if k == n - 2:
                u = lambd + e
                if func(lambd) > func(u):
                    a = lambd
                else:
                    b = u
            else:
                k += 1
    return (a + b) / 2