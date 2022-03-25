import math
import dichotomy
import goldenSection

def func(x):
    return math.sin(x) * x ** 3

print(dichotomy.calc(func, -100, 100, 0.1))
print(goldenSection.calc(func, 13, 20, 0.1))