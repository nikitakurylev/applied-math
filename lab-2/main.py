import gradient_descent as gd
import numpy as np

fn1 = lambda xy: xy[0] ** 2 + xy[1] ** 2

print(gd.gradient_descent(fn1, [70., 50.], 0.001, 1.,));