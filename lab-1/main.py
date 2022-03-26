import math
import dichotomy
import goldenSection
import parabola
import fibonacci

def func(x):
    return math.sin(x) * x ** 3

print(dichotomy.calc(func, 13, 20, 0.1))
print(goldenSection.calc(func, 13, 20, 0.1))
print(parabola.calc(func, 13, 20, 0.1))
print(fibonacci.calc(func, 13, 20, 0.1))