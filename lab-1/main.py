import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1000,1000) 
y = np.sin(x) * x ** 3; 
plt.plot(x, y)
plt.show()