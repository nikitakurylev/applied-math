from turtle import color
import gradient_descent as gd
import numpy as np
import matplotlib.pyplot as plt

fn1 = lambda xy: xy[0] ** 2 + xy[1] ** 3 + xy[0] ** 4

x = gd.gradient_descent(fn1, [50., 50.], 0.001, 1.,)
xmin = x[0][0]
ymin = x[0][1]
xmax = x[0][0]
ymax = x[0][1]
x1 = []
x2 = []
y = []

curx = [x[0][0], x[0][1]]
for i in range(0, len(x)):
    xmin = min(xmin, x[i][0])
    ymin = min(ymin, x[i][1])
    xmax = max(xmax, x[i][0])
    ymax = max(ymax, x[i][1])
    x1.append(x[i][0])
    x2.append(x[i][1])
    y.append(fn1(x[i]))
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

ax.plot3D(x1, x2, y)

x1, x2 = np.meshgrid(np.arange(xmin, xmax, 0.1), np.arange(ymin, ymax, 0.1))
y = fn1([x1,x2])

ax.plot_wireframe(x1, x2, y, linewidth=0.5, color="red")
plt.show()