from cProfile import label
from turtle import color

import matplotlib
import gradient_descent as gd
import numpy as np
import matplotlib.pyplot as plt
import conjugate

def draw(ax, x, fn1, name):
    print(name)
    xmin = x[0][0]
    ymin = x[0][1]
    xmax = x[0][0]
    ymax = x[0][1]
    x1 = []
    x2 = []
    y = []
    for i in range(0, len(x)):
        xmin = min(xmin, x[i][0])
        ymin = min(ymin, x[i][1])
        xmax = max(xmax, x[i][0])
        ymax = max(ymax, x[i][1])
        x1.append(x[i][0])
        x2.append(x[i][1])
        y.append(fn1(x[i]))
    ax.plot(x1, x2, label=name)
    print()

def drawmesh(ax, fn1, xmin, xmax, ymin, ymax):
    x1, x2 = np.meshgrid(np.arange(xmin, xmax, 0.5), np.arange(ymin, ymax, 0.5))
    y = fn1([x1,x2])
    ax.contour(x1, x2, y, linewidth=0.5, color="red")

fn1 = lambda xy: 22 * ((xy[0]-100) ** 4) + 8 * (xy[1] ** 4)
#fn1 = lambda xy: xy[0] ** 2 + 2 * (xy[1] + 5) ** 2
fig, ax = plt.subplots()
matplotlib.rcParams['legend.fontsize'] = 10
drawmesh(ax, fn1, -20, 20, -20, 20)
startpoint = [7., 15.]
draw(ax, gd.gradient_descent(fn1, startpoint, 0.001, 2., gd.const_step), fn1, 'const_step')
draw(ax, gd.gradient_descent(fn1, startpoint, 0.001, 1., gd.splitting_method), fn1, 'splitting_method')
draw(ax, gd.gradient_descent(fn1, startpoint, 0.001, 1., gd.golden_section), fn1, 'golden_section')
draw(ax, gd.gradient_descent(fn1, startpoint, 0.001, 1., gd.fibonacci_method), fn1, 'fibonacci_method')
draw(ax, conjugate.conjugate_gradient_method(fn1, np.array(startpoint), 0.001), fn1, 'conjugate_gradient_method')
ax.legend()
plt.show()
