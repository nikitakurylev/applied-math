import gradient_descent as gd
import numpy as np
import conjugate

fn1 = lambda xy: xy[0] ** 2 + xy[1] ** 2 # 0 0
fn2 = lambda x: x[0]**2 + x[1]**2 + 3  #0 0
fn3 = lambda xy: 22 * ((xy[0]-100) ** 4) + 8 * (xy[1] ** 4) #100 0

print(gd.gradient_descent(fn2, [10., 10.], 0.001, 1.,gd.fibonacci_method));
print(conjugate.conjugate_gradient_method(lambda x, y: x ** 2 + y ** 2, np.array([70., 50.]), 0.001))