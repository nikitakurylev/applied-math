import math
import matplotlib.pyplot as plt

import dichotomy
import goldenSection
import parabola
import fibonacci
import brent



def func(x):
    return math.sin(x) * x ** 3


print(dichotomy.calc(func, 13, 20, 0.1))
print(goldenSection.calc(func, 13, 20, 0.1))
print(fibonacci.calc(func, 13, 20, 0.1))
print(parabola.calc(func, 13, 20, 0.1))
print(brent.calc(func, 13, 20, 0.1))

powerOfTen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dichotomyIterations = []
goldenSectionIterations = []
fibonacciIterations = []
parabolaIterations = []
brentIterations = []

a, b = 13, 20

for i in powerOfTen:
    precision = 10 ** -i
    dichotomyIterations.append(dichotomy.calc(func, a, b, precision)[1])
    goldenSectionIterations.append(goldenSection.calc(func, a, b, precision)[1])
    fibonacciIterations.append(fibonacci.calc(func, a, b, precision)[1])
    parabolaIterations.append(parabola.calc(func, a, b, precision)[1])
    brentIterations.append(brent.calc(func, a, b, precision)[1])
lineObjects = plt.plot(powerOfTen, dichotomyIterations,  powerOfTen, goldenSectionIterations, powerOfTen, fibonacciIterations, powerOfTen, parabolaIterations, powerOfTen, brentIterations)
plt.xlabel("Precision")
plt.ylabel("Iterations")
plt.locator_params(axis='x', nbins=len(powerOfTen))
plt.legend(lineObjects, ('dichotomy', 'goldenSection', 'fibonacci', 'parabola', 'brent'))
plt.show()