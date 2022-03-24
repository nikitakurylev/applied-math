import math
import dichotomy

def func(x):
    return math.sin(x) * x ** 3

print(dichotomy.calc(func, -100, 100, 0.1))